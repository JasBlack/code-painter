# Code Painter by JAS.BLACK

Drop in any picture and watch it painted in code, stroke by stroke, with the program writing itself underneath.
Add a song and the painting follows its hits and sections; add stroke sounds and every stroke plays a note.
Record it as an MP4 (in real time, or rendered frame by frame), save the code, an SVG, 4K / 8K PNGs, stills and covers.

Everything runs in the browser: pictures, songs and videos never leave the computer. No account, no server.
Best in Chrome, Edge or Brave on a desktop or laptop (Safari works too).

## Use it

- **From this folder**: double-click `index.html`. Everything works except the 3D input, which needs the page opened
  from a web address (a host, or a local server).
- **Online**: put the folder on a host (below) and open its link.

## Send it to Resolume

*send* (top of the out panel) plays the painting live into Resolume (or any VJ app) as a source called
**Code Painter**: Syphon on a Mac, Spout on Windows. It goes through a small sender app that runs on your computer
(`send/` in this folder; it works with the studio opened from the disk or from a website):

1. Double-click `send/send-to-resolume.command` (Mac; right-click → Open the first time) or
   `send/send-to-resolume.bat` (Windows). The first time it sets itself up (about a minute; it needs Python 3.9 – 3.12
   on a Mac, 3.9+ on Windows, from python.org). Keep its window open.
2. In the studio press *send*: it blinks until it finds the sender, then lights green.
3. In Resolume: Sources → Syphon / Spout → *Code Painter*.

## Put it online (free)

It is a plain static site: any static host works, no server code, no database.

- **Netlify Drop** (quickest): go to https://app.netlify.com/drop and drag this whole folder onto the page. You get a
  link straight away (sign up, free, to keep it and give it a name).
- **GitHub Pages**: create a public repository, upload the contents of this folder (GitHub Desktop is easiest), then
  Settings → Pages → "Deploy from a branch", branch `main`, folder `/ (root)`, Save. After a minute it is at
  `https://<username>.github.io/<repository>/`.
- **Cloudflare Pages**: Workers & Pages → Create → Pages → "Upload assets", drop this folder.

Hosts serve it over https, which the camera, the microphone, screen / tab recording and the video encoder need.
To update: replace the files with a newer version (GitHub redeploys by itself; on Netlify drag the folder on again).

## What's in here

- `index.html`: opens the studio
- `studio/index.html`: the whole app in one page (its code, the painter's and the recorder's)
- `studio/viewer3d.js` + `studio/vendor/three/`: the 3D input (three.js, MIT licence, see its LICENSE)
- `send/`: the sender for Resolume / VJ apps (Syphon on a Mac, Spout on Windows)

© 2026 JAS.BLACK. All rights reserved.
