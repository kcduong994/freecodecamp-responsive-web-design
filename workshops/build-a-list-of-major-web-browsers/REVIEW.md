# Workshop 08 — Conceptual Review / Ôn tập kiến thức

**Activity:** Build a List of Major Web Browsers — freeCodeCamp Responsive Web Design V9.
**Original evidence:** Step 7, **7/7 completed (100%)**, with a passing freeCodeCamp code check.
**Source:** [index.html](./index.html), transcribed from the complete code supplied by the learner.
**Focus:** `dl`, `dt`, `dd`, association semantics, HTML hierarchy, defaults and evidence.

## 1. Description lists — danh sách mô tả

**Description list** /dɪˈskrɪp.ʃən lɪst/: danh sách gồm các thuật ngữ/tên và phần mô tả hoặc giá trị tương ứng.

```html
<dl>
  <dt>Google Chrome</dt>
  <dd>This is a free web browser developed by Google and first released in 2008.</dd>
</dl>
```

- `<dl>` is the container for groups of names/terms and their descriptions.
- `<dt>` introduces a name, term or label. It is not a heading element.
- `<dd>` contains its description/value; it follows the associated `dt` in this source.
- HTML allows more general groupings (e.g. one term with multiple descriptions or multiple terms sharing a description), but this exercise uses exactly one `dt` followed by one `dd` for each browser.

**Important:** here, `dt` and `dd` are **siblings inside `dl`**. Neither `dd` nor `dt` is nested inside the other. The relationship is expressed by their order and shared `dl` parent.

## 2. Exact completed DOM structure

```text
body
├── h1  List of Major Web Browsers
└── dl
    ├── dt  Google Chrome
    ├── dd  Chrome description
    ├── dt  Firefox
    ├── dd  Firefox description
    ├── dt  Safari
    ├── dd  Safari description
    ├── dt  Brave
    ├── dd  Brave description
    ├── dt  Arc
    └── dd  Arc description
```

In total: one description-list container, **five term elements** and **five descriptions**. The visible pairs are rendered by the browser from these ten children; no custom layout system, CSS or JavaScript is present.

The source includes the specific browser names **Google Chrome, Firefox, Safari, Brave and Arc**. Their descriptions are the student's exercise text; the task is semantic HTML, not a market-share comparison or a modern browser-history audit.

## 3. Compare `dl` with `ul` and `ol`

| Pattern | Appropriate use | Child elements |
| --- | --- | --- |
| `<ul><li>…</li></ul>` | Unordered collection | Each item uses `li` |
| `<ol><li>…</li></ol>` | Ordered procedure or ranking | Each step/item uses `li` |
| `<dl><dt>…</dt><dd>…</dd></dl>` | Terms with definitions, metadata, key/value relations | Groups of `dt` and `dd` |

**Example:** A list of five browsers without explanation could reasonably use `ul`. Once each name is associated with a descriptive statement, `dl` is a suitable semantic representation. An ordered list would misleadingly suggest a ranking or meaningful sequence unless one actually exists.

## 4. Browser interpretation and default presentation

The browser parses HTML into the **DOM** (*Document Object Model* /ˈdɒk.jə.mənt ˈɒb.dʒekt ˈmɒd.əl/ — mô hình đối tượng tài liệu). The user-agent stylesheet commonly indents `dd` elements while leaving `dt` aligned near the left edge. Such indentation is **presentation**, not a nesting relationship.

Inspect the Elements panel: a `dd` appears at the same DOM nesting level as its associated `dt`. Applying CSS later can change spacing without changing the description-list semantics.

Do not use `dl` solely to obtain default indentation. Choose it because the text genuinely describes or assigns values to named terms.

## 5. Document metadata and headings

The archived page is a standalone HTML5 document:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>List of Browsers and Descriptions</title>
  </head>
  <body>
    <h1>List of Major Web Browsers</h1>
    <!-- The browser description list follows. -->
  </body>
</html>
```

- The `title` is document metadata, usually shown on the browser tab. It is not the visible page heading.
- `h1` gives the document one clear main heading in this exercise.
- `lang="en"` identifies the language of the written content.
- `charset="UTF-8"` sets the character encoding.
- The viewport meta tag adjusts the initial layout viewport behavior on mobile devices; it does **not** create responsive CSS.

## 6. Common errors and debugging

| Symptom | Possible issue | How to check |
| --- | --- | --- |
| Term and description do not associate as intended | Misordered `dt`/`dd`, or a missing close tag | Inspect `dl` child sequence in Elements |
| The list is shown with bullets | Used `ul`/`li` instead of `dl`/`dt`/`dd` | Compare source tags |
| A description appears indented | Default browser stylesheet | Verify DOM sibling relationships |
| A browser name becomes a large heading | Accidentally used `h1`/`h2` instead of `dt` | Inspect HTML, not only visual appearance |
| Text characters are garbled | Encoding mismatch | Verify UTF-8 source and `meta charset` |
| Checker passes but the layout seems plain | No CSS was authored | Distinguish source acceptance from visual design |
| Someone claims market-share rank from the order | Ordering was for the exercise only | Do not infer rankings from `dl` |

**Potential accessibility extension:** a description list can expose term/description semantics to assistive technology. Actual announcements vary by browser and screen reader; a 100% exercise screenshot does not establish tested accessibility.

## 7. Key vocabulary with British English pronunciation

| English | IPA | Tiếng Việt |
| --- | --- | --- |
| Major | /ˈmeɪ.dʒə/ | Chính, quan trọng, phổ biến (theo ngữ cảnh) |
| Web browser | /web ˈbraʊ.zə/ | Trình duyệt web |
| Description | /dɪˈskrɪp.ʃən/ | Sự mô tả |
| Description list | /dɪˈskrɪp.ʃən lɪst/ | Danh sách mô tả |
| Term | /tɜːm/ | Thuật ngữ hoặc tên |
| Definition | /ˌdef.ɪˈnɪʃ.ən/ | Định nghĩa |
| Element | /ˈel.ɪ.mənt/ | Phần tử |
| Attribute | /ˈæt.rɪ.bjuːt/ | Thuộc tính |
| Heading | /ˈhed.ɪŋ/ | Tiêu đề |
| Document | /ˈdɒk.jə.mənt/ | Tài liệu |
| Nesting | /ˈnes.tɪŋ/ | Lồng phần tử |
| Sibling | /ˈsɪb.lɪŋ/ | Phần tử cùng cấp |
| Semantic | /sɪˈmæn.tɪk/ | Thuộc ngữ nghĩa |
| Hierarchy | /ˈhaɪə.rɑː.ki/ | Phân cấp |
| Chromium | /ˈkrəʊ.mi.əm/ | Dự án nền tảng trình duyệt Chromium |
| Rendering | /ˈren.dər.ɪŋ/ | Quá trình hiển thị |
| Browser engine | /ˈbraʊ.zə ˈen.dʒɪn/ | Bộ máy trình duyệt |
| User agent | /ˈjuː.zər ˈeɪ.dʒənt/ | Phần mềm tác nhân người dùng |
| Accessible | /əkˈses.ə.bəl/ | Có thể tiếp cận |
| Viewport | /ˈvjuː.pɔːt/ | Vùng hiển thị |
| Association | /əˌsəʊ.siˈeɪ.ʃən/ | Sự liên kết, quan hệ |

## 8. Self-assessment / Câu hỏi tự đánh giá

### Remember and understand

1. Expand the abbreviations `dl`, `dt` and `dd` in the context of HTML description lists.
2. How many `dt` elements and `dd` elements are in the completed browser list?
3. Which element is the direct parent of the five browser terms?
4. Are `dt` and `dd` nested or siblings in the submitted markup?
5. What is the difference between `<title>` and `<h1>`?
6. Explain why `lang="en"` and `charset="UTF-8"` address different concerns.
7. What role does `<!DOCTYPE html>` play in an HTML5 document?
8. Why is the presence of a viewport meta tag not sufficient proof of responsive layout?

### Apply and debug

9. Write a description-list entry for a new browser using exactly one `dt` and one `dd`.
10. Why should a `dd` explanation not be placed inside the opening/closing `dt` tags?
11. If descriptions are indented, does that prove `dd` is a child of `dt`? Explain.
12. Convert an unordered collection of three terms with explanations into a `dl`.
13. A `dl` contains a `li` for each browser. What structure would you use instead?
14. What should you inspect if an `h1` appears in the browser tab but not on the page?
15. How would you verify the exact child order in Chrome/Firefox Developer Tools?
16. Why might a description list be a better fit than a numbered list for browser definitions?

### Analyze and create

17. Could a description list contain one term with two descriptions? How would you represent it?
18. Give an example in which a description list is inappropriate even though it looks visually convenient.
19. Explain the difference between semantics and browser default styles.
20. What exactly does the Step 7 screenshot prove, and which checks are not covered?
21. **Extension:** Build a small glossary of five coastal engineering terms (e.g. tide, surge, bathymetry), each with a correct definition and units where relevant.
22. **Extension:** Describe how CSS might change the description list's layout while retaining meaningful DOM order.
23. **Extension:** How would you investigate how a screen reader announces the term and description pairs?
24. **Critical thinking:** Does the order of the five named browsers imply a popularity ranking? Why not?

Answers are intentionally omitted for active recall. Base answers on [`index.html`](./index.html), Developer Tools and the freeCodeCamp lesson; distinguish observed outcomes from assumptions.

## 9. Maintenance and evidence boundary

The student's submitted text and browser-release statements are preserved exactly (apart from formatting), not modernized or independently fact-checked. The freeCodeCamp screenshot supports **7/7 steps completed**; independent manual testing and external reference verification remain open.

The install helper included in the transfer ZIP is **not part of this workshop source** and is not committed to the repository.
