# Code Painter: the guide

Code Painter repaints any picture, video or live camera stroke by stroke, and writes the code for every stroke as it goes. It runs entirely in your browser: nothing you drop in is uploaded.

**Open it:** [paint.jas.black](https://paint.jas.black)

---

## Quick start (one minute)

1. Open the site. On a first visit you land in **easy** mode.
2. Press **▶ try a demo**, or **open picture / video** (or drop a file anywhere on the page).
3. Pick a **look** (pencil sketch, graffiti, watercolour, ink drawing, liquid chrome, hylics).
4. Pick a **path**: *free*, *one line*, *spiral out* or *top → bottom*. Each press of ▶ try a demo shows the next one.
5. Press **record video**, **save picture** or **save as code**.

When you want more control, switch to **console** (top left).

---

## Easy mode and console

| | |
|---|---|
| **easy** | Four steps down the left: *source · look · motion · export*. Each one has a "more ▸" link that opens the console at the right panel. |
| **console** | Every control. Hover any control for a description of what it does. |
| **phone** | On a phone the page gives you the painting with its code, plus the essentials: photo/video, camera, looks, path, styles, speed, restart, record and save. |

---

## Sources

- **Pictures**: drop one, or several to make a **playlist**.
- **Videos**: repainted live, frame by frame. The *video sound* button chooses what happens to the video's own sound: *off*, *keep* (it goes into the recording, nothing else changes), or *music* (it drives the painting).
- **Live input**: the camera, a shared screen, or a 3D model you can turn.
- **Text**: type a word and it's painted.
- **Examples**: a menu of ready pictures.
- **Playlist** (up to 10 slots): *cycle* (each holds for a few seconds), *hand* (you play them), *bars* (they change on the song's bars).

## Styles (48)

Styles are grouped in tabs. Tick several and every stroke picks one of them. Right-click a style key to give that style its own size.

| tab | styles |
|---|---|
| **paint** | paint, oil, acrylic, palette knife, gouache, watercolour, wet watercolour, sumi, ink, calligraphy, graffiti, soft |
| **draw** | pencil, charcoal, pastel, pen, hatch, marker |
| **graphic** | flat, geo, dots, halftone, scribble, string, paper, bokeh, neon, hylics, linocut, riso |
| **craft** | thread, cross-stitch, clay, beads, foam, tape |
| **3d** | ceramic, stone, puffy, metal, molten, pewter, copper, gold, bronze, glass, lens, crystal |

- **3d** styles and oil / acrylic / knife are lit in 3D: the light follows the **light pad**, and you can drag it.
- **Glass**, **lens** and **crystal** bend the picture behind them.
- The **brush** menu only changes the plain styles (paint, soft, flat, geo, hatch, string). Every other style draws with its own tool.

## Motion: how a stroke arrives

The options are *draw, glide, sketch, ink, spiral, fall, pop, shard, pixel* and *hilite*. Tick several and each stroke picks one.

## Path: how the painter travels

- **order**: *free* (the biggest mistake first), *top → bottom*, *bottom → top*, *left → right*, *right → left*, *diagonal*, *spiral out / in*, *rings out / in*, or *clock sweep*.
- **one line**: a pen that never lifts. With music, *beats: branch* splits the line on every beat.
- **outlines**: the picture's real lines, drawn first or last.
- **shapes by hand**: big patches of one colour get their outline traced, then are scribbled in (*outline + scribble*, *outline + rows*, *scribble*).
- **cuts**: when a video cuts to a new scene, the change is either drawn or pre-drawn.

Order and one line also work in playlists.

## Brush panel

- **detail**: *fast*, *sharp*, *ultra*, *max* or *hq*.
- **shapes**: *auto* picks a stroke count from the stroke size.
- **size**: the stroke-size knob, or *rnd* for random sizes.
- **fill**: how a tool fills a stroke much wider than itself: *zigzag*, *cross* or *one stroke*.

## Music

Load a song, or use live sound.

- **hits**: strokes land on the song's hits.
- **flow**: the painting follows the song's energy.
- **free**: hits throw bursts of strokes.
- **sections**: drops paint bolder, breaks paint calmer.
- **beats**:
  - *glow*: strokes that land on a beat light up.
  - *branch*: in one-line mode, the line splits on each beat.
  - *glow + branch*: both.
- **fx**: punch zoom, flashing border, grid pulse.

## Recording and export

- **⏺ render** (the default): the run starts again and is rendered frame by frame, perfectly smooth, at **720p, 1080p, 1440p or 4K**. The message line shows how long is left.
- **⏺ live**: the stage in real time. **interface** records the whole page; **from now** records the stage from this moment on.
- **⬇ code**: a small web page that paints the picture again by itself, stroke by stroke, in the same styles (self-playing, with the song if you like).
- **svg**, **png 1K / 4K / 8K**, **stills**, **contact sheet**, **cover**.
- **window**: open the painting on its own, for a projector or a second screen.

## Local version: Resolume and more

`download/code-painter-local.zip` (also *resolume ↓* in the studio) is the studio run from your own computer, on Mac or Windows. It adds **Syphon / Spout** in and out for Resolume and other VJ software. Unzip it and double-click *start.command* (Mac) or *start.bat* (Windows).

---

## How it works

1. The picture is analysed for edges, detail and important areas.
2. A **worker** (a background thread) proposes candidate strokes where the painting differs most from the picture. Each candidate is scored by how much closer it would bring the canvas to the picture, and the best one is kept and refined.
3. The chosen stroke is sent to the page, which draws it in its style and adds its line to the code.
4. The 3D styles are drawn into a **height map** (with a material and a direction per pixel), lit by a **WebGL 2** shader with shadows, reflections and, for glass, lens and crystal, refraction.
5. Saving the code packs the strokes and the style renderers into one HTML file, so the painting can be replayed anywhere.

## Example outputs

| | | |
|---|---|---|
| ![pencil](examples/pencil.webp) | ![graffiti](examples/graffiti.webp) | ![oil](examples/oil.webp) |
| pencil | graffiti | oil |
| ![acrylic](examples/acrylic.webp) | ![watercolour](examples/watercolour.webp) | ![linocut](examples/linocut.webp) |
| acrylic | watercolour | linocut |
| ![riso](examples/riso.webp) | ![bronze](examples/bronze.webp) | ![glass](examples/glass.webp) |
| riso | bronze | glass |

## Tips

- A portrait or a picture with a clear subject paints best.
- **Lower the stroke count** for bold, graphic pictures; **raise it** (or use *hq*) for detail.
- To make the music obvious, use **one line + beats: glow + branch**.
- Rendering at 4K takes about four times as long as 1080p.
