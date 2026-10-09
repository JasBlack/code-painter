# Code Painter by JAS.BLACK

Version 4.15.0

Drop in any picture and watch it painted in code, stroke by stroke, with the program writing itself underneath.
Add a song and the painting follows its hits and sections; add stroke sounds and every stroke plays a note.
Record it as an MP4 (in real time, or rendered frame by frame), save the code, an SVG, 4K / 8K PNGs, stills and covers.
*window* (top of the out panel) opens the painting in a window of its own: drag it to a projector or a second screen
and double-click it for full screen.

Everything runs in the browser: pictures, songs and videos never leave the computer. No account, no server.
Best in Chrome, Edge or Brave on a desktop or laptop (Safari works too).

## Use it

- **Online**: open the studio's link. It opens painting a JAS.BLACK picture; pick a demo, type a word or drop your
  own picture / video / song to take over.
- **On a phone**: the same link. A small screen gets its own layout: the painting (4:5, or 9:16 for reels) with
  its code over it and the essentials under it (a photo / video, the camera, the examples, style, shapes, speed,
  restart, record, save). The full studio, with every control, is for a computer.
- **From this folder**: double-click `index.html`. Everything works except the 3D input, which needs the online
  version.
- **With Resolume** (Syphon / Spout in and out): a website can't reach other apps, so that is in the **local
  version**, a free download for Mac and Windows: *resolume ↓* in the studio's out panel, or
  `download/code-painter-local.zip`.

## What's in here

- `index.html`: the studio, the whole app in one page (its code, the painter's and the recorder's)
- `viewer3d.js` + `vendor/three/`: the 3D input (three.js, MIT licence, see its LICENSE)
- `CNAME`: the site's address for GitHub Pages (paint.jas.black): keep it with the other files
- `og-image.jpg`: the picture a shared link shows (the page's link preview points to it at https://paint.jas.black/)
- `download/code-painter-local.zip`: the local version (the studio run from your own computer, with the Resolume bridge)
- `studio/index.html`: forwards old links (…/studio/) to the studio

## Credits

The wet, pencil and charcoal styles use ideas from p5.brush by Alejandro Campos Uribe (MIT licence, https://github.com/acamposuribe/p5.brush: stamped brush lines with a pressure profile) and Tyler Hobbs' watercolour method (a fractal-edged outline stacked in transparent layers), written again for this painter.

© 2026 JAS.BLACK. All rights reserved.
