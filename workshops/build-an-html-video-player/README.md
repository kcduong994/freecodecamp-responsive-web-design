# Workshop 05 — Build an HTML Video Player

> **Course:** [freeCodeCamp — Responsive Web Design V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/) → Basic HTML
> **Activity:** [Build an HTML Video Player](https://www.freecodecamp.org/learn/responsive-web-design-v9/workshop-html-video-player/step-1)
> **Type:** Guided HTML workshop
> **Status:** Completed — **13/13 steps (100%)** in the learner's freeCodeCamp final screenshot
> **Implementation:** HTML only; no authored CSS, JavaScript, backend or bundled video files

## Objective / Mục tiêu

Build a browser-native video player using HTML's `<video>` element. Learn how media attributes work, how the browser selects a supported `<source>`, and why an exercise's green checks do not automatically establish network availability or cross-browser playback. This workshop extends [Workshop 04 — HTML Music Player](../build-an-html-music-player/).

## Contents

- [index.html](./index.html) — the complete HTML5 document, reconstructed from the provided final fragment and the lesson's visible boilerplate; authored media values and order preserved.
- [REVIEW.md](./REVIEW.md) — concept-by-concept explanation, troubleshooting, British English pronunciation with Vietnamese meaning and **30 independent questions**.
- [Cumulative review](../../RWD_REVIEW.md) — cross-workshop comparison of HTML media, resource selection and validation.

## What the completed page contains

| Feature | Completed source | Why it matters |
| --- | --- | --- |
| Document skeleton | `<!DOCTYPE html>`, `html lang="en"`, `head`, `body` | Standard HTML5 document and language metadata |
| Metadata | UTF-8 and mobile viewport declaration | Text encoding and mobile viewport configuration |
| Browser tab title | `Working with the HTML Video Element` | Identifies the document in the tab/bookmark |
| Main heading | `h1` with the same title | Gives the visible page a primary heading |
| Player | One `<video>` element | Browser-native media playback |
| Display width | `width="640"` | Nominal video display width in CSS pixels; responsive resizing is not implemented |
| Controls | `controls` | Native play/pause, timeline, volume and other browser-dependent options |
| Repetition | `loop` | Replays the current video when it reaches the end |
| Initial audio state | `muted` | Video starts muted; users may unmute with controls |
| Pre-play image | `poster=".../past-event2.jpg"` | Placeholder image before playback, where supported |
| Alternative sources | Four `<source>` elements | Gives the browser candidate resources and MIME hints |

### Sources exactly as supplied

| Position | Source file | Declared MIME type |
| ---: | --- | --- |
| 1 | `what-is-the-map-method-and-how-does-it-work.mp4` | `video/mp4` |
| 2 | `mapmethod.webm` | `video/webm` |
| 3 | `mapmethod.ogg` | `video/ogg` |
| 4 | `mapmethod.mov` | `video/quicktime` |

All four resources and the poster use absolute HTTPS URLs under `https://cdn.freecodecamp.org/curriculum/labs/`. **No media file is copied into this repository.** Exact URL strings and source order are preserved from the learner's submitted final fragment.

## Document layout

```text
html lang="en"
├── head
│   ├── meta charset="UTF-8"
│   ├── meta name="viewport"
│   └── title
└── body
    ├── h1
    └── video [width, loop, controls, muted, poster]
        ├── source [MP4, video/mp4]
        ├── source [WebM, video/webm]
        ├── source [Ogg, video/ogg]
        └── source [MOV, video/quicktime]
```

`<source>` is a **void element** (no `</source>`); `<video>` is not void and **must** be closed with `</video>`. The `type` attribute is a hint; actual playback also depends on browser codec support and network responses.

## Core concepts / Các khái niệm chính

1. **Native player:** The browser supplies the UI when `controls` is present; the workshop does not implement custom playback buttons.
2. **Boolean attributes:** Presence of `loop`, `controls`, and `muted` requests their behavior. Writing `muted="false"` would not reliably turn muting off; omission is the HTML way to leave it false.
3. **Source candidates:** The browser may try alternative source candidates compatible with its supported formats/codecs. Four source tags do not mean four simultaneous video players.
4. **Poster:** A still image is shown while no video frame is available (normally before playback). It is not a substitute for a valid media source.
5. **Width and responsive behavior:** `width="640"` alone does not make the player mobile-responsive; later CSS can adjust max-width/layout.
6. **Video without autoplay:** `loop` and `muted` do **not** mean playback starts automatically. `autoplay` is not present.
7. **Audio vs video:** The prior music workshop used three independent `<audio src="...">` elements; this video workshop uses one `<video>` with four child `<source>` candidates.

## Local inspection / Kiểm tra cục bộ

1. Open [index.html](./index.html) directly in a modern browser (no server required for the HTML file).
2. Verify one `h1`, one native video player, its visible controls and the poster image before playback, if the browser presents it.
3. Attempt play, pause, seek, mute/unmute and replay after the end. Results depend on the browser and available remote files; **not independently verified here**.
4. Open **Developer Tools → Elements** to inspect the DOM, `video` attributes and four nested sources.
5. Open **Developer Tools → Network** (Media filter if supported) to see the selected video request, HTTP status, response `Content-Type`, and loading errors. The browser need not request all four files.
6. Inspect **Console** for resource and media errors. Verify keyboard operation and accessible name/context manually.
7. Resize the browser: a fixed 640-pixel width may overflow a narrow viewport; responsive CSS is outside the completed workshop.

## Validation boundaries / Giới hạn bằng chứng

- **Confirmed:** the screenshot from freeCodeCamp shows **"Congratulations. Your code passes."** and **100%** at **Step 13**.
- **Provided:** the learner pasted the complete `<h1>` and `<video>` content through `</html>`, but the paste omitted its opening `<!DOCTYPE html>`, `<html>`, `<head>`, title/metadata and `<body>` lines. Those are reconstructed from the prior lesson screenshot and its known HTML5 scaffold, not invented application features.
- **Not independently established:** all remote videos being available at present, media playback on every browser, codec compatibility of each file, universal keyboard accessibility, or any licensing rights to redistribute media binaries.
- **Source policy:** the archive reproduces the completed learning structure; no extra JavaScript player, CSS skin, video download, test script or application claims are added.

## Connections to earlier activities

- **Workshop 01:** the visible `h1` communicates the page's primary heading, separate from the document `<title>`.
- **Workshop 02 / Lab 03:** valid `head` and `body` structure, UTF-8, viewport and document nesting.
- **Lab 02 / Lab 04:** a correct URL and a passing source check do not guarantee that a remote resource loads.
- **Workshop 03:** a generic `<button>` needs application logic for business behavior; `video controls` are browser-provided UI.
- **Workshop 04:** compare separate MP3 `<audio>` players with a single `<video>` whose nested `<source>` elements provide alternatives.

Continue with [REVIEW.md](./REVIEW.md) for explanations, debugging scenarios, IPA and self-assessment.

**Repository convention:** no completion dates, Python test files, auxiliary updater scripts or downloaded media assets.
