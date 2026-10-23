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

**More room for the painting** (top right): **ui** sets the size of the controls (*auto* makes them smaller on a smaller window, or pick 70–110%), and the panel button (or the **H** key) hides the panels under the painting.

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
- **one line**: a pen that never lifts. With music, *branch* (on the beat) splits the line on every beat.
- **circles** (*circles · ink* or *circles · colour*, in the line menu): the picture's lines are joined into one closed path and drawn by a chain of spinning circles (a Fourier series, up to 300 circles), the way the epicycle drawing videos do it. The circles show while it draws and disappear at the end. *trace · ink* and *trace · colour* draw the same loop without showing the circles.
- **outlines**: the picture's real lines, drawn first or last.
- **shapes by hand**: big patches of one colour get their outline traced, then are scribbled in (*outline + scribble*, *outline + rows*, *scribble*).
- **cuts**: when a video cuts to a new scene, the change is either drawn or pre-drawn. With *pre-drawn*, recordings have no pause: ⏺ render pre-draws between frames, and ⏺ live leaves the pre-draw out of the file (the song waits with it). The video cuts straight to the new scene, already painted.

Order and one line also work in playlists.

## Brush panel

- **detail**: *fast*, *sharp*, *ultra*, *max* or *hq*.
- **shapes**: *auto* picks a stroke count from the stroke size.
- **size**: the stroke-size knob, or *rnd* for random sizes.
- **faces** (*off*, *detail*, *max*): face detail. Faces are found in the picture, or in every frame of a video, and painted with more, finer strokes, the eyes and mouth most. It uses Google's MediaPipe face detector, which runs on your computer (nothing is sent anywhere) and loads the first time you switch it on. It finds faces that fill a good part of the frame, and needs the page served (online, or the local version's start.command), not opened as a file.
- **fill**: how a tool fills a stroke much wider than itself: *one stroke* (the default), *zigzag* or *cross*.
- **spray** (for the graffiti style):
  - The paint goes down as a cloud of fine droplets, the way a real can (or a Photoshop / Affinity spray brush) lays it: a grainy body, a fine overspray mist round it, a few splatters and drips.
  - **cap**: the nozzle. *auto* picks skinny caps for thin lines, fat caps for fills and soft for big areas. *skinny* is sharp with little overspray; *fat* is wide, with more mist and drips; *calligraphy* is a flat cap whose ribbon thins and thickens with the angle; *soft* is a wide fog.
  - **wall**: *canvas*, *concrete* or *brick*. The paint takes on the wall's texture as if it was sprayed onto it. The wall shows on screen, in stills and in recordings; saved code paints on plain canvas.
  - **finish**: *clean* (the default: base colours and big shapes first, then the detail, nothing added at the end) or *+ lines*: once the piece is painted, black outlines and white shines are sprayed over it.

## Music

Load a song, pick one of the 10 **demo ♪** songs (house, boom bap, drum & bass, techno, trap, lo-fi, dubstep, synthwave, breakbeat, ambient: 18–28 s each, each with a quiet part, a build and a drop), or use live sound.

- **hits**: strokes land on the song's hits.
- **flow**: the painting follows the song's energy.
- With **hits** and **flow** (and with *one line*), the **speed** slider sets how much of the song the painting takes. At its default (×3) the last stroke lands at the song's end; faster finishes sooner, with more strokes on each hit; slower leaves the rest to be painted after the song, at that pace.
- **free**: hits throw bursts of strokes.
- **sections**: drops paint bolder, breaks paint calmer.
- **music in the paint** (*amount*): how much the song changes the painting itself. At 0 the music only sets the pace.
  - Every beat lands **one big, bold stroke**, snapped down on the beat. With *one line*, the line swells on the beat instead.
  - **Loud parts paint with broad brushes, quiet parts with fine ones.** Loud and quiet are measured against the song itself, so any track gets the full range.
  - On the **3D styles** (oil, acrylic, metals, glass…), **every beat flares the surface**: the light snaps to one side and rakes low, then settles and holds still until the next beat.
- Extras on the beat:
  - *splash*: the brushes being drawn flick drops of their paint off the tip.
  - *branch*: in one-line mode, the line splits on each beat.
  - *glow*: on the beat, the tip of each brush being drawn lights up in its own shape and colour, then fades as it moves on.
- **fx**: punch zoom, flashing border, grid pulse.

## Settings travel with what you make

Every PNG, MP4 (⏺ render or ⏺ live), SVG and ⬇ code page you save carries the settings it was made with, like ComfyUI does with its workflows. **Drop one of those files back onto the page and its settings come back**: styles, motion, path, brush, music mode and amount, splash / branch / glow, recording size and the rest. The picture and the song are not stored: open them again to paint with those settings (a demo song is picked again by itself).

- **Drop it anywhere on the page**, or use **load** in the preset row (under the painting).
- To paint a file that carries settings (instead of loading them), **hold Alt (Option on a Mac) while you drop it**.
- Only files saved from version 4.25.0 on carry settings; an older file is simply opened as a picture or video.

## Score: the sound as a moving score

**score** (music panel, in the *music in the paint* row) shows the song the way producers' audio-reactive visuals do.
A spine down the middle is *now*. The notes still to come (every onset the song analysis finds, hats and ghost notes
included) drift in from the right as small dots. When one reaches the spine it fires: a ring flares on the low hits,
stems drop to the axis on the mids, sprigs and bundles of strands fly off on the highs. Then it scrolls away to the
left with the rest, glowing and smearing. Low notes sit near the middle line, high ones out at the edges. The spine
swells with the sound, and the colours change with the song's sections.

- **score · clean**: crisp lines, rings and dots, like the videos.
- **score · brush**: the same score drawn loose in your ticked styles and brush: gestures that swell and taper, loose loops, dabs. No clean circles or bars.
- **score · organic**: the same score as liquid. Blobs run together, the lanes are wobbling chains of drops, stems are drips, sprigs are splats and the spine is a column of molten drops, with a grain over it.
- **score · nature**: the same dynamics, but the movers are living things wandering over the picture: *cells* (pulse with the bass, split on the hard hits), *plants* (growing tips leave stems in the paint and branch on the hits), *spores* (pods that puff spores on the hits) or *bones* (bone chains that crawl). Pick the form in *shape*. They crawl along the picture's dotted lines, heading for the nearest sleeping dot each time, so they trace the drawing. Each wakes the picture's dots it passes, and a hit wakes a whole patch round it; woken dots become leaves, cells, spore heads or bones in the dot's colour and your styles. Over the song the canvas gets painted where they've been.
- **score · vector**: the picture traced into flat colour shapes, like a vector drawing. The shapes pop in on the notes, biggest first, with a little overshoot and wobble, and are all in by about a third of the song (sooner with a higher *speed*). After that every note kicks a group of shapes (a third of them on the strong notes): they swell, flash and the small ones jump outwards, and the whole picture draws in before a strong note and punches out on it. With a video the shapes are traced again from the frame a couple of times a second. *shape → save svg* saves the shapes as an SVG, sharp at any size.
- **score · motion only**: none of the score drawn. The painting's strokes swell out on the hits, and the painting smears and glows with the bass.

**shape** (the button beside the score menu) reshapes it:

- **picture dots** (on by default): the picture becomes a dotted line drawing: dots an even step apart along its lines and outlines, so you can see what it is without it being drawn. These dots are the notes: the score's figures wake the dots they pass over (a hit wakes more), and each woken dot blooms into a painted mark in its colour, so the picture gets painted where the score goes. *score only* turns it off. With a video, the outlines are read again from the frame showing about three times a second, so they follow the video, and the painted marks fade slowly so the painting follows it too. The colours come from the video as it plays.
- **bg**: the background: *picture* (the picture's own paper tint), *dark*, *black*, *white* or your own colour. On a dark one the lines turn light.
- **dots**: their colour (*picture*, *mono* against the background, *accent*, or your own) and their shape: dot, ring, cross, dash (along the line), square, star. What they paint into keeps the picture's colours.
- **sparsity** (how far apart the picture's dots are) and **dot size**.
- **path**: *line* (as above), *ring* (a circle in the middle: what's coming arrives from outside, the past sinks inwards) or *frame* (a loop round the whole canvas).
- **flows**: which way a line score runs (←, →, ↑, ↓).
- **line position**, **line width**, **line wave** (the line snakes, moving) and **line beads** (smooth or beaded).
- **spread** (how far the lanes reach), **size** (every figure), **speed**, **glow** and **tilt** (turns the whole score).
- **vector colours** (how many flat colours score · vector uses), **vector detail** (how many shapes: low gives a few big ones, high many small ones; tiny specks join their neighbours, so nothing is left empty), **fill** (*flat*; *painted*: each shape filled with brushwork in your ticked styles; *mixed*: flat shapes with brush accents), **outlines** (an ink line round each shape) and **save svg**.
- **echo**: the frames before trail behind, zooming and turning a little more on each hit. 0 is off.

The movers squash and stretch: they gather in just before a strong note, stretch out on it and settle back with a wobble.

Double-click or right-click a slider to put it back; *reset* puts them all back.

The score's colours come from the picture (its strongest colours, its darkest tone for the ink, its lightest for the paper), or from the locked palette when there is one.

The score modes take the layout's frame (9:16, 4:5, 1:1, 16:9) in the *paint* display. Without a song a quiet score
keeps time on its own; with live sound the notes appear as they're heard. It shows on the stage and in recordings.

## Text bar

**text** (out panel) adds your own words between the picture and the code, **one line at a time**. Write one text per
line in the box: each line gets an equal share of the video. Three lines over nine seconds means a new one every three
seconds, and the last one stays to the end. A line comes up whole, with a quick pop, like the text in a reel.

- **font**: ten choices (Archivo Black, Bebas Neue, Playfair, Marker, Caveat, Space Mono, Abril Fatface, Rubik Mono, Pacifico, Rock Salt), carried with the app so they work offline.
- **style**: classic, box (white box), colour box, outline, neon, typewriter, shadow.
- **colour**: white, black, accent or the picture's main colour.

It works in the studio, simple, +code and editor displays, shows in recordings, and the words travel with presets.

## Recording and export

- **⏺ render** (the default): the run starts again and is rendered frame by frame, perfectly smooth, at **720p, 1080p, 1440p or 4K**. The message line shows how long is left.
- **⏺ live**: the stage in real time. **interface** records the whole page; **from now** records the stage from this moment on.
- **⬇ code**: a small web page that paints the picture again by itself, stroke by stroke, in the same styles (self-playing, with the song if you like).
- **svg**, **png 1K / 4K / 8K**, **stills**, **contact sheet**, **cover**. With a live input, a video, a zoom or a playlist (which never finish), **svg** saves the view as it is now. The canvas is traced into flat colour shapes, with the most recent strokes over them as vector strokes.
- **window**: open the painting on its own, for a projector or a second screen.
- **Displays** (above the stage): *studio*, *simple*, *paint*, *+code* and *editor*. *editor* puts the painting beside its code in an editor window (painting.js, window dots, big line numbers, the current line highlighted, "Code Painter by Jas Black" along the bottom). In 16:9 they sit side by side. In the tall frames the painting is as big as it fits, with a thin black trim, and the editor sits under it, lined up with its edges.

## Colour grade

**grade** (in the out panel) opens the colour sliders: *brightness*, *contrast*, *saturation*, *highlights*, *shadows*, *hue*, *colour boost*, *glow* and *haze*. They change the painting as it shows, so recordings get them too, and the saved PNGs, stills and covers. Saved code and SVG keep the plain colours. Double-click a slider to put it back to 0; *reset* clears them all. The **grade** button lights up while any slider is in use.

## Vector base

**vector** (beside *under*, next to the live input menu) puts the picture, traced into flat colour shapes, under a normal painting. The shapes pop in on the notes like *score · vector*, and the painter paints only what they miss: the edges, lines and details, in small strokes in your ticked styles. So graffiti, oil, ink or any style gets a vector base with its own marks on top, using the same caps, wall and piece order as usual. *score → shape → paint over* sets how much it paints over them: low gives only the sharpest edges in fine strokes, so the vector shows most; high gives more and bigger strokes, further out, so the paint shows most. It takes effect on the next painting. The colours, detail and fill of the shapes come from the same panel (*vector colours*, *vector detail*, *fill*). Saved PNGs and stills have the shapes under the strokes.

## Signal

**signal** (in the out panel) sends the painting down a chain of old video gear, on the graphics card, after the grade, the way a real signal would go:

source → colorizer → noize enhancer → the composite wire (with a circuit bend on it) → sync → tape → RF → the TV set → feedback → the tube

The composite wire is the heart of it. The colour rides a carrier wave along each line and the TV decodes it again (with a notch filter, or a comb filter that uses the line above). That is where the dot crawl, the rainbow cross-colour on fine detail and the colour bleed come from. The wire runs at broadcast resolution, one line at a time (with a scanline count, that many lines). Each frame is kept for the feedback.

- **look**: sets all the knobs together, then make it your own. *clean TV*, *VHS tape*, *broadcast Trinitron*, *arcade 240p*, *worn VHS*, *filmed screen*, *rolling scan band*, *noize box*, *noize wrap*, *overdriven*, *neon colorizer*, *colour space 2*, *both boxes*, *resonant bend*, *ringing circuit*, *feedback tunnel*, *pattern synth*, *lost sync*, *crt tv*, *video synth*, *fm lines*, *phosphor*, *dither*, *90s cel*, *cel on tv*, *thermal*.
- **tint**: the picture's own colours, or a screen's few: green or amber phosphor, blue, gameboy, cga, thermal, mono.
- **on the beat**: the sync, the bend, the feedback zoom and the synth colour kick with the bass. **bend on hits**: each hit shorts the circuit for a moment at a random bend point.
- **bend points**: hold one to short the circuit (*sync loss*, *roll*, *chroma short*, *feedback*, *fold*, *static*, *invert*, *freeze*). Shift-click latches one on. With the panel open, the keys 1–8 hold them too. *random bend* fires one for a moment.
- The sections open and close; a light shows the ones in use:
  - **colorizer**: *colour* and *deform* (the hues bent by the brightness), in *space 1*, *standard* or *space 2*.
  - **noize enhancer**: *gain*, *noize* (*plain*, *lines* or *wrap*: overdriven brightness wraps round) and *bright warp*.
  - **composite wire**: *composite* (how much of the picture goes through the carrier), *sharpness*, the *decoder* (notch or comb) and the *field rate* (50, 59.94 or 60 Hz: how the dot crawl moves).
  - **circuit bend**: a resonant stage on the wire that rings: *amount*, *frequency*, *Q*, *boost*, *clip low* / *high*, *feedback*, *delay*, *motion*.
  - **sync**: *V hold* (the picture rolls), *H jitter*, *H tear* (the top flags), *head switch* (the tear at the bottom), *sync pull* (bright parts pull the lines), *AFC ringing*, *wobulate* and *wob freq*, *sync warp*, *ripple*.
  - **tape**: the *format* (off, VHS, worn VHS), *grain*, *chroma noise*, *chroma delay*, *dropouts*, *tracking*.
  - **feedback**: the output patched back to the input: *amount*, *zoom*, *rotate*, *shift x* / *y*, *hue drift*, *luma key* (only where the picture is dark).
  - **oscillator**: a raster pattern generator mixed in: *mix*, *H* / *V freq*, *rate*, *colour*.
  - **RF**: *snow*, *specks*, *interference*, *ghost*, *hum bar*, *chaos*.
  - **TV set**: *colour*, *tint*, *brightness*, *contrast*, *hue drift*.
  - **tube**: *scanlines* (the screen's own, or 240p / 288p / 480 / 576 lines, each drawn by a beam that widens where it is bright), the *mask* (aperture grille, slot, shadow), *phosphor*, *bloom*, *tube curve*, *screen size*, *glass* and *camera* (as if filmed off the screen).
  - **stylise**: *pixels*, *dither*, *cel bands*, *cel ink*, *fm lines*, *synth colour*.

It works on every score mode too, and shows in recordings and the saved PNGs and stills. The **on** switch at the top turns it off and keeps every setting for later; *clean* puts every knob back to 0. Double-click or right-click a knob for 0.

## Grade look: vector scope

In the **grade** panel, *look: vector scope* turns the painting into a vector display seen through good glass:

- **The lines:** the picture's edges, traced thin and sharp at full resolution, with a hot core.
- **The light:** each line blooms at three sizes, from a tight glow to a wide soft haze, with a warm halation round the brightest parts and a little film grain. It is meant to feel nostalgic but expensive, not like an old effect.
- **Axes:** quiet hairline axes with ticks, and a few faint glowing dashes dropped from the picture's strongest points.
- **Settings:** the colour (*green*, *amber*, *cyan*, *white*, *magenta*, or *picture*, which keeps the picture's own colours in the glow), **axes** on or off, **detail** (how many edges become lines) and **blobs**.

It goes on before the signal, so a CRT look can sit on top.

## Bolts

**bolts** (one of the beat keys) makes the brush itself strike like lightning on the hits. On each hit the painter picks one of the picture's lines and runs the ticked style along it: a fast stroke that follows the edge, jumps small gaps and forks, so the bolt is painted in graffiti, gold, oil or whatever is ticked, and stays as part of the painting. Harder hits make longer, wider bolts with more forks.

## Growth

*one line → growth · ink / growth · colour* makes the picture out of one closed line that grows (differential growth), then paints it:

- **Growing:** it starts as a small loop in the picture's darkest part. Each point keeps its neighbours close and pushes every other point away, and where the line stretches a new point goes in. While it grows it shows as a steady pencil line.
- **The picture:** the line lengthens and folds like a brain coral until it fills the picture. It folds tighter where the picture is darker and leaves the near-white empty.
- **Painting:** once grown, the brush paints along the whole line in the ticked styles (graffiti, gold, oil…), in the picture's colours with *growth · colour*.
- **Video and music:** on a video the line re-forms round the picture as it plays; with music the bass makes it pulse.
- **Settings:** the stroke count sets how long it may grow and so how fine it gets; the speed slider sets how fast. **svg** saves the line.

## Real paint

**real paint** (in the style panel, beside *pigment*; on by default) paints some styles with a simulation of the paint itself instead of drawing them:

- **Watercolour** (*water*, *wet*, *wash*): Maksim Surguy's Watercolor Playground engine (MIT licence). Water and pigment flow on paper: the paint bleeds into damp paper, pools into a darker tide line as it dries, settles into the paper's grain and glazes where strokes cross. Each layer is let dry before the next, as a watercolourist waits. It is painted on white watercolour paper and lies over the other styles as a transparent glaze.
- **Oil and acrylic**: David Li's Fluid Paint (MIT licence). A brush of up to a hundred bristles, each bending against the canvas, drags wet paint that smears into the paint already there and keeps the bristles' ridges, lit as a real surface: glossy for oil, matte for acrylic.
- **Where it shows:** on the painting, in the saved pictures and in recordings. The saved code and SVG keep the drawn look, since they are code.
- **What it needs:** a graphics card with float textures (WebGL 2 for watercolour). Without it, or with real paint off, the drawn styles are used.
- **Speed:** the paint stays on the graphics card (nothing is read back), about ten times a second, less when that is costly. Without a song the painter waits for the paint when it falls behind, so the two stay in step; with a song the painter keeps time and the paint catches up. On a slow computer the paint sheets are smaller and the oil brush has fewer bristles. To make it lighter still: fewer strokes, or real paint off.

## Pigment mixing

**pigment** (in the style panel, beside *tint*) mixes the paint styles' colours as real paint does, after spectral.js (Kubelka–Munk theory, by Ronald van Wijnen, MIT licence):

- **Mixing:** blue into yellow makes green, not grey, and a colour thinned with white keeps its hue.
- **Wet pickup:** each stroke takes up a little of the wet colour already under it, more by its end, as a brush does.
- **Styles:** it applies to oil, acrylic, knife, gouache, watercolour, wet, soft, painterly and the inks. Graffiti stays as it is.

Off, colours mix as light on a screen. The difference shows most where two different colours meet or cross: with pigment on, a blue stroke over wet yellow turns green at its tail; with it off, it turns grey.

Right-click any slider in the studio to put it back to its default.

The pop-up panels (score shape, signal, colour grade, text bar) can be dragged anywhere by their title bar, and they stay inside the window. Each remembers where you put it; double-click its title bar to put it back.

## Presets and reset

The preset row under the painting keeps four sets of settings: press **store**, then a letter; press a letter to bring them back; **save** / **load** them as a file. **reset** (press it twice) puts every setting back to its default; your presets and the easy / console choice are kept.

## Replay and layering (local version)

The local version has 383 hand-coded recreations of JAS.BLACK artworks to **replay**, with live strokes mixed in (**+live**) and the code finishing on top (**finish**).

**layer ⤮** replays the pieces in a random order, each one on top of the last. It keeps one frame for the whole show:
- **frame**: the first piece's shape, or a fixed one: 5:7 (most pieces), 1:1, 4:5, 9:16, 16:9 or 7:5.
- **same shape / all shapes**: only the pieces whose own shape matches the frame, or every piece.
- **crop / fit**: a piece of another shape fills the frame (cropped), or fits inside it whole, with black bars.

Saving a picture (PNG, 4K / 8K), stills or a contact sheet during a replay with live strokes or layers saves the canvas as you see it, strokes and layers included.

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
| ![pencil](examples/pencil.webp) | ![graffiti](examples/graffiti.webp) | ![foam](examples/foam.webp) |
| pencil | graffiti | foam |
| ![acrylic](examples/acrylic.webp) | ![watercolour](examples/watercolour.webp) | ![linocut](examples/linocut.webp) |
| acrylic | watercolour | linocut |
| ![riso](examples/riso.webp) | ![bronze](examples/bronze.webp) | ![hylics](examples/hylics.webp) |
| riso | bronze | hylics |

## Tips

- A portrait or a picture with a clear subject paints best.
- **Lower the stroke count** for bold, graphic pictures; **raise it** (or use *hq*) for detail.
- To make the music obvious, turn **amount** up and pick a 3D style such as oil or gold: the beat strokes and the swinging light both show it.
- Rendering at 4K takes about four times as long as 1080p.
