# Workshop 04 — Build an HTML Music Player

> **Course:** [freeCodeCamp — Responsive Web Design V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/) → Basic HTML
> **Activity:** [Build an HTML Music Player](https://www.freecodecamp.org/learn/responsive-web-design-v9/workshop-html-music-player/step-1)
> **Type:** Guided workshop
> **Status:** Completed — **9/9 steps (100%)**, confirmed by the learner's final-step screenshot
> **Archive:** The learner's supplied final HTML content and structure are retained; formatting-only whitespace is normalized; this is not a claimed independent rerun.

## Objective / Mục tiêu

Build a basic HTML music player using three browser-native audio elements. The lesson demonstrates that HTML can expose playable audio through the `audio` element and its `src`, `controls`, and `loop` attributes **without custom CSS or JavaScript**. Browser controls and resource availability are separate from the HTML's syntactic correctness.

## Contents

```text
workshops/build-an-html-music-player/
├── index.html    # Learner's original 100%-accepted HTML source
├── README.md     # Scope, structure, walkthrough and checks
└── REVIEW.md     # Technical review, English IPA, debugging and questions
```

## What the completed page contains

| Item | Source evidence | Interpretation |
| --- | --- | --- |
| Full HTML document | `<!DOCTYPE html>`, `html lang="en"`, `head`, `body` | Standards-mode document; English content |
| Character encoding | `meta charset="UTF-8"` | UTF-8 declaration |
| Responsive viewport hint | `meta name="viewport" content="width=device-width, initial-scale=1.0"` | Mobile viewport setup; not a complete responsive design |
| Browser-tab title | `Working with the HTML Audio Element` | `title` in `head` |
| Visible main heading | `freeCodeCamp Tunes` | Exactly one `h1` |
| Track titles | Three `h2` headings | One heading for each audio track |
| Attribution | Three `p` paragraphs | `Artist: Quincy Larson` for each track |
| Audio players | Three `audio` elements | Each has `src`, `loop`, and `controls` |

### Track inventory (as authored)

| Track | Audio file |
| --- | --- |
| Can't Stay Down | `https://cdn.freecodecamp.org/curriculum/js-music-player/can't-stay-down.mp3` |
| Cruising for a Musing | `https://cdn.freecodecamp.org/curriculum/js-music-player/cruising-for-a-musing.mp3` |
| Scratching the Surface | `https://cdn.freecodecamp.org/curriculum/js-music-player/scratching-the-surface.mp3` |

External audio is referenced by URL; audio files are **not downloaded or redistributed** by this repository. Playback requires a compatible browser and network access to those resources.

## Document layout

```text
html (lang=en)
├── head
│   ├── meta (charset=UTF-8)
│   ├── meta (name=viewport, content=width=device-width, initial-scale=1.0)
│   └── title: Working with the HTML Audio Element
└── body
    ├── h1: freeCodeCamp Tunes
    ├── h2: Can't Stay Down
    ├── p: Artist: Quincy Larson
    ├── audio [src, loop, controls]
    ├── h2: Cruising for a Musing
    ├── p: Artist: Quincy Larson
    ├── audio [src, loop, controls]
    ├── h2: Scratching the Surface
    ├── p: Artist: Quincy Larson
    └── audio [src, loop, controls]
```

The source deliberately uses `h2`, `p`, `audio` in a repeating pattern. It does not include a playlist controller, album metadata API, coordinated play/pause logic, custom media UI, `autoplay`, or a download feature.

## Core concepts

1. **`audio`:** a standard HTML element for sound content; in this exercise the `src` attribute supplies an MP3 URL.
2. **`controls`:** a Boolean attribute asking the browser to show its built-in play/pause, seek, volume and other controls (exact controls vary by browser).
3. **`loop`:** a Boolean attribute that requests repeating the same audio resource when playback reaches its end. It does not start playback automatically.
4. **`h1`, `h2`, `p`:** page-level title, track headings and artist information remain semantic text, not arbitrary visual styling.
5. **`title` vs `h1`:** the browser-tab document title and the page's visible heading have distinct purposes.
6. **`meta viewport`:** helps set viewport sizing on mobile; no CSS breakpoints, layout rules or responsive evaluation are part of this workshop.

### Exact source fragment

```html
<h2>Can't Stay Down</h2>
<p>Artist: Quincy Larson</p>
<audio src="https://cdn.freecodecamp.org/curriculum/js-music-player/can't-stay-down.mp3" loop controls></audio>
```

The apostrophe in `can't-stay-down.mp3` is legal inside a **double-quoted** HTML attribute value. A filename extension does not independently prove codec support or remote availability. Each `<audio>` element is independent; starting a second one does not automatically pause the first.

## Local inspection / Kiểm tra cục bộ

1. Open `index.html` directly in a modern browser; no Node.js, CSS, JavaScript or server setup is required.
2. Verify the visible `h1` and exactly three pairs of track title (`h2`) and artist (`p`).
3. Check that the three browser-native audio controls appear. Try play, pause, seek and volume as available in your browser.
4. Check that each file actually loads and plays with an internet connection; repeat playback through the end to check `loop` if desired.
5. Open **Developer Tools → Network → Media** (or the appropriate filter) to inspect external HTTP requests, failures, content types and range requests when relevant.
6. Open **Developer Tools → Elements** to verify the element order and Boolean `controls`/`loop` attributes.
7. Check keyboard access and understandable headings manually; passing freeCodeCamp is not a substitute for an accessibility audit.

**Evidence boundary:** the learner's screenshot shows *Congratulations. Your code passes.* and **100%** at Step 9. This confirms the freeCodeCamp checker accepted the learner's final submission; it does **not** prove uninterrupted audio access, all browser controls, cross-browser compatibility, accessibility compliance or licensing rights to the linked audio files. The archived file is faithful to the learner's submitted elements, values and order (with insignificant whitespace normalized).

## Connections to previous activities

- **Workshop 01:** headings and paragraphs form meaningful page structure; this workshop repeats `h2` + `p` to describe each track.
- **Workshop 02:** the complete `html`/`head`/`body` skeleton and `meta charset`; now add the supplied viewport declaration.
- **Lab 02 / Lab 04:** remote `src` and `href` resources: source correctness and successful network retrieval are different.
- **Workshop 03:** native controls such as `button` do not imply application behavior; by contrast native `audio controls` delegates playback UI and behavior to the browser.

Continue with the [conceptual REVIEW](./REVIEW.md) for common mistakes, UK IPA with Vietnamese explanations and questions designed for independent answers. Update the cumulative [RWD_REVIEW](../../RWD_REVIEW.md) without removing previous lessons.

**Repository conventions:** no completion dates, Python tests, code-generation tools or helper scripts are stored with this workshop.
