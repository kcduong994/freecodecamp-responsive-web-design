# Workshop 07 — Conceptual Review / Ôn tập kiến thức

**Activity:** Build a Video Display Using iframe · freeCodeCamp Responsive Web Design V9
**Evidence:** The learner completed the guided seven-step activity and supplied the final accepted HTML.
**Source:** [index.html](./index.html) — archived submission, not a redesigned project.
**Scope:** Iframes, nested browsing contexts, embedding URLs, permissions, referrer policies and fullscreen. Accessibility and responsiveness are discussed as extensions.

## 1. `iframe` is an embedded document, not a video file

**Iframe — inline frame** /ˈɪn.laɪn freɪm/ (khung nội tuyến) embeds a separate browsing context in an HTML page. The outer page controls its placement and selected permissions; YouTube supplies the embedded document, scripts and media-player interface.

```text
Outer HTML page
├── h1: iframe Video Display
└── iframe: 560 × 315
    └── Remote YouTube embed document
        └── YouTube-provided video player
```

Contrast this with the previous native video workshop:

```html
<video controls width="640">
  <source src="movie.mp4" type="video/mp4">
</video>
```

A `source` inside a `video` element identifies a media resource; an iframe `src` identifies a web document. A YouTube `watch` URL is not an MP4 media file, and a successful embedded player does not mean the outer HTML directly decodes the video.

## 2. Core markup and attribute meanings

| Attribute | Submitted value | Role |
| --- | --- | --- |
| `width` | `560` | Width of the iframe viewport in CSS pixels in this HTML context. |
| `height` | `315` | Height of the iframe viewport. |
| `src` | `https://www.youtube.com/embed/I0_951_MPE0` | Third-party player-document URL. |
| `allow` | `accelerometer autoplay clipboard-write encrypted-media gyroscope web-share` | Submitted feature-permission string. |
| `referrerpolicy` | `strict-origin-when-cross-origin` | Browser referrer-disclosure policy for the frame load. |
| `allowfullscreen` | Present, without a value | Boolean attribute permitting the frame to request fullscreen, subject to browser/provider constraints. |

The intended 560:315 ratio simplifies to 16:9. These fixed dimensions can overflow a narrow phone viewport. The `<meta name="viewport">` declaration in the document does not itself solve that problem.

## 3. The correct YouTube URL shape

```text
Watch page:  https://www.youtube.com/watch?v=I0_951_MPE0
Embed page:  https://www.youtube.com/embed/I0_951_MPE0
Raw file:    https://example.org/video.mp4
```

- The **watch page** is YouTube's ordinary viewing page, not generally the correct iframe embed URL.
- The **embed page** is the URL requested by this workshop's iframe. Use the embed form for the player.
- A **raw video file** is what a native `video` element can load as a media source.

**Cross-origin** /ˌkrɒs ˈɒr.ɪ.dʒɪn/ means that the embedded document comes from a different origin (scheme, host or port) than the parent page. The browser isolates documents according to origin-related security rules. Do not presume the parent page can directly inspect or manipulate YouTube's internal DOM.

## 4. Permissions and `allow`

`allow` is a permissions-policy declaration for the iframe. It does not force autoplay or switch on the camera/microphone; it defines which features may be available under the browser's and embedded site's rules.

**Engineering note:** the archived source preserves the exact learner-supplied value; for a new production implementation, separate individual feature directives with semicolons, for example:

```html
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; web-share"
```

The exercise's source and the improved alternative are intentionally distinguished. For real deployments, request only the permissions actually needed and verify support in target browsers.

## 5. Referrer policy and privacy

`referrerpolicy="strict-origin-when-cross-origin"` controls the `Referer` request header:

- **Same-origin request:** normally permits the full referrer URL.
- **Cross-origin request with comparable secure scheme:** normally sends just the origin, not the full path or query.
- **Secure-to-insecure downgrade:** does not send the referrer.

This is not an anti-tracking switch and does not disable third-party cookies, scripts or YouTube's network traffic. A policy string must be spelled exactly; the HTML attribute uses `referrerpolicy`, not `refererpolicy`.

## 6. `allowfullscreen`, accessibility and responsiveness

The Boolean attribute `allowfullscreen` gives the embedded player an opportunity to enter fullscreen when the browser and provider allow it. The fullscreen feature still requires browser support and often user action.

**Accessibility extension:** a meaningful `title` such as `title="Tutorial video about embedding videos"` helps assistive technologies identify the frame. The originally accepted code did not include an iframe title, so accessibility is not claimed as fully satisfied.

**Responsive extension:** use CSS such as `max-width`, `aspect-ratio`, and proportional widths around the iframe, or a responsive wrapper, while avoiding arbitrary stretching. None of that CSS was part of the accepted seven-step workshop.

**Privacy extension:** consider whether the third-party player can load cookies and how to give users suitable notice. This is separate from the course test requirements.

## 7. Debugging matrix

| Symptom | Investigation |
| --- | --- |
| Blank frame | Inspect the iframe `src` and browser network error. |
| YouTube watch page instead of embedded player | Confirm the `/embed/VIDEO_ID` path. |
| Embedded video refuses playback | Check provider embed restrictions, browser policy, cookies and console messages. |
| Autoplay does not begin | Verify browser autoplay restrictions; `allow` alone does not force autoplay. |
| Fullscreen option fails | Check `allowfullscreen`, iframe permissions and browser/provider support. |
| Frame spills off a phone screen | Inspect fixed `width` and viewport dimensions. |
| Accessibility checker flags the frame | Consider a descriptive `title` and keyboard operation. |
| A copied media URL fails in `<video>` | Check whether the URL points to a real media file, not an HTML watch page. |

## 8. Technical vocabulary with British English IPA

| English | IPA | Tiếng Việt |
| --- | --- | --- |
| Inline frame | /ˈɪn.laɪn freɪm/ | Khung nội tuyến |
| Embed | /ɪmˈbed/ | Nhúng nội dung |
| Browsing context | /ˈbraʊ.zɪŋ ˈkɒn.tekst/ | Ngữ cảnh duyệt web |
| Frame | /freɪm/ | Khung |
| Viewport | /ˈvjuː.pɔːt/ | Vùng hiển thị |
| Attribute | /ˈæt.rɪ.bjuːt/ | Thuộc tính |
| Referrer | /rɪˈfɜː.rə/ | Nguồn giới thiệu/yêu cầu |
| Policy | /ˈpɒl.ə.si/ | Chính sách |
| Permission | /pəˈmɪʃ.ən/ | Quyền cho phép |
| Fullscreen | /ˈfʊl.skriːn/ | Toàn màn hình |
| Cross-origin | /ˌkrɒs ˈɒr.ɪ.dʒɪn/ | Khác nguồn gốc |
| Autoplay | /ˈɔː.təʊ.pleɪ/ | Tự động phát |
| Clipboard | /ˈklɪp.bɔːd/ | Bảng nhớ tạm |
| Responsive | /rɪˈspɒn.sɪv/ | Thích ứng kích thước màn hình |
| Accessibility | /əkˌses.əˈbɪl.ə.ti/ | Khả năng tiếp cận |
| Privacy | /ˈprɪv.ə.si/ | Quyền riêng tư |

## 9. Self-assessment — answer independently

### Remember and understand

1. What does `iframe` stand for and what does it embed?
2. How does `<iframe src="...">` differ from `<video><source src="..."></video>`?
3. What role do the 560px width and 315px height play?
4. Why is a YouTube `/embed/` URL used rather than `/watch?v=`?
5. What does the `allowfullscreen` Boolean attribute permit?
6. Does `allow="autoplay"` guarantee that a video starts without user interaction? Why?
7. Which HTML element creates the visible page heading in the final source?

### Apply and debug

8. A player is blank in an iframe. What would you inspect in Network and Console?
9. A video file works in a `video` element but not as a YouTube embed. What distinction might explain this?
10. What would happen if `height` were set to 100 while width remained 560?
11. How would you make a 16:9 iframe responsive without changing its internal YouTube player code?
12. Why is `referrerpolicy` not equivalent to blocking cookies or scripts?
13. Why should individual permission-policy directives generally use semicolon separators?
14. Propose a meaningful iframe title for an engineering training video.

### Analyze and extend

15. Compare the browser's responsibility for media decoding in a native `video` element with the third-party iframe case.
16. Which parts of a remote YouTube document are normally unavailable for direct manipulation from the parent page due to cross-origin restrictions?
17. How would you test keyboard access and fullscreen with and without a mouse?
18. Explain why the exercise's acceptance result does not prove responsiveness or full accessibility.
19. In a coastal engineering dashboard, when would you prefer to embed a demonstration video versus hosting direct MP4 media?
20. Which privacy or availability trade-offs arise when relying on a third-party host for an important scientific communication resource?

## 10. Maintenance

Keep this completed source distinct from proposed enhancements. New CSS, additional media sources, an improved `allow` value and an accessibility title are **extensions**, not changes to the learner's accepted submission. Do not add completion dates, Python test files, local update scripts or downloaded media to this workshop's archived three-file directory.
