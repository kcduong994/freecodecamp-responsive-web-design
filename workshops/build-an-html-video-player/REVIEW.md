# Workshop 05 — Conceptual Review / Ôn tập kiến thức

**Activity:** Build an HTML Video Player · freeCodeCamp Responsive Web Design V9
**Evidence:** Learner's Step 13 screenshot: **13/13 (100%)**, "Your code passes"
**Source:** [index.html](./index.html) · the learner's final markup plus lesson-provided opening HTML boilerplate
**Learning rule:** Explain and investigate what has actually been practiced before exploring extra capabilities.

## 1. Read the completed source, not an imagined production app

The completed page has **one visible `h1`**, **one `<video>` player**, **four `<source>` candidates**, and **one image URL provided via `poster`**. There is no custom JavaScript, no custom CSS, no playlist, no upload form, and no server API. The screenshot confirms the workshop checker accepted the learner's submitted code. It does not verify every remote video format on every browser.

**English:** "Build an HTML Video Player" /bɪld ən ˌeɪtʃ tiː em ˈel ˈvɪd.i.əʊ ˈpleɪ.ə/.
**Tiếng Việt:** Xây dựng trình phát video HTML.
**Mental model:** HTML defines the media element and its candidate sources. The browser decides if and how it can decode the resource and render native controls.

## 2. HTML document structure and separation of roles

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Working with the HTML Video Element</title>
</head>
<body>
  <h1>Working with the HTML Video Element</h1>
  <!-- Video player is here -->
</body>
</html>
```

- `<!DOCTYPE html>` requests standards-mode HTML parsing; it is a declaration, not an HTML element.
- `lang="en"` communicates the document's primary language to user agents and assistive technology. It is unrelated to codec selection.
- `meta charset="UTF-8"` specifies character encoding; not the media MIME type.
- The viewport meta declaration helps mobile browser viewport configuration; it does not create responsive layout by itself.
- `<title>` appears in the browser's tab and is not the same element as visible `<h1>`; their textual equality in this workshop is a content choice.

## 3. Anatomy of the `<video>` element

```html
<video width="640" loop controls muted
       poster="https://cdn.freecodecamp.org/curriculum/labs/past-event2.jpg">
  <source src="https://cdn.freecodecamp.org/curriculum/labs/what-is-the-map-method-and-how-does-it-work.mp4" type="video/mp4">
  <source src="https://cdn.freecodecamp.org/curriculum/labs/mapmethod.webm" type="video/webm">
  <source src="https://cdn.freecodecamp.org/curriculum/labs/mapmethod.ogg" type="video/ogg">
  <source src="https://cdn.freecodecamp.org/curriculum/labs/mapmethod.mov" type="video/quicktime">
</video>
```

The `video` element defines one media playback context. The nested `source` elements are candidate sources, **not four independently rendered videos**. When sources are listed inside `video`, the browser evaluates candidates using MIME hints and supported decoding behavior. What is actually selected can be inspected through browser developer tools. The complete outer element has a closing tag; each `source` element is void and has no end tag.

### 3.1 HTML element versus media resource

- `<video>` is the **HTML element**; it is not the bytes of the MP4/WebM/Ogg/MOV file.
- `src` contains a **URL** identifying the remote resource.
- `type` gives a **MIME type hint** to help the user agent select a playable resource. It cannot force support for a codec that the browser lacks.
- The filename extension (e.g. `.mp4`) and the MIME type (e.g. `video/mp4`) should agree, but neither alone guarantees decoding support.

### 3.2 Candidate formats versus codecs

| Source candidate | Declared MIME | What to remember |
| --- | --- | --- |
| `.mp4` | `video/mp4` | MP4 is a container; its codec determines whether it can actually play |
| `.webm` | `video/webm` | WebM is a container commonly used on the web; codec support still matters |
| `.ogg` | `video/ogg` | Ogg video may be less consistently supported depending on browser/platform |
| `.mov` | `video/quicktime` | QuickTime format may require compatible software/codecs and is not universal on the web |

**Do not conclude:** All four formats are supported merely because freeCodeCamp accepted all four `source` elements. A checker may verify correct markup and declared attributes without reproducing all real-world playback conditions.

## 4. Attributes: `width`, `loop`, `controls`, `muted`, `poster`

| Attribute | In this workshop | Meaning and limits |
| --- | --- | --- |
| `width="640"` | Present | Width of the video display area; not by itself a fluid responsive rule |
| `loop` | Present | Replays the **same** video when it reaches its end |
| `controls` | Present | Requests native browser UI (play/pause/seek/volume where supported) |
| `muted` | Present | Sets the media's default muted state; user can typically unmute |
| `poster="...jpg"` | Present | Image shown before a video frame is available, subject to browser/loading behavior |
| `autoplay` | **Absent** | The completed source does not request automatic playback |
| `preload` | **Absent** | No explicit preload hint is provided; browser chooses its default loading behavior |
| `height` | **Absent** | No explicit video height is specified in the exercise |

### 4.1 Boolean attributes / Thuộc tính logic

For HTML Boolean attributes, **presence** means true, and **absence** means false. Both `controls` and `controls=""` request controls. Writing `muted="false"` still leaves the Boolean attribute *present* and therefore does not have the intended meaning. This differs from string-valued `width="640"` or `poster="..."`.

### 4.2 `loop` is not `autoplay`

`loop` requests repetition **after** an existing playback reaches its end; `autoplay` requests that playback start without manual interaction, subject to policy restrictions. This exercise uses `loop` but **not** `autoplay`. The presence of `muted` does not make autoplay implicit.

### 4.3 `poster` is not a fallback video

A poster can provide a visual preview. A successful poster image request does **not** establish that any MP4/WebM/Ogg/MOV candidate is playable. Conversely, the video may play even when the poster request fails. Use separate Network entries to investigate each resource.

## 5. Source selection, ordering and errors

The exercise lists MP4 → WebM → Ogg → QuickTime. Browsers evaluate source candidates for suitable type/codec support and load a selected resource according to their media algorithms. It is incorrect to describe all four as automatically downloaded or played sequentially. Fallback source order influences what compatible source can be selected; actual behavior may differ by platform and configuration.

**Diagnostic sequence:**

1. **Markup:** in DevTools **Elements**, confirm the `video` element contains four valid, direct `source` children and the closing `</video>`.
2. **Selection:** in DevTools, inspect the resolved selected resource (for example `video.currentSrc` when investigating interactively) and supported media types.
3. **Network:** check for HTTP status such as 404/403, interrupted responses, content-type errors, failed cross-origin loading or offline connectivity.
4. **Decoding:** a successful HTTP response may still carry unsupported media encoding; read browser media/console diagnostics.
5. **UI:** verify poster, dimensions, mute state and native controls; check whether the media has loaded metadata/duration.
6. **Interaction:** manually test play/pause/seek/loop and keyboard use as applicable; the screenshot is not equivalent to this verification.

**Important distinction:** `source type="video/mp4"` is descriptive metadata on a candidate; it does **not** transcode other formats into MP4.

## 6. Responsiveness, accessibility and author intent

### Responsiveness

The HTML provides a 640-pixel width without additional responsive styling. The viewport meta tag alone does not guarantee that the player fits narrow screens. **Extension, not part of this completed exercise:** CSS such as `video { max-width: 100%; height: auto; }` can constrain overflow relative to its container.

### Accessibility

- The visible `h1` describes the page; it is **not** a transcript or captions for the video content.
- Native controls generally provide familiar interactions, but keyboard behavior and presentation vary across browser/device combinations.
- `poster` is visual preview content, not an alternative text transcript of the video.
- **Extension:** captions/subtitles commonly use `<track kind="captions" ...>` with a separate timed-text asset. This workshop did not add `<track>`.
- For important scientific or instructional media, consider captions, a transcript, and accessible context; evaluate real behavior rather than assuming a passing checker guarantees accessibility.

## 7. Compare this workshop with Workshop 04 (audio)

| Aspect | Workshop 04 — Audio | Workshop 05 — Video |
| --- | --- | --- |
| HTML root media element | Three `<audio>` elements | One `<video>` element |
| Resource specification | Each `audio` has its own MP3 `src` | Four nested `<source>` candidate URLs |
| Player count | Three independent native audio players | One native video player |
| Shared attributes | `controls`, `loop` | `controls`, `loop` |
| New attributes practiced | — | `muted`, `poster`, `width` |
| Format hint | Not explicitly specified | Four explicit MIME hints |
| Custom JavaScript | None | None |
| Verification evidence | Original screenshot 9/9 (100%) | Original screenshot 13/13 (100%) |

**Connection to Lab 04:** a correct `src` attribute and a satisfied source checker are separate from proving an external image or video loads. **Connection to Workshop 03:** static HTML buttons do not implement custom behavior, whereas browser-native media controls have built-in actions.

## 8. Troubleshooting / Những lỗi thường gặp

| Symptom | Likely cause | What to inspect |
| --- | --- | --- |
| Video is invisible | Missing `<video>`, malformed tree, no display region | Elements and structure |
| Control bar missing | `controls` absent | `video` attributes |
| Video looks silent | `muted` present, volume low or track has no sound | Mute icon and actual media |
| Poster shows but video won't play | Failed network media request or unsupported format | Network + media errors |
| Source names appear as text | Tags malformed, wrong nesting or broken delimiters | HTML markup |
| The lesson checker fails | Misspelled `src`, `type`, exact URL or title, wrong number of sources | Compare Step 13 requirements |
| Playback cannot repeat | `loop` absent or media never reaches end | Attribute and timeline |
| Player overflows on mobile | Fixed width without responsive constraint | Viewport size, CSS (future lesson) |
| MP4 works but MOV doesn't | Format/container/codec support differs | Browser/platform compatibility |
| All four URLs appear but no media plays | HTTP error, codec issue or network restriction | `currentSrc`, Network, Console |

## 9. Technical vocabulary & pronunciation / Từ vựng và cách đọc (British English IPA)

| Term | IPA | Nghĩa tiếng Việt |
| --- | --- | --- |
| Video player | /ˈvɪd.i.əʊ ˈpleɪ.ə/ | Trình phát video |
| Multimedia | /ˌmʌl.tiˈmiː.di.ə/ | Đa phương tiện |
| Media element | /ˈmiː.di.ə ˈel.ɪ.mənt/ | Phần tử đa phương tiện |
| Source | /sɔːs/ | Nguồn dữ liệu |
| Browser | /ˈbraʊ.zə/ | Trình duyệt |
| Controls | /kənˈtrəʊlz/ | Các điều khiển |
| Loop | /luːp/ | Lặp lại |
| Muted | /ˈmjuː.tɪd/ | Được tắt tiếng |
| Poster | /ˈpəʊ.stə/ | Ảnh xem trước |
| Playback | /ˈpleɪ.bæk/ | Quá trình phát |
| Codec | /ˈkəʊ.dek/ | Bộ mã hóa/giải mã |
| Container | /kənˈteɪ.nə/ | Định dạng bao chứa dữ liệu |
| Format | /ˈfɔː.mæt/ | Định dạng |
| Compatible | /kəmˈpæt.ə.bəl/ | Tương thích |
| MIME type | /maɪm taɪp/ | Kiểu nội dung truyền thông |
| Fallback | /ˈfɔːl.bæk/ | Phương án thay thế |
| Captions | /ˈkæp.ʃənz/ | Phụ đề (mô tả lời nói và âm thanh liên quan) |
| Transcript | /ˈtræn.skrɪpt/ | Bản chép lời |
| Resolution | /ˌrez.əˈluː.ʃən/ | Độ phân giải |
| Viewport | /ˈvjuː.pɔːt/ | Vùng hiển thị |
| Accessibility | /əkˌses.əˈbɪl.ə.ti/ | Khả năng tiếp cận |
| Encoding | /ɪnˈkəʊ.dɪŋ/ | Mã hóa |
| QuickTime | /ˈkwɪk.taɪm/ | Định dạng/nền tảng đa phương tiện QuickTime |

These are pronunciation aids; HTML code tokens themselves are spelled literally rather than pronounced as English sentences.

## 10. Self-assessment — 30 questions (intentionally no answer key)

Try answering *why* the browser behaves this way before consulting DevTools or documentation. Questions are divided into increasing cognitive difficulty.

### A. Remember and understand / Nhớ và hiểu

1. What does `<video>` represent in the completed page? What does it **not** represent?
2. Which attribute requests built-in play/pause/seek controls? Is its value a string or Boolean?
3. Explain how `loop` differs from `autoplay`.
4. Explain how `muted` affects the default audio state. Does it automatically start playback?
5. What is the purpose of `poster`? Does it guarantee playable video?
6. How many `<video>` and `<source>` elements are in the completed file? How many separate players does the browser render?
7. Why is `<video>` closed with `</video>`, while `<source>` has no closing tag?
8. What is the role of `type="video/webm"` on a `<source>` element?
9. Distinguish a file extension, a container format, a codec, and an HTTP `Content-Type`.
10. Why do `<title>` and `<h1>` occupy different parts of the HTML document?

### B. Apply and debug / Vận dụng và gỡ lỗi

11. What would you change if the video has no native control bar?
12. Why might `<video muted="false">` still produce a muted player? Correct the markup.
13. A developer puts four `<source>` tags outside the `<video>` element. What is structurally wrong?
14. The poster loads but clicking Play does nothing. Which three distinct classes of failure would you investigate?
15. How can DevTools tell you which candidate source the browser selected?
16. A resource URL returns HTTP 404. Is this automatically a syntax error in the `video` tag?
17. Suppose the MP4 loads successfully but fails decoding. Which checks distinguish content type from actual codec support?
18. Explain why setting `loop` does not automatically advance from MP4 to WebM.
19. The video is cut off on a narrow phone screen. What CSS **extension** could fix this while keeping the original HTML lesson intact?
20. If the fourth `<source>` omits `type`, how could the browser still attempt it, and what useful selection hint would be lost?

### C. Analyze, evaluate and extend / Phân tích, đánh giá, mở rộng

21. Why can the earlier audio workshop render three players, while this video workshop with four sources renders only one?
22. Why do four format candidates not ensure universal browser playback?
23. What exactly does freeCodeCamp's 13/13 result prove? What does it not prove?
24. Is `width="640"` sufficient to call the page responsive? Justify using HTML layout and viewport concepts.
25. Assess the accessibility implications of having a poster and an `h1` but no captions or transcript.
26. Compare a Network 403/404 error, a blocked HTTPS request, and a decoder/codec error. What observable evidence differs?
27. How would you verify keyboard interaction with native media controls across two browsers?
28. **Extension:** outline how a `<track kind="captions">` might improve an instructional video page. Why must captions be supplied as a separate timed-text resource?
29. **Extension for coastal engineering:** describe an HTML page showing a wave-flume experiment video. Which source metadata, captions and descriptive context would you provide beyond the workshop requirements?
30. **Design judgment:** when should you prefer a single `<video>` with alternative `<source>` formats over several separate `<video>` players?

**Self-study approach:** answer in English or Vietnamese, explain your reasoning, then verify through `index.html`, DevTools and official browser/HTML documentation. The unanswered questions are intentional for repeated revision.

## 11. Completion evidence and maintenance

- **Confirmed:** user screenshot displays a green check and **100%** completion in freeCodeCamp at Step 13.
- **Confirmed from supplied fragment:** `h1`, `video` attributes, poster URL and four `source` URLs/types/order.
- **Reconstructed from lesson's visible scaffold:** opening doctype, `html`, `head` metadata, `title` and opening `body`. This is made explicit so the local HTML document is complete without pretending those lines were pasted in the final message.
- **Not independently verified:** exact behavior of all media formats, current network access to resources, end-to-end keyboard accessibility, or cross-browser playback.
- **Repo rules:** no completion dates, Python tests, media binary downloads, update scripts or unnecessary dependencies.

See [README](./README.md) and [RWD_REVIEW](../../RWD_REVIEW.md) for the complete record.
