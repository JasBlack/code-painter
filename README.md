# Code Painter by JAS.BLACK

Version 4.9.4

Drop in any picture and watch it painted in code, stroke by stroke, with the program writing itself underneath.
Add a song and the painting follows its hits and sections; add stroke sounds and every stroke plays a note.
Record it as an MP4 (in real time, or rendered frame by frame), save the code, an SVG, 4K / 8K PNGs, stills and covers.

Everything runs in the browser: pictures, songs and videos never leave the computer. No account, no server.
Best in Chrome, Edge or Brave on a desktop or laptop (Safari works too).

## Use it

- **Online**: open the studio's link. It opens painting a JAS.BLACK picture; pick a demo, type a word or drop your
  own picture / video / song to take over.
- **From this folder**: double-click `index.html`. Everything works except the 3D input, which needs the online
  version.

## Resolume (out and in)

The bridge app in `send/` connects the studio to Resolume (or any VJ app) on this computer: Syphon on a Mac, Spout on
Windows. Online, the browser may ask to let the page reach apps on this computer: allow it.

1. Double-click `send/send-to-resolume.command` (Mac; right-click → Open the first time) or
   `send/send-to-resolume.bat` (Windows). The first time it sets itself up (about a minute; it needs Python 3.9 – 3.12
   on a Mac, 3.9+ on Windows, from python.org). Keep its window open.
2. **Out**: press *send* (top of the out panel): it blinks until it finds the bridge, then lights green. In Resolume:
   Sources → Syphon / Spout → *Code Painter*. With *code* on, the code goes out too as *Code Painter code* (text on
   black: layer it with Add or Screen).
3. **In**: switch on Resolume's Syphon / Spout output, then pick *live input → Syphon / Spout* in the studio.

## What's in here

- `index.html`: opens the studio
- `studio/index.html`: the whole app in one page (its code, the painter's and the recorder's)
- `studio/viewer3d.js` + `studio/vendor/three/`: the 3D input (three.js, MIT licence, see its LICENSE)
- `send/`: the bridge to Resolume / VJ apps (Syphon on a Mac, Spout on Windows; out and in)

© 2026 JAS.BLACK. All rights reserved.
