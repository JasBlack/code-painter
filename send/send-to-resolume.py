#!/usr/bin/env python3
"""Code Painter by JAS.BLACK: the bridge to Resolume and other VJ apps.

Out: the painting from the studio (switch on "send" in its out panel) as a live source called "Code Painter", and
     (with "code" on) its code as "Code Painter code".
In:  any Syphon / Spout source (Resolume's output, another app) as a live input of the studio
     (live input → Syphon / Spout).
On a Mac it uses Syphon, on Windows Spout.

Start it with the launcher next to it (send-to-resolume.command on a Mac, send-to-resolume.bat on Windows): the first
time, it sets up what it needs (a minute; it needs Python 3.9-3.12 on a Mac, 3.9+ on Windows).

    python send-to-resolume.py [--name "Code Painter"] [--port 8792] [--flip] [--flip-in] [--in-size 1920]
"""
import argparse
import array
import asyncio
import io
import json
import sys
import time

from PIL import Image


# ── Syphon (macOS) / Spout (Windows) ──────────────────────────────────────────────────────────────────────────────
class Backend:
    via = ''

    def output(self, name, flip):          # -> (publish(rgba_bytes, w, h), close())
        raise NotImplementedError

    def sources(self, own):                # -> [{'id', 'name'}] (our own outputs left out)
        raise NotImplementedError

    def source(self, sid):                 # -> reader with read() -> (bytes, w, h, 'RGBA' | 'BGRA') | None, and close()
        raise NotImplementedError

    def idle(self):
        pass


class SyphonBackend(Backend):
    via = 'Syphon'

    def __init__(self):
        import syphon
        import Metal
        from Foundation import NSDate, NSRunLoop
        from syphon.utils.raw import create_mtl_texture, copy_bytes_to_mtl_texture, copy_mtl_texture_to_bytes
        self.syphon, self.Metal, self.NSDate, self.NSRunLoop = syphon, Metal, NSDate, NSRunLoop
        self.create, self.put, self.get = create_mtl_texture, copy_bytes_to_mtl_texture, copy_mtl_texture_to_bytes
        self.directory = syphon.SyphonServerDirectory()

    def output(self, name, flip):
        server = self.syphon.SyphonMetalServer(name)
        state = {'tex': None, 'size': None}

        def publish(buf, w, h):
            if state['size'] != (w, h):
                state['tex'] = self.create(server.device, w, h)
                state['size'] = (w, h)
            self.put(buf, state['tex'])
            server.publish_frame_texture(state['tex'], is_flipped=flip)

        return publish, server.stop

    def sources(self, own):
        out = []
        for d in self.directory.servers:
            if d.name in own:
                continue
            label = f'{d.app_name} – {d.name}' if d.name and d.app_name else (d.name or d.app_name or 'Syphon source')
            out.append({'id': d.uuid, 'name': label})
        return out

    def source(self, sid):
        desc = next((d for d in self.directory.servers if d.uuid == sid), None)
        if desc is None:
            raise LookupError('that source is no longer there')
        client = self.syphon.SyphonMetalClient(desc)
        bk = self

        class Reader:
            def read(self):
                if not client.has_new_frame:
                    return None
                tex = client.new_frame_image
                if tex is None:
                    return None
                w, h = tex.width(), tex.height()
                mode = 'BGRA' if tex.pixelFormat() == bk.Metal.MTLPixelFormatBGRA8Unorm else 'RGBA'
                return bytes(bk.get(tex)), w, h, mode

            def close(self):
                client.stop()

        return Reader()

    def idle(self):
        # Syphon finds servers and clients through system notifications: let them through
        self.NSRunLoop.currentRunLoop().runUntilDate_(self.NSDate.dateWithTimeIntervalSinceNow_(0.001))


class SpoutBackend(Backend):
    via = 'Spout'

    def __init__(self):
        import SpoutGL
        from OpenGL import GL
        self.SpoutGL, self.GL = SpoutGL, GL

    def output(self, name, flip):
        sender = self.SpoutGL.SpoutSender()
        sender.setSenderName(name)

        def publish(buf, w, h):
            sender.sendImage(buf, w, h, self.GL.GL_RGBA, flip, 0)
            sender.setFrameSync(name)

        return publish, sender.releaseSender

    def sources(self, own):
        r = self.SpoutGL.SpoutReceiver()
        try:
            names = list(r.getSenderList() or [])
        finally:
            r.releaseReceiver()
        return [{'id': n, 'name': n} for n in names if n not in own]

    def source(self, sid):
        r = self.SpoutGL.SpoutReceiver()
        r.setReceiverName(sid)
        GL = self.GL
        state = {'buf': None, 'w': 0, 'h': 0}

        class Reader:
            def read(self):
                ok = r.receiveImage(state['buf'], GL.GL_RGBA, False, 0)
                if r.isUpdated():
                    state['w'], state['h'] = r.getSenderWidth(), r.getSenderHeight()
                    state['buf'] = array.array('B', bytes(state['w'] * state['h'] * 4))
                    return None
                if state['buf'] is not None and ok and r.isFrameNew():
                    return state['buf'].tobytes(), state['w'], state['h'], 'RGBA'
                return None

            def close(self):
                r.releaseReceiver()

        return Reader()


def backend():
    if sys.platform == 'darwin':
        return SyphonBackend()
    if sys.platform == 'win32':
        return SpoutBackend()
    raise SystemExit('The bridge works on macOS (Syphon) and Windows (Spout).')


# ── frames ────────────────────────────────────────────────────────────────────────────────────────────────────────
def decode(jpeg):                          # the studio's JPEG -> RGBA bytes
    im = Image.open(io.BytesIO(jpeg)).convert('RGBA')
    return im.tobytes(), im.width, im.height


def encode(frame, limit, flip):            # a source's pixels -> JPEG for the studio (long side at most `limit`)
    data, w, h, mode = frame
    im = Image.frombuffer('RGBA', (w, h), data, 'raw', mode, 0, 1).convert('RGB')
    if flip:
        im = im.transpose(Image.FLIP_TOP_BOTTOM)
    if max(w, h) > limit:
        im.thumbnail((limit, limit))
    out = io.BytesIO()
    im.save(out, 'JPEG', quality=88)
    return out.getvalue()


async def serve(args):
    import websockets
    bk = backend()
    names = [args.name, args.name + ' code']          # what the studio sends: 0 = the painting, 1 = its code
    outputs = {}
    loop = asyncio.get_running_loop()
    stats = {'frames': 0, 't': time.time()}

    def out(ch):
        if ch not in outputs:
            outputs[ch] = bk.output(names[ch], args.flip)
            print(f'  {bk.via} source "{names[ch]}" is on', flush=True)
        return outputs[ch]

    async def handler(ws):
        st = {'reader': None, 'inflight': 0, 'task': None}
        print('  studio connected', flush=True)
        await ws.send(json.dumps({'hello': True, 'via': bk.via, 'name': args.name}))

        async def pump():                  # the chosen source -> the studio, as fast as it takes them (2 on their way)
            while st['reader'] is not None:
                if st['inflight'] >= 2:
                    await asyncio.sleep(0.004)
                    continue
                try:
                    frame = st['reader'].read()
                except Exception as e:
                    await ws.send(json.dumps({'inerr': f'reading the source failed ({e})'}))
                    break
                if frame is None:
                    await asyncio.sleep(1 / 120)
                    continue
                jpeg = await loop.run_in_executor(None, encode, frame, args.in_size, args.flip_in)
                st['inflight'] += 1
                await ws.send(jpeg)
                await asyncio.sleep(1 / 120)

        def stop_input():
            if st['reader'] is not None:
                try:
                    st['reader'].close()
                except Exception:
                    pass
                st['reader'] = None
            st['inflight'] = 0

        try:
            async for msg in ws:
                if isinstance(msg, str):
                    m = json.loads(msg)
                    if 'sources' in m:
                        await ws.send(json.dumps({'sources': bk.sources(set(names))}))
                    if 'in' in m:
                        stop_input()
                        if m['in']:
                            try:
                                st['reader'] = bk.source(m['in'])
                                print(f'  input: {m["in"]}', flush=True)
                                if st['task'] is None or st['task'].done():
                                    st['task'] = asyncio.ensure_future(pump())
                            except Exception as e:
                                await ws.send(json.dumps({'inerr': str(e)}))
                    if 'inack' in m:
                        st['inflight'] = max(0, st['inflight'] - 1)
                    continue
                ch, jpeg = msg[0], msg[1:]
                if ch < len(names) and jpeg[:2] == b'\xff\xd8':
                    rgba, w, h = await loop.run_in_executor(None, decode, jpeg)
                    out(ch)[0](rgba, w, h)
                    if ch == 0:
                        stats['frames'] += 1
                await ws.send(json.dumps({'ack': 1, 'ch': int(ch)}))
                now = time.time()
                if args.verbose and now - stats['t'] > 5:
                    print(f'  sending {stats["frames"] / (now - stats["t"]):.0f} fps', flush=True)
                    stats['frames'], stats['t'] = 0, now
        except websockets.ConnectionClosed:
            pass
        finally:
            stop_input()
            print('  studio disconnected (the sources stay, showing their last frame)', flush=True)

    async def pump_system():
        while True:
            bk.idle()
            await asyncio.sleep(0.02)

    try:
        async with websockets.serve(handler, '127.0.0.1', args.port, max_size=128 * 1024 * 1024, compression=None):
            print(f'Code Painter bridge: ready ({bk.via}, port {args.port}).', flush=True)
            print(f'  out: in the studio press "send" (out panel) - sources "{names[0]}" (+ "{names[1]}" with code on)', flush=True)
            print(f'  in:  in the studio pick live input -> Syphon / Spout', flush=True)
            print('Close this window to stop.', flush=True)
            await pump_system()
    except OSError as e:
        raise SystemExit(f'Port {args.port} is busy: is the bridge already running? ({e})')
    finally:
        for publish, close in outputs.values():
            try:
                close()
            except Exception:
                pass


def main():
    try:                                   # (never let an odd character in a message stop the bridge)
        sys.stdout.reconfigure(errors='replace')
    except Exception:
        pass
    p = argparse.ArgumentParser(description='Code Painter <-> Syphon (Mac) / Spout (Windows) bridge.')
    p.add_argument('--name', default='Code Painter', help='the source name the VJ app shows')
    p.add_argument('--port', type=int, default=8792, help='local port the studio connects to (the studio uses 8792)')
    p.add_argument('--flip', action='store_true', help='flip what is sent vertically (if it arrives upside down)')
    p.add_argument('--flip-in', action='store_true', help='flip what comes in vertically (if it arrives upside down)')
    p.add_argument('--in-size', type=int, default=1920, help='largest side of an incoming source (pixels)')
    p.add_argument('--verbose', action='store_true', help='print the frame rate')
    args = p.parse_args()
    try:
        asyncio.run(serve(args))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
