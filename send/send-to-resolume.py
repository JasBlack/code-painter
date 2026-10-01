#!/usr/bin/env python3
"""Code Painter by JAS.BLACK: sender.

Takes the painting from the studio (switch on "send" in its out panel) and offers it to Resolume or any VJ app as a
live source called "Code Painter": a Syphon server on a Mac, a Spout sender on Windows.

Start it with the launcher next to it (send-to-resolume.command on a Mac, send-to-resolume.bat on Windows): the first
time, it sets up what it needs (a minute; it needs Python 3.9-3.12 on a Mac, 3.9+ on Windows).

    python send-to-resolume.py [--name "Code Painter"] [--port 8792] [--flip]
"""
import argparse
import asyncio
import io
import json
import sys
import time

from PIL import Image


def make_output(name, flip):
    """(how it is offered, publish(rgba_bytes, w, h), idle(), close())"""
    if sys.platform == 'darwin':
        import syphon
        from syphon.utils.raw import create_mtl_texture, copy_bytes_to_mtl_texture
        from Foundation import NSDate, NSRunLoop
        server = syphon.SyphonMetalServer(name)
        state = {'tex': None, 'size': None}

        def publish(buf, w, h):
            if state['size'] != (w, h):
                state['tex'] = create_mtl_texture(server.device, w, h)
                state['size'] = (w, h)
            copy_bytes_to_mtl_texture(buf, state['tex'])
            server.publish_frame_texture(state['tex'], is_flipped=flip)

        def idle():
            # Syphon finds its servers through system notifications: let them through
            NSRunLoop.currentRunLoop().runUntilDate_(NSDate.dateWithTimeIntervalSinceNow_(0.001))

        return 'Syphon', publish, idle, server.stop

    if sys.platform == 'win32':
        import SpoutGL
        from OpenGL import GL
        sender = SpoutGL.SpoutSender()
        sender.setSenderName(name)

        def publish(buf, w, h):
            sender.sendImage(buf, w, h, GL.GL_RGBA, flip, 0)
            sender.setFrameSync(name)

        return 'Spout', publish, (lambda: None), sender.releaseSender

    raise SystemExit('The sender works on macOS (Syphon) and Windows (Spout).')


async def serve(args):
    import websockets
    via, publish, idle, close = make_output(args.name, args.flip)
    stats = {'frames': 0, 't': time.time(), 'clients': 0}

    async def handler(ws):
        size = None
        stats['clients'] += 1
        print(f'  studio connected — sending to {via} as "{args.name}"', flush=True)
        await ws.send(json.dumps({'hello': True, 'via': via, 'name': args.name}))
        try:
            async for msg in ws:
                if isinstance(msg, str):
                    m = json.loads(msg)
                    if 'size' in m:
                        size = (int(m['size'][0]), int(m['size'][1]))
                        print(f'  frame size {size[0]}×{size[1]}', flush=True)
                    continue
                if msg[:2] == b'\xff\xd8':            # a JPEG frame (what the studio sends)
                    t0 = time.perf_counter()
                    im = Image.open(io.BytesIO(msg)).convert('RGBA')
                    t1 = time.perf_counter()
                    publish(im.tobytes(), im.width, im.height)
                    stats['frames'] += 1
                    if args.verbose and stats['frames'] % 15 == 0:
                        print(f'  {len(msg) // 1024} KB  decode {1000 * (t1 - t0):.0f} ms  publish {1000 * (time.perf_counter() - t1):.0f} ms  since last {1000 * (t0 - stats.get("last", t0)):.0f} ms', flush=True)
                    stats['last'] = t0
                elif size and len(msg) == size[0] * size[1] * 4:   # raw RGBA
                    publish(msg, *size)
                    stats['frames'] += 1
                await ws.send('{"ack":1}')
                now = time.time()
                if now - stats['t'] > 10:
                    print(f'  {stats["frames"] / (now - stats["t"]):.0f} fps', flush=True)
                    stats['frames'], stats['t'] = 0, now
        except websockets.ConnectionClosed:
            pass
        finally:
            stats['clients'] -= 1
            print('  studio disconnected (the source stays, showing the last frame)', flush=True)

    async def pump():
        while True:
            idle()
            await asyncio.sleep(0.02)

    try:
        async with websockets.serve(handler, '127.0.0.1', args.port, max_size=128 * 1024 * 1024, compression=None):
            print(f'Code Painter sender: ready ({via} "{args.name}", port {args.port}).', flush=True)
            print('In the studio, switch on "send" (out panel). Close this window to stop.', flush=True)
            await pump()
    except OSError as e:
        raise SystemExit(f'Port {args.port} is busy: is the sender already running? ({e})')
    finally:
        close()


def main():
    p = argparse.ArgumentParser(description='Send the Code Painter studio to Syphon (Mac) / Spout (Windows).')
    p.add_argument('--name', default='Code Painter', help='the source name the VJ app shows')
    p.add_argument('--port', type=int, default=8792, help='local port the studio connects to (the studio uses 8792)')
    p.add_argument('--flip', action='store_true', help='flip the picture vertically (if it arrives upside down)')
    p.add_argument('--verbose', action='store_true', help='print timings')
    args = p.parse_args()
    try:
        asyncio.run(serve(args))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
