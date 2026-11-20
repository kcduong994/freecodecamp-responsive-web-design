# Lab 06 — Build a Video Compilation Page

- **Curriculum:** [freeCodeCamp — Responsive Web Design V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/) → Basic HTML
- **Type:** Independent lab
- **Status:** The learner's curriculum screenshot displays the completed checkmark. The exact passing HTML was **not supplied**, so this archived edition is a newly reconstructed example based on all 20 user stories. It has **not** been independently submitted to freeCodeCamp.
- **Activity:** [Build a Video Compilation Page](https://www.freecodecamp.org/learn/responsive-web-design-v9/lab-video-compilation-page/build-a-video-compilation-page)

## Objective

Build an HTML-only video collection with a single `main` landmark containing one `h1`, one introduction paragraph and **exactly three** thematic `section` elements. In each section, the first three direct children are `h2`, `p` and `iframe`, in that order. Each iframe embeds a video and has `src`, `title`, `width` and `height` attributes.

This task builds upon the iframe workshop, with greater emphasis on the **document tree**, order of direct children, accessible iframe titles and consistent embedded resources.

## Source provenance and verification boundary

The learning-platform screenshot shows the lab marked complete, but does **not** disclose the user's original code or all individual test results. This repository's `index.html` is therefore an **illustrative reconstruction**, not a verbatim archive of the passing submission. It follows the 20 published structural requirements and uses known YouTube `/embed/` URLs, but has not been re-run through the official checker or verified to play in every browser.

## Document tree

```text
html[lang=en]
├── head
│   ├── meta[charset=UTF-8]
│   ├── meta[name=viewport]
│   ├── meta[name=description]
│   └── title
└── body
    └── main                       ← only direct body child
        ├── h1                     ← single page title
        ├── p                      ← topic introduction
        ├── section
        │   ├── h2                 ← video title
        │   ├── p                  ← video introduction
        │   └── iframe             ← embedded HTML lesson
        ├── section
        │   ├── h2
        │   ├── p
        │   └── iframe             ← embedded iframe lesson
        └── section
            ├── h2
            ├── p
            └── iframe             ← embedded JavaScript lesson
```

## Acceptance criteria: 20 checks grouped

| Checks | Requirement | Reconstructed source |
| --- | --- | --- |
| 1–2 | A `main` element is the sole direct child of `body` | Present |
| 3–4 | An `h1` and a following introductory `p` within `main` | Present |
| 5 | Exactly three `section` elements after the introduction | Present |
| 6–8 | Every section directly contains `h2`, then `p`, then `iframe` | Present |
| 9–12 | First iframe contains a video URL, `title`, `height`, `width` | All present |
| 13–16 | Second iframe contains a video URL, `title`, `height`, `width` | All present |
| 17–20 | Third iframe contains a video URL, `title`, `height`, `width` | All present |

This is a **source-level checklist**, not a claim of a new official 20/20 checker run.

## External video resources

The embedded videos are freeCodeCamp educational material, and are referenced rather than downloaded into the Git repository:

1. [HTML Full Course — Build a Website Tutorial](https://www.youtube.com/watch?v=pQN-pnXPaVg)
2. [How do you embed videos onto your page using the iframe element?](https://www.youtube.com/watch?v=I0_951_MPE0)
3. [Learn JavaScript — Full Course for Beginners](https://www.youtube.com/watch?v=PkZNo7MFNFg)

The source uses the `/embed/VIDEO_ID` forms of these links. Loading and playback can be affected by provider permissions, network restrictions, privacy settings or browser policy. A syntactically valid iframe does not guarantee successful playback.

## Manual verification

1. Open [`index.html`](./index.html) in a browser connected to the internet.
2. In **Developer Tools → Elements**, verify that `body` has only one element child, `main`.
3. Verify that there are three sibling `section` elements, each with direct children `h2`, `p`, `iframe` in that order.
4. Inspect all three iframe `src`, `title`, `width` and `height` attributes.
5. Use **Network** and the browser console if a third-party player refuses to load.
6. Test keyboard focus, iframe accessible names and narrow-screen overflow. Fixed iframe dimensions do not themselves create a responsive page.
7. Optionally paste the reconstructed source into the official freeCodeCamp challenge and run the checker, recording the resulting evidence separately.

## Learning connections

- **Workshop 07:** a single YouTube iframe demonstrates the basic embed contract; this lab combines three distinct embedded lessons in semantic sections.
- **Lab 05:** native `<video>` needs direct media files, whereas `iframe` loads a third-party video player page.
- **Workshop 02:** `main`, `section`, `h1`, `h2`, and `p` express structure and reading hierarchy.
- **Accessibility extension:** an iframe `title` describes the embedded content to assistive technologies; deeper accessibility testing remains outstanding.

The companion [REVIEW.md](./REVIEW.md) contains terminology, failure modes, British English IPA, and unanswered review questions.
