# Lab 05 — Build an HTML Audio and Video Player

- **Curriculum:** [freeCodeCamp — Responsive Web Design V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/) → Basic HTML
- **Type:** Independent lab
- **Status:** Learner's original submission passed the freeCodeCamp checker (**18/18 tests, 100%**). The archived edition improves the audio resource and has **not** been resubmitted to the official checker.
- **Activity:** [Build an HTML Audio and Video Player](https://www.freecodecamp.org/learn/responsive-web-design-v9/lab-html-audio-and-video-player/build-an-html-audio-and-video-player)

## Objective

Create a browser-native video and audio page using **exactly two `section` elements**. The first section displays one video from a direct MP4 resource; the second provides a looping MP3 audio player. This lab consolidates the native media concepts introduced in the earlier HTML Music Player and HTML Video Player workshops. It requires **no JavaScript, CSS, framework, or build process**.

## Evidence: original submission versus archived edition

The learner's final freeCodeCamp screenshot displays **"Congratulations. Your code passes"** and **100% complete**. The original audio source was a relative path, `whatisthemapmethod.mp3`, while the browser Preview showed a `0:00 / 0:00` player. That is evidence of **no successfully loaded media duration at the time of the screenshot**, not definitive proof of why the resource failed to load.

The archived `index.html` preserves the page heading, two sections, the first section's video title, and the valid MP4 source. It replaces the unprovided local MP3 with the **officially suggested remote audio URL** and changes the song heading to match that track:

- **Original:** `h2` "Can you see it?" plus `src="whatisthemapmethod.mp3"`.
- **Archived:** `h2` "Sailing Away" plus `src="https://cdn.freecodecamp.org/curriculum/js-music-player/sailing-away.mp3"`.
- **Verification boundary:** the 18/18 result applies to the learner's original submission; the revised source has been checked for its stated structural requirements but has **not** been re-tested on freeCodeCamp or across real browsers.

## Document structure

```text
html[lang=en]
├── head
│   ├── meta[charset=UTF-8]
│   ├── meta[name=viewport]
│   └── title
└── body
    ├── h1 — The Map Method
    ├── section (video)
    │   ├── h2 — Method Video
    │   └── video[width=640][controls]
    │       └── source[src=...mp4][type=video/mp4]
    └── section (audio)
        ├── h2 — Sailing Away
        └── audio[src=...mp3][controls][loop]
```

## Acceptance criteria (18 checks, grouped)

| Test numbers | Requirement | Archived edition |
| --- | --- | --- |
| 1–3 | One nonempty `h1` | One main heading |
| 4 | Exactly two `section` elements | Video section and audio section |
| 5–6 | First section has `h2`, then `video` | Correct order |
| 7–8 | `video` has `controls`, `width="640"` | Both present |
| 9–12 | Video contains `source` with a real video-file URL and matching MIME type | Direct `.mp4` URL, `type="video/mp4"` |
| 13–15 | Second section has nonempty `h2`, then `audio` | Correct order |
| 16–18 | `audio` has `controls`, `loop`, and an audio-file URL | All present, official `.mp3` URL |

## Why the earlier YouTube URL did not work

The learner first tried a YouTube `watch?v=...` page as the `source` URL and specified `video/mp4`. A YouTube **watch page** is not a directly downloadable MP4 media resource; the HTML `video` element cannot use that watch-page URL as a video source. YouTube embeds instead generally use a compatible `iframe` URL, but an `iframe` would **not** satisfy this lab's explicit `video > source` contract.

In the subsequent attempt the video markup was corrected and the MP4 example source succeeded. The same core lesson applies to audio: a syntactically present `src` is not proof that its file exists or is reachable.

## View and manual verification

1. Open [`index.html`](./index.html) in a browser with an internet connection.
2. Verify that the first player displays playback controls and can begin the Map Method video.
3. Verify that the second player loads a nonzero duration, can be played and restarted, and repeats when playback reaches the end.
4. Inspect **Developer Tools → Elements** to verify the nested order: `section > h2 + video > source` and `section > h2 + audio`.
5. Inspect **Developer Tools → Network** for failed media requests, HTTP status codes, MIME information and possible CORS or browser codec restrictions.
6. Try keyboard navigation and test at a narrow browser width. `width="640"` is a fixed intrinsic width, **not** a mobile-responsive guarantee.

**External media used by the archive:**

- Video (MP4): https://cdn.freecodecamp.org/curriculum/labs/what-is-the-map-method-and-how-does-it-work.mp4
- Audio (MP3): https://cdn.freecodecamp.org/curriculum/js-music-player/sailing-away.mp3

These links are media resources, **not** downloaded or committed assets. Their future availability cannot be guaranteed. Native controls may have different appearances across browsers and devices.

## What this lab teaches

- Semantic division into two independently titled `section` elements.
- Distinction between the media **container** (`video`), nested **alternative resource declaration** (`source`) and standalone `audio src`.
- The need for a direct resource URL and accurate MIME type (`video/mp4`).
- Boolean HTML attributes (`controls`, `loop`): their presence enables behavior; they do not require `="true"`.
- The difference between **code-check acceptance**, **resource loading**, **successful decoding** and **accessible user experience**.
- Why an MP3 URL can be present and pass an automated test even when playback fails.

See [REVIEW.md](./REVIEW.md) for technical explanations, bilingual terminology with IPA, debugging cases and independent review questions.

## Scope and repository conventions

- The lab practices native HTML media, not custom playlists, JavaScript event handling or multimedia editing.
- No completion date, Python tests, repository-maintenance scripts or binary MP3/MP4 assets are stored.
- The official 18/18 result is **evidence of the learner's original code**, not certification of the revised archive's runtime playback, responsiveness or accessibility.
