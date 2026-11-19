# Lab 05 — HTML Audio and Video Player: Conceptual Review / Ôn tập kiến thức

**Evidence:** The learner completed all **18/18 freeCodeCamp tests (100%)** with an MP4 video and an audio element pointing to an unprovided relative MP3 path. The archived HTML uses a freeCodeCamp-provided MP3 URL instead. The revised edition has **not** been resubmitted to freeCodeCamp; browser playback still requires verification.

## 1. Concepts from this independent lab

This exercise bridges two workshops:

- **Music Player workshop:** `audio` provides native controls; Boolean `loop` repeats a track; `src` names the resource.
- **Video Player workshop:** `video` displays a video, and nested `source` elements can describe resources and media types.
- **This lab:** combines both in two semantic `section` elements, satisfying explicit document-tree and attribute requirements.

### 1.1 Page hierarchy and semantics

```html
<h1>The Map Method</h1>
<section>
  <h2>Method Video</h2>
  <video width="640" controls>
    <source src="https://example.org/video.mp4" type="video/mp4">
  </video>
</section>
<section>
  <h2>Sailing Away</h2>
  <audio src="https://example.org/song.mp3" controls loop></audio>
</section>
```

The example illustrates **relationships**, not a promise that the `example.org` media resources exist. The lab requires **two** `section` elements, each with an `h2` followed by a media element. `section` denotes a thematic region of the document; `div` is a generic grouping container without equivalent section semantics.

### 1.2 `video > source` versus `audio[src]`

`video` and `audio` are **media elements**. `source` is a **void element**, so it must not have a `</source>` closing tag. `video` can choose a supported media file from its child sources; in this lab, only one MP4 source is required. The audio player uses the `src` attribute directly on `audio` rather than nesting `source`, and both patterns are valid in HTML when used appropriately.

**Valid:**

```html
<video width="640" controls>
  <source src="movie.mp4" type="video/mp4">
</video>
<audio src="song.mp3" controls loop></audio>
```

**Invalid lab interpretation:** putting `controls` and `width` on `source`, adding `</source>`, or closing `video` before its child `source`.

### 1.3 MIME types and file extensions

MIME (*Multipurpose Internet Mail Extensions*) types identify resource formats. The lab checks that `type="video/mp4"` corresponds to a `.mp4` media URL. This helps browsers choose suitable media candidates. The declared type does **not** convert the resource into MP4 or prove it contains a decodable codec.

| Resource | Typical HTML media type |
| --- | --- |
| `.mp4` video | `video/mp4` |
| `.webm` video | `video/webm` |
| `.ogg` video | `video/ogg` |
| `.mp3` audio | `audio/mpeg` |

The audio element in this lab is not required to declare a `type` when using a direct `src`.

### 1.4 Boolean attributes

`controls` exposes built-in playback controls. `loop` asks the browser to restart the media after reaching the end. Their mere **presence** enables the behavior:

```html
<audio controls loop src="song.mp3"></audio>
```

Writing `loop="false"` still counts as the attribute being present; to disable looping, **remove `loop`**. `loop` is not the same as `autoplay`. Browsers often restrict audible autoplay even if explicitly requested, and this lab does not require autoplay.

### 1.5 The meaning of `width="640"`

The lab explicitly requires a numeric width of **640 CSS pixels** on the video element. This is an HTML presentation attribute, not proof that the layout adapts to mobile screens. A future CSS lesson can constrain the rendered width using `max-width: 100%` and a suitable layout while preserving the exercise's required attribute.

## 2. Debugging evidence from the learner's attempt

| Observation | Interpretation | Correction |
| --- | --- | --- |
| YouTube `watch?v=...` used as `source src` | A web page URL, not a direct MP4 resource | Use the supplied direct MP4 CDN URL |
| `type="video/mp4"` attached to YouTube page | MIME claim does not match actual URL/resource | Use a real `.mp4` resource |
| `</video>` placed before the source or attributes placed on `source` | Incorrect media element hierarchy | Use `<video width="640" controls><source ...></video>` |
| Test 9/11 passed, but Test 10/12 failed | Correct element and attribute presence, incorrect resource-type contract | Correct the URL and matching MIME type |
| Lab passed 18/18 while audio showed `0:00 / 0:00` | Source checker cannot prove a playable media file exists | Use a known media resource; investigate Network and media errors |
| `src="whatisthemapmethod.mp3"` used without a supplied file | Relative path requires an accessible file at the resolved location | Archived edition uses official freeCodeCamp MP3 URL |

### 2.1 Why YouTube URLs cannot be used directly as MP4 sources

A URL ending in `/watch?v=...` points to an HTML player page. `<video>` expects a media resource, not another webpage. An `iframe` with a `/embed/...` URL can load a provider player, but it is a distinct embedding model and would not satisfy this lab's required `<video>` plus `<source>` structure. Do not confuse the validity of a URL with the suitability of its representation as a media source.

### 2.2 What does a passing checker actually establish?

**Established by the screenshot:** the original submission satisfied freeCodeCamp's 18 structural/code checks.

**Not established:** the original audio resource was available; the new MP3 URL will remain online; video/audio playback works in every browser; the page is responsive; the content includes captions/transcripts; or the revised archive has passed a fresh official test.

A technically complete learning record must preserve this evidence boundary rather than claim additional success by implication.

## 3. Recommended manual debugging sequence

1. Compare failing test wording with the source: required tag, attribute, count, text and nesting.
2. Verify the DOM in **Elements**, not only the raw source or visible preview.
3. For media that does not play, check **Network**: request URL, status, response headers and actual bytes returned.
4. Check the browser media UI: duration, loading state, play action, error messages and support for the file's codec.
5. Check that the file can be opened from the same browser under the same network conditions.
6. Re-run the freeCodeCamp checker **after** editing the code, and record which version was actually verified.
7. Evaluate keyboard access, available captions/transcripts and layout behavior separately from structural code acceptance.

## 4. Technical vocabulary — British English IPA / Từ vựng kỹ thuật

| English | IPA | Vietnamese / Giải nghĩa |
| --- | --- | --- |
| Audio | /ˈɔː.di.əʊ/ | Âm thanh; đọc gần "o-đi-âu" |
| Video | /ˈvɪd.i.əʊ/ | Video, hình ảnh động; đọc "vi-đi-âu" |
| Player | /ˈpleɪ.ə/ | Trình phát |
| Control | /kənˈtrəʊl/ | Điều khiển |
| Source | /sɔːs/ | Nguồn dữ liệu |
| Resource | /rɪˈzɔːs/ | Tài nguyên |
| Section | /ˈsek.ʃən/ | Khu vực nội dung có chủ đề |
| Heading | /ˈhed.ɪŋ/ | Tiêu đề |
| Attribute | /ˈæt.rɪ.bjuːt/ | Thuộc tính của thẻ |
| Loop | /luːp/ | Lặp lại |
| Playback | /ˈpleɪ.bæk/ | Hoạt động phát media |
| Media | /ˈmiː.di.ə/ | Phương tiện đa truyền thông |
| Direct URL | /dɪˈrekt ˌjuː.ɑːrˈel/ | Địa chỉ trực tiếp đến tài nguyên |
| MIME type | /maɪm taɪp/ | Kiểu nội dung media |
| Codec | /ˈkəʊ.dek/ | Bộ mã hóa và giải mã |
| Network | /ˈnet.wɜːk/ | Mạng; tab theo dõi yêu cầu |
| Duration | /djʊəˈreɪ.ʃən/ | Thời lượng |
| Accessibility | /əkˌses.əˈbɪl.ə.ti/ | Khả năng tiếp cận |
| Caption | /ˈkæp.ʃən/ | Phụ đề/hướng dẫn hiển thị |
| Transcript | /ˈtræn.skrɪpt/ | Bản chép nội dung lời nói |

## 5. Self-assessment questions — questions first, research the answers

### A. Remember and understand

1. What is an HTML media element, and which two media elements are practiced here?
2. Why does the lab ask for one `h1` and two `section` elements?
3. What is the difference between a `section` and a generic `div`?
4. Why should each section have its own meaningful `h2`?
5. What does `controls` change, and which user-agent component draws the buttons?
6. What does `loop` do? Does it automatically start playback?
7. What is the meaning of `src` on `audio`?
8. Why does `source` not have a closing tag?
9. Why is the video width required to be `640`, and what is not implied by that width?
10. What is the difference between a resource filename and its MIME type?

### B. Apply and debug

11. Correct `<source controls width="640" src="movie.mp4" type="video/mp4"></source>` as part of a valid video player.
12. Why can't `<video><source src="https://www.youtube.com/watch?v=..." type="video/mp4"></video>` play the YouTube watch page?
13. Given `film.webm`, what MIME type would ordinarily correspond to that extension?
14. Given an MP3 source directly on `<audio>`, is a nested `<source>` required by this lab? Why?
15. An audio player displays `0:00 / 0:00`. What evidence would you inspect before diagnosing the cause?
16. Why might a relative audio file path work in one local directory but fail in freeCodeCamp's editor?
17. An MP4 loads but produces an unsupported-format error. Why is a matching `.mp4` extension insufficient proof of codec support?
18. What happens to `<audio loop="false">`? How would you truly disable looping?
19. How do you distinguish an HTTP 404 media error from a decoder/codec problem?
20. Draw the DOM hierarchy expected for this lab and identify each element's parent and siblings.

### C. Evaluate and design

21. Why is 18/18 evidence of requirement satisfaction but not a comprehensive user-experience assessment?
22. Should a music player for a real website use `autoplay` by default? Explain browser policy and user choice.
23. How could you provide captions and a transcript for an instructional video beyond this lab's scope?
24. What issues could arise when viewing a 640-pixel video in a 320-pixel-wide viewport?
25. When should you use a video `poster` and when might it become misleading?
26. Compare one video with multiple alternative `source` elements against three separate audio elements used as independent songs.
27. In a coastal engineering field course, what media metadata and contextual notes would make an experiment recording scientifically interpretable?
28. How would you design a manual verification checklist so that "passed tests", "media loaded" and "accessible to users" remain distinct outcomes?

**Practice policy:** Keep your answers grounded in the completed HTML, the official user stories and real browser observations. Questions are intentionally left unanswered in the archive to support active recall and independent investigation. Do not add dates, Python tests or repository-maintenance scripts.
