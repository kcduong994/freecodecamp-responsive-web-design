# Workshop 04 — Conceptual Review / Ôn tập kiến thức

**Activity:** Build an HTML Music Player · freeCodeCamp Responsive Web Design V9
**Evidence:** Learner's final Step 9 screenshot confirms **9/9 (100%)**
**Source:** [index.html](./index.html), supplied by the learner after passing
**Learning rule:** Source-grounded statements are separated from optional extensions. Answer the exercises independently; no answer key is provided.

## 1. Read the final source before generalizing

The archived document has one `h1` (`freeCodeCamp Tunes`) and exactly three tracks. Each track uses an `h2` heading, a `p` paragraph containing the artist's name, and one `audio` element that has `src`, `loop` and `controls`.

```html
<h2>Cruising for a Musing</h2>
<p>Artist: Quincy Larson</p>
<audio src="https://cdn.freecodecamp.org/curriculum/js-music-player/cruising-for-a-musing.mp3" loop controls></audio>
```

| Track number | Heading (`h2`) | Artist (`p`) | Source file |
| ---: | --- | --- | --- |
| 1 | Can't Stay Down | Quincy Larson | `can't-stay-down.mp3` |
| 2 | Cruising for a Musing | Quincy Larson | `cruising-for-a-musing.mp3` |
| 3 | Scratching the Surface | Quincy Larson | `scratching-the-surface.mp3` |

**Do not invent extra features:** the page has no custom styling, no JavaScript, no playlist coordination, no playlist navigation, no download code and no custom playback application logic.

## 2. Anatomy of an HTML audio element

```html
<audio src="https://example.org/example.mp3" controls loop></audio>
```

| Construct | What it means | What it does not mean |
| --- | --- | --- |
| `audio` element | Embeds sound playback in an HTML document | Does not guarantee the sound resource exists |
| `src` attribute | Identifies the audio resource URL | Does not imply a successful HTTP response |
| `controls` | Boolean attribute requesting built-in browser UI | Does not provide one universal appearance across browsers |
| `loop` | Boolean attribute requesting repeat when playback ends | Does **not** mean `autoplay` |
| `</audio>` | Closes the `audio` element | `audio` is **not** a void element |

HTML Boolean attributes generally represent *true when present*. `controls`, `controls=""` and `controls="controls"` are equivalent in HTML. Adding `controls="false"` would **not** disable controls: presence is still true. To remove the Boolean state, remove the attribute itself.

The source's `loop controls` ordering is valid; attribute order does not change the intended behavior. Source text is declared using double quotes, so the apostrophe in `can't-stay-down.mp3` does not end the attribute value.

## 3. Controls vs looping vs autoplay

- **Controls:** the browser decides which native controls to show (often play/pause, timeline, volume; variations exist). The `controls` attribute permits interaction; it does not start playback.
- **Looping:** after a track reaches the end, the player attempts to start it again. It repeats that individual media element's resource, not automatically the next `h2` track.
- **Autoplay — extension, not in this source:** `autoplay` requests starting without user action. Browsers may block autoplay with sound. Do not treat `loop` as a workaround.
- **Preload — extension:** `preload="none"`, `metadata` or `auto` are hints about loading behavior, not guarantees. The final learner code does not set `preload`.

**Important behavior:** because the page has three separate native `audio` elements, playing two simultaneously is possible. There is no JavaScript that pauses the previously active player. Hence this is a multi-player page rather than a coordinated one-track-at-a-time playlist.

## 4. MP3, URL resolution and browser media loading

`src` in the source is an **absolute HTTPS URL**. A browser contacts the referenced CDN when appropriate. Availability depends on network conditions, server status, allowed requests and media support. A path ending in `.mp3` is a useful hint about format, not proof that the remote bytes are playable MP3 content.

To diagnose a player with visible controls but no sound:

1. Inspect the exact `src` spelling and whether quotation marks are correctly closed.
2. Check that the browser can reach the remote resource (Network panel, HTTP status, redirects, type and request details).
3. Distinguish unsupported audio formats/decoding from missing resources and from silent/muted audio.
4. Check the player's mute/volume, the system sound device and the browser's permissions.
5. Remember that an accepted exercise tests HTML structure/requirements; it may not test media delivery on every device.

**Extension — multiple sources and fallback:** A production page may place several `<source>` elements inside `<audio>` and include fallback text. This workshop does **not** use that pattern. Choosing between sources can improve support for differing media formats but must be tested in real target browsers.

```html
<!-- Extension only; NOT part of the completed workshop source. -->
<audio controls>
  <source src="sample.ogg" type="audio/ogg">
  <source src="sample.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
```

## 5. Document metadata and semantic headings

The completed `head` contains:

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Working with the HTML Audio Element</title>
```

- **Character encoding** (`charset`) allows correct interpretation of Unicode text.
- **Viewport metadata** gives mobile browsers a basis for device-width rendering and initial zoom. It does not generate CSS, a grid or responsive breakpoints.
- **Title** labels the *document* (commonly shown in the browser tab). The visible `h1` labels the *page content*. They need not contain identical text.
- **Heading hierarchy:** one `h1` introduces the page; three sibling `h2` headings identify tracks. Do not substitute `h2` with a styled `p` merely because of font size.
- **Language:** `html lang="en"` declares the document's primary language. It is not a substitute for UTF-8.

**Extension:** production content could be grouped with semantic `section` or `article` where appropriate, but these containers are **not** present in the learner's source and are not prerequisites for this exercise.

## 6. Accessibility: native media UI and its limits

Native audio controls are generally preferable to a fake play button made from plain text because browsers provide built-in interaction behavior. However, control appearance, keyboard support and labels can differ across browser/platform combinations, so manual checks remain necessary.

The nearby heading names each track, but that is not the same as a programmatically associated accessible name for every possible user agent. For a full application, test with a screen reader and keyboard, consider transcripts for spoken media when appropriate, and ensure any added custom controls have clear labels and states.

**Content note:** an `alt` attribute applies to images, not to `<audio>`. Do not transplant the image pattern from Lab 04 to audio. Captions for synchronized video/audio use different strategies and should be studied in context.

## 7. Fault diagnosis — lỗi thường gặp

| Symptom / Test issue | Likely cause | Action |
| --- | --- | --- |
| One audio player absent | `audio` missing or malformed | Inspect source and parsed DOM |
| Native player is missing controls | `controls` attribute absent | Add `controls`; inspect result |
| Track repeats unexpectedly | `loop` is present | Remove `loop` when repeat is not desired |
| Track never starts automatically | No user start and no permitted autoplay | `loop` does not imply autoplay; initiate playback manually |
| Controls visible, no audio plays | Resource missing, unsupported, muted or network failure | Inspect Network and audio/system output |
| Text `Artist:` rendered in wrong position | Misordered `h2`, `p`, `audio` | Compare with source pattern |
| Browser tab shows a different title than the page | `title` differs from `h1` | This is legitimate; each serves a different purpose |
| Filename apostrophe appears suspicious | Apostrophe inside double-quoted attribute | Valid HTML; do not break the attribute quoting |
| Several tracks play together | Each player is independent | No coordinated playback logic in source |
| Passes workshop checks but cannot be used offline | Sources reference remote MP3s | Offline resources were never archived |

## 8. Conceptual comparisons with past completed work

| Earlier activity | Relevant knowledge | New contrast in Workshop 04 |
| --- | --- | --- |
| Workshop 01: Curriculum Outline | `h1`, `h2`, `p` semantics | A repeated track-specific heading/artist pattern |
| Lab 02: Pet Adoption | `src` on `img` | `src` can also identify an audio resource |
| Workshop 02: Cat Photo App | HTML skeleton, `meta charset`, external assets | Adds viewport metadata from supplied boilerplate |
| Workshop 03: Bookstore | `button` without JavaScript does not implement a cart | `audio controls` supplies built-in real playback controls |
| Lab 04: Travel Agency | Images can pass a source test while failing to load | Media resource delivery needs separate Network verification |

## 9. Vocabulary and pronunciation — Từ vựng và cách đọc (British English IPA)

| English | IPA (UK) | Tiếng Việt / usage |
| --- | --- | --- |
| Music player | /ˈmjuː.zɪk ˈpleɪ.ə/ | Trình phát nhạc |
| Audio | /ˈɔː.di.əʊ/ | Âm thanh; phần tử `audio` |
| Track | /træk/ | Bản nhạc / track |
| Artist | /ˈɑː.tɪst/ | Nghệ sĩ, người biểu diễn |
| Playback | /ˈpleɪ.bæk/ | Quá trình phát nội dung |
| Control | /kənˈtrəʊl/ | Điều khiển; `controls` |
| Loop | /luːp/ | Lặp lại; `loop` |
| Autoplay | /ˈɔː.təʊ.pleɪ/ | Tự phát; không dùng trong bài |
| Source | /sɔːs/ | Nguồn tài nguyên; `src` |
| Browser | /ˈbraʊ.zə/ | Trình duyệt |
| Media | /ˈmiː.di.ə/ | Đa phương tiện |
| Attribute | /ˈæt.rɪ.bjuːt/ | Thuộc tính HTML |
| Boolean | /ˈbuː.li.ən/ | Giá trị logic; thuộc tính Boolean |
| Viewport | /ˈvjuː.pɔːt/ | Vùng hiển thị |
| Metadata | /ˈmet.əˌdeɪ.tə/ | Siêu dữ liệu |
| Encoding | /ɪnˈkəʊ.dɪŋ/ | Mã hóa ký tự |
| Accessibility | /əkˌses.əˈbɪl.ə.ti/ | Khả năng tiếp cận |
| Network request | /ˈnet.wɜːk rɪˈkwest/ | Yêu cầu mạng |
| Volume | /ˈvɒl.juːm/ | Âm lượng |
| Playlist | /ˈpleɪ.lɪst/ | Danh sách phát; chưa có logic playlist |

IPA is an aid to reading English technical documentation; actual accents vary. For practice, say the term, explain it in Vietnamese, then identify the exact related HTML construct.

## 10. Independent questions — Câu hỏi tự ôn tập (không kèm đáp án)

### A. Recall and explain / Nhớ và giải thích

1. What is the primary purpose of the HTML `audio` element?
2. What are the three track titles in the actual completed file, in source order?
3. How many `h1`, `h2`, `p`, and `audio` elements are present, respectively?
4. Explain the difference between `src` and `href` using a media element and an anchor as examples.
5. What is the role of `controls`? Does it automatically start playback?
6. What is the role of `loop`? Does it automatically play the *next* song?
7. Why is `audio` different from the void element `img`?
8. Why can `title` and `h1` have different text without causing an HTML error?

### B. Apply and debug / Vận dụng và sửa lỗi

9. Write the complete `audio` element for `https://example.org/sample.mp3` with controls and repeat.
10. Why does `controls="false"` **not** turn off the controls in ordinary HTML markup?
11. Is `<audio src="sample.mp3" controls loop>` a complete properly closed normal audio element? Explain.
12. A student writes `<audio href="song.mp3" controls></audio>`. What should they change and why?
13. A student writes `src='can't-stay-down.mp3'`. What can go wrong with the single-quote delimiters?
14. The player UI appears, but the media will not load. What would you inspect in DevTools before editing HTML?
15. A student uses `<h3>` for the only page heading and `<h1>` for each track. How would you revise the hierarchy?
16. Two tracks play at once. Is that necessarily a syntax error? Identify the actual cause.

### C. Analyze, evaluate and extend / Phân tích, đánh giá, mở rộng

17. What does the success screenshot prove? What does it **not** prove about network delivery or accessibility?
18. Compare `loop`, `controls`, `autoplay` and `preload`. Which are present in the learner's source?
19. What is the difference between a browser-native audio UI and a fake `<button>` labelled Play with no event handler?
20. Why does an HTTPS MP3 URL require online availability even if the `index.html` is opened locally?
21. Explain why the mobile viewport meta element alone does not make this page fully responsive.
22. How would you check whether a track description and the associated player are clear to a keyboard-only user?
23. What checks are needed before replacing the MP3 URLs with audio distributed from your own hosting?
24. **Extension:** how might a single-play-at-a-time playlist behave differently from these three independent native players?
25. **Extension:** propose a structure for labeling audio content in a scientific coastal monitoring webpage (e.g., wave buoy acoustic recordings), and distinguish source metadata from visible headings.
26. **Extension:** compare a failure from an unsupported media codec with a 404 response. What different browser evidence would you seek?

**Self-review rule:** answer each question from memory, then verify with `index.html`, browser Elements/Network panels or official documentation. This file intentionally has no answers so it can be used repeatedly as a learning exercise.

## 11. Acceptance and maintenance notes

- **Confirmed:** the original learner's source passed the freeCodeCamp Workshop 04 final step (**100%**).
- **Preserved:** the three audio sources, track names, artist paragraphs, element order, viewport meta and title preserve the submitted values and order.
- **Not independently established:** current availability of all three MP3 files, behavior on every browser, complete accessibility conformance or rights to redistribute third-party audio.
- **Not in the repository:** Python tests, completion dates, compiled bundles, media binaries, helper scripts, or a custom JavaScript player.

See the [workshop README](./README.md) and [cumulative RWD_REVIEW](../../RWD_REVIEW.md) for the wider learning record.
