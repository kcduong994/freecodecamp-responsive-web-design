# Lab 06 — Video Compilation Page: Conceptual Review / Ôn tập kiến thức

**Evidence boundary:** The learner's screenshot marks this lab completed in freeCodeCamp. The original submission HTML is not available. The locally packaged page is reconstructed from the published 20 requirements and is **not** represented as an independently re-tested original solution.

## 1. HTML document hierarchy

The core rule is not just that the tags exist, but **where they appear in the Document Object Model (DOM)**.

```html
<body>
  <main>
    <h1>Web Development Video Library</h1>
    <p>Explore three video lessons.</p>
    <section>
      <h2>HTML lesson</h2>
      <p>An introduction to the lesson.</p>
      <iframe
        src="https://www.youtube.com/embed/pQN-pnXPaVg"
        title="HTML full course"
        width="560"
        height="315"></iframe>
    </section>
    <!-- Two additional sections follow the same pattern. -->
  </main>
</body>
```

`body > main` means that `main` is a **direct child** of `body`. The lab requires it to be the **only direct element child**. An `h1` adjacent to `main`, or a separate `footer` outside `main`, would violate that specific user story even if the page looked acceptable.

Every section should have these **direct** children in this order: `h2`, `p`, `iframe`. Placing the iframe in a wrapper `div`, omitting a paragraph or moving the heading after the iframe changes the DOM contract.

## 2. Semantic elements versus embedded browsing contexts

- `main` identifies the document's primary content.
- `section` groups a thematic video with its heading and explanatory paragraph.
- `h1` names the whole collection; each `h2` names a video section.
- `p` provides contextual prose rather than replacing semantic headings.
- `iframe` embeds another browsing context, such as a YouTube video player hosted on a different site.

`iframe` is not a native media decoder. Unlike `video > source`, it does not need a direct `.mp4` resource. A YouTube watch URL of the form `/watch?v=VIDEO_ID` is not the standard iframe embed URL; `/embed/VIDEO_ID` is the appropriate pattern for this task.

## 3. Essential iframe attributes

| Attribute | Function | Failure mode |
| --- | --- | --- |
| `src` | Specifies the webpage to embed | A watch page, typo or blocked provider may fail to render a player |
| `title` | Names the embedded content for assistive technologies | Missing or vague labels harm navigation |
| `width` | Sets the iframe's presented width | Fixed width can overflow smaller screens |
| `height` | Sets its presented height | An unsuitable aspect ratio may look distorted or awkward |
| `loading="lazy"` | Requests deferred loading until near the viewport | May delay loading; not required by the lab |
| `referrerpolicy` | Controls referrer information sent on navigation | Does not block all tracking or cookies |
| `allowfullscreen` | Permits fullscreen capability where supported | Does not guarantee provider playback or fullscreen permission |

The **acceptance contract** requires `src`, `title`, `height` and `width`. The other attributes are documented **extensions**; do not confuse them with requirements checked by the exercise.

## 4. Native media and third-party embeds

| Native video | YouTube iframe |
| --- | --- |
| `<video><source src="file.mp4" type="video/mp4"></video>` | `<iframe src="https://www.youtube.com/embed/VIDEO_ID"></iframe>` |
| Browser decodes the linked media resource | Embedded provider handles its own player page |
| Can use HTML video controls and captions | Provider controls are rendered in the embedded document |
| Direct video resource, correct MIME type important | Valid embed endpoint and provider policy important |

An HTTP-successful iframe page does not necessarily mean video playback is permitted. Check browser Console and Network, third-party restrictions, connectivity and embedded player error messages independently of markup tests.

## 5. Evidence-aware engineering workflow

The curriculum screenshot confirms a **completed activity marker**. It does not contain the student's submitted HTML, so it cannot prove the rebuilt local source equals that submission. The reconstructed example has been manually checked for the published structural contract, and should be tested against freeCodeCamp again if exact official acceptance evidence is needed.

Do not equate three iframes rendering in the browser with semantic correctness: the tester may additionally inspect sibling order, element count, direct-child relationships and attribute presence.

## 6. British English pronunciation / Phiên âm

| Term | British English IPA | Nghĩa tiếng Việt |
| --- | --- | --- |
| compilation | /ˌkɒm.pɪˈleɪ.ʃən/ | bản tổng hợp |
| embedded | /ɪmˈbed.ɪd/ | được nhúng |
| iframe | /ˈaɪ.freɪm/ | khung nhúng tài liệu |
| semantic | /sɪˈmæn.tɪk/ | có ngữ nghĩa |
| hierarchy | /ˈhaɪə.rɑː.ki/ | hệ phân cấp |
| attribute | /ˈæt.rɪ.bjuːt/ | thuộc tính |
| accessibility | /əkˌses.əˈbɪl.ɪ.ti/ | khả năng tiếp cận |
| viewport | /ˈvjuː.pɔːt/ | vùng hiển thị |
| browser | /ˈbraʊ.zə/ | trình duyệt |
| reference | /ˈref.ər.əns/ | tham chiếu |

## 7. Self-assessment questions / Câu hỏi tự kiểm tra

1. **Remember:** What is the difference between `main` and `section`?
2. **Understand:** Why does the exercise require `main` to be the only direct child of `body`?
3. **Debug:** Does `<body><header>...</header><main>...</main></body>` meet this specific lab's first user story?
4. **Apply:** Write a section with exactly three children in `h2`, `p`, `iframe` order.
5. **Analyse:** What is the difference between direct children and more distant descendants?
6. **Remember:** Which four iframe attributes are required in this lab?
7. **Compare:** When should an HTML author use `video > source` rather than an `iframe`?
8. **Debug:** Why might a YouTube `watch?v=` URL fail or behave unexpectedly in an iframe?
9. **Evaluate:** Does a present `src` attribute prove an embedded video can play?
10. **Apply:** How would you give three embedded frames unique descriptive titles?
11. **Analyse:** Why does `loading="lazy"` affect network timing but not DOM child order?
12. **Understand:** What is the meaning of `referrerpolicy="strict-origin-when-cross-origin"`?
13. **Evaluate:** Does that referrer policy automatically prevent third-party cookies?
14. **Debug:** Which browser tools help investigate an iframe showing an error or blank player?
15. **Compare:** How does the `title` of the iframe differ from the document's `<title>`?
16. **Analyse:** Does `width="560"` make the embed responsive on a narrow phone screen?
17. **Create — extension:** How would you present three coastal engineering training videos with meaningful section headings?
18. **Evaluate:** What evidence can a freeCodeCamp completion marker establish without the source code being available?
19. **Debug:** What happens to the required DOM contract if the `iframe` is nested inside a `div`?
20. **Evaluate:** What manual accessibility checks remain even if all 20 freeCodeCamp source tests pass?

Answers are intentionally omitted to support independent review.
