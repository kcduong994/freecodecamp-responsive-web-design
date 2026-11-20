# Workshop 07 — Build a Video Display Using iframe

> **Curriculum:** [freeCodeCamp — Responsive Web Design V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/)
> **Area:** HTML → Basic HTML
> **Activity:** [Build a Video Display Using iframe](https://www.freecodecamp.org/learn/responsive-web-design-v9/workshop-build-a-video-display-using-iframe/step-1)
> **Evidence:** The learner completed the final, seven-step workshop and supplied the full HTML source.
> **Status:** Accepted in the freeCodeCamp workshop; a production-ready embedding and accessibility audit have not been performed.

## Objective / Mục tiêu

Embed a hosted video into a web page using an HTML **iframe** (*inline frame* /ˈɪn.laɪn freɪm/, khung nội tuyến). Practise the difference between referencing a video-hosting web page and linking to a raw video file. This workshop follows earlier exercises using native HTML `audio` and `video` elements.

## Files

- [`index.html`](./index.html) — the completed learner-submitted standalone HTML page.
- [`README.md`](./README.md) — learning scope, source choices and verification limits.
- [`REVIEW.md`](./REVIEW.md) — detailed technical review, IPA pronunciation, debugging and independent questions.

## Source overview

The page contains one `h1` followed by one `iframe` embedding a video from YouTube:

```html
<iframe
  width="560"
  height="315"
  src="https://www.youtube.com/embed/I0_951_MPE0"
  allow="accelerometer autoplay clipboard-write encrypted-media gyroscope web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen
>
</iframe>
```

The complete doctype, `html`, `head`, encoding, viewport metadata, title and body are kept in `index.html`. The accepted `allow` string and iframe markup have been preserved as provided; additional engineering improvements are explained in `REVIEW.md` rather than silently changed in the archive.

## Concept-to-source map

| Construct | Actual purpose |
| --- | --- |
| `<iframe>` | Embeds another HTML browsing context in this page. |
| `width="560"` / `height="315"` | Establish the iframe's specified display dimensions. They do not independently make it responsive. |
| `src="https://www.youtube.com/embed/..."` | Loads YouTube's **embed** page, not a raw MP4 file or ordinary `watch?v=` page. |
| `allow="..."` | Requests browser feature permissions for the embedded content; the browser and provider determine effective access. |
| `referrerpolicy="strict-origin-when-cross-origin"` | Controls how much referrer information is sent with cross-origin requests. |
| `allowfullscreen` | Gives the embedded content permission to request fullscreen where supported. |

## Important comparison

- Native `<video>` renders an HTML media player for an actual video resource, commonly via `<source src="...mp4" type="video/mp4">`.
- `<iframe>` embeds another web document with its own scripts, player UI, privacy behaviour and network dependencies.
- Pasting a `youtube.com/watch?v=...` URL as `<video><source>` does not supply an MP4 file. An `/embed/VIDEO_ID` URL is the appropriate structure for this exercise.
- Rendering an iframe in Preview does not establish that every remote network request, permission, cookie, fullscreen or playback scenario will work in all environments.

## Verification and boundaries

1. Open `index.html` with an internet-connected browser and inspect the embedded player.
2. Inspect the iframe attributes using Developer Tools → Elements.
3. In Network, distinguish the iframe document request from subsequent media and script requests.
4. Test playback, fullscreen and narrower viewports separately, remembering that a fixed width of 560px can overflow a small screen.
5. Optional improvement (not part of the accepted submission): add a meaningful iframe `title` for assistive technology and use semicolon-separated permission directives in `allow`.

**Evidence boundary:** completion of freeCodeCamp's guided steps demonstrates acceptance of the exercise markup. The archive has not been independently checked for keyboard accessibility, third-party cookie behaviour, responsive layout or changes in YouTube's embedding policy.

## Connections

This workshop extends [Workshop 05 — HTML Video Player](../build-an-html-video-player/) and [Lab 05 — HTML Audio and Video Player](../../labs/build-an-html-audio-and-video-player/): the earlier lessons load media resources directly, whereas this activity embeds a third-party player as an HTML document. See the [conceptual review](./REVIEW.md) and [cumulative review](../../RWD_REVIEW.md).

**Archive conventions:** no completion dates, Python tests, repository automation scripts or downloaded video assets are included in this workshop directory.
