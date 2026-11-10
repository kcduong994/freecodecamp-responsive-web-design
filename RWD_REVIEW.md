# Responsive Web Design — Cumulative Conceptual Review

> **Status:** **In progress** — Chapter 01 documented after Workshop 01 (2026-11-10).  
> **Curriculum:** freeCodeCamp Responsive Web Design V9.  
> **Final review:** **Not yet completed**; this document will be expanded and critically revised after the remaining practical curriculum.  
> **Evidence checkpoint:** [`83af1c7`](https://github.com/kcduong994/freecodecamp-responsive-web-design/commit/83af1c7d02ab4c835c1ce78d1feac82ce4150bdb) on `main`.

## Why this document exists / Mục đích

This is the **repository-wide knowledge synthesis**. It is not a transcript of freeCodeCamp instructions, a substitute for the source code, or a collection of unverified completion claims.

- **Workshop `README.md`:** the specific exercise, requirements, artifacts and verification evidence.
- **Workshop `REVIEW.md`:** step-level concepts, vocabulary, common mistakes and practice questions.
- **Root `RWD_REVIEW.md`:** the underlying browser and web-design mental models that connect multiple exercises over time.

**Status labels:** **Learned** = covered in a completed exercise; **Explained** = supported conceptual interpretation; **Extension** = relevant background not yet taught in that exercise; **Planned** = future curriculum coverage, not yet complete.

## Six-question review framework

Every chapter will answer:

1. **What did we learn?** — Concept, purpose and correct use.
2. **What does the browser receive?** — HTML, CSS, assets and document metadata, when applicable.
3. **What does the browser do?** — Parse, construct DOM/CSSOM, apply styles and lay out/render the document, as each topic is learned.
4. **What does the user experience?** — Visual structure, reading order, navigation and accessibility.
5. **What can fail?** — Incorrect semantics, malformed markup, broken resources, layout problems or misleading assumptions.
6. **How do we verify it?** — Workshop requirements, local tests, browser inspection, validation and accessibility checks, each within its stated scope.

## Learning map

| Chapter | Domain | Status | Evidence |
| --- | --- | --- | --- |
| 01 | HTML structure and heading hierarchy | **Learned + explained** | [Workshop 01](./workshops/build-a-curriculum-outline/README.md), **11/11 steps**, **8/8 local tests** |
| 02 | HTML attributes and document boilerplate | **Planned** | Some standalone scaffolding was added to Workshop 01's archived file; this does not constitute completion of the theory lessons |
| 03 | Links, images, lists, semantic sections, tables and forms | **Planned** | No completed repository exercises |
| 04 | CSS syntax, selectors, cascade, inheritance, typography, color and box model | **Planned** | No completed repository exercises |
| 05 | Layout: dimensions, positioning, Flexbox, Grid and responsive design | **Planned** | No completed repository exercises |
| 06 | Pseudo-classes/elements, custom properties and CSS effects | **Planned** | No completed repository exercises |
| 07 | Debugging, accessibility, browser tools and project verification | **Develop gradually** | Only basic inspection/checking in Workshop 01 so far |

---

# Chapter 01 — HTML structure and heading hierarchy (Workshop 01)

**Primary exercise:** [Build a Curriculum Outline](./workshops/build-a-curriculum-outline/) — completed **11/11 steps**, **100%** in the user-supplied freeCodeCamp screenshots dated **2026-11-10**. The independent Python suite showed **8/8 tests passed** in the user's local terminal. The source was pushed to `main` at the checkpoint listed above.

### 1. What did we learn? / Học được gì?

**Learned:** **HTML** (*HyperText Markup Language* — ngôn ngữ đánh dấu siêu văn bản) describes the **structure and meaning** of a webpage's content. A browser can display plain text, but marking it up gives that content an explicit role.

The workshop introduces these elements:

| Markup | Function in the completed exercise | Count |
| --- | --- | ---: |
| `<h1>` | Page-level welcome heading | 1 |
| `<h2>` | Curriculum heading beneath the page title | 1 |
| `<h3>` | Parallel headings for HTML, CSS and JavaScript topics | 3 |
| `<p>` | Introductory and explanatory paragraphs | 4 |

**Tag vs element:** in `<h3>Introduction to HTML</h3>`, `<h3>` is the **opening tag**, `Introduction to HTML` is its **text content**, `</h3>` is the **closing tag**, and the whole marked-up structure represents an **HTML element**.

**Heading hierarchy:** `<h1>` → `<h2>` → three sibling `<h3>` headings. Choose heading levels to reflect the document's logical structure, **not merely to obtain a particular font size**. The beginner guidance to use one meaningful page-level `<h1>` fits this example; multiple `<h1>` elements do not automatically make an HTML document invalid.

**HTML, CSS, JavaScript:** HTML expresses content and structure; CSS expresses visual presentation and layout; JavaScript can add program behavior and interactivity. **Only HTML was authored in this workshop.**

### 2. What does the browser receive? / Trình duyệt nhận gì?

**Learned:** The original freeCodeCamp editor shows a short HTML **fragment** containing headings and paragraphs, for example:

```html
<h3>Introduction to HTML</h3>
<p>HTML represents the content and structure of a webpage</p>
```

**Extension — packaging, not a completed lesson:** The [archived local `index.html`](./workshops/build-a-curriculum-outline/index.html) adds `<!DOCTYPE html>`, `<html lang="en">`, `<head>`, document metadata, `<title>` and `<body>` to make a standalone HTML5 file. These additions belong conceptually to upcoming boilerplate lessons; do **not** report those lessons as completed.

The archived page deliberately retains the screenshot's `Javascript`/`javaScript` capitalization. The conventional name for the language is **JavaScript**; copying lesson evidence is not a recommendation for production wording.

### 3. What does the browser do? / Trình duyệt xử lý thế nào?

**Explained:** After receiving HTML bytes, the browser's HTML parser processes the markup and constructs a **DOM** (*Document Object Model*) tree. The `<h1>`, `<h2>`, `<h3>` and `<p>` become elements with relationships that can be inspected in developer tools.

**Extension:** Browsers also apply a **user-agent stylesheet** (CSS mặc định). This is why the same text appears larger/bolder after it is wrapped in `<h1>` or `<h2>`, even though no stylesheet was written in this workshop. Browser defaults are a presentation detail, not the semantic purpose of the headings.

Conceptual sequence:

```text
HTML text received
      ↓
HTML parsing and DOM construction
      ↓
Browser default styles (no author CSS in this exercise)
      ↓
Layout and rendered headings/paragraphs
```

The full rendering pipeline (CSSOM, cascade, style calculation, layout, paint and compositing) will be examined in later CSS chapters; **it has not been taught or independently tested here**.

### 4. What does the user experience? / Người dùng thấy gì?

**Learned:** The preview displays a prominent welcome title, a curriculum title, an introductory paragraph, and three topic sections. The structure makes the page readable without custom styling.

**Explained:** Semantic headings help communicate section hierarchy to people and assistive technologies. A heading is not equivalent to an arbitrary `<p>` made visually large with CSS. This simple page is a **starting point** for accessibility, not proof of an accessible or production-ready interface.

### 5. What can fail? / Những lỗi nào cần tránh?

| Potential issue | Why it matters | What to check |
| --- | --- | --- |
| Mismatched opening/closing tags | May yield an unintended DOM tree | Compare tag names; inspect resulting element structure |
| Choosing `<h3>` only because it looks smaller | Confuses semantic hierarchy with styling | Read headings as a nested outline |
| Leaving descriptive prose as raw text | Loses paragraph semantics | Use `<p>` for genuine paragraphs |
| Treating CSS/JavaScript descriptions as authored code | Overstates exercise scope | Review actual `index.html` source |
| Assuming freeCodeCamp pass proves accessibility | The test only verifies its own criteria | Perform separate browser, keyboard and assistive-technology checks when those become relevant |
| Mistaking archive scaffolding for freeCodeCamp steps | Misstates the learning record | Separate workshop fragment from locally added document shell |

### 6. How do we verify it? / Kiểm tra ra sao?

**Verified evidence:**

- **freeCodeCamp:** all **11** workshop steps completed, with a 100% result visible in the supplied screenshots.
- **Local:** `python -m unittest` reported **8 tests** and `OK` in the supplied Windows terminal screenshot. The tests check the archived HTML structure, expected content, metadata and absence of separately authored CSS/JavaScript.
- **GitHub:** the finished workshop source and documentation were committed and pushed to `main` at commit `83af1c7`.

**Not verified:** cross-browser rendering, screen-reader behavior, keyboard accessibility, responsive behavior across viewport sizes, W3C validation and production deployment. Those checks are outside the workshop's verified evidence.

Reproduce the source tests from the repository root:

```powershell
py -m unittest discover -s workshops/build-a-curriculum-outline/tests -p "test_*.py" -v
```

For manual inspection, open `index.html` and examine the document in the browser's **Developer Tools → Elements** panel. Compare the DOM hierarchy with the intended headings and paragraphs. This is a recommended check, **not an additional completed test claim**.

### Technical English — core vocabulary (British English IPA)

| Term | Pronunciation | Nghĩa tiếng Việt |
| --- | --- | --- |
| Hypertext | /ˈhaɪ.pə.tekst/ | Siêu văn bản |
| Markup | /ˈmɑː.kʌp/ | Ngôn ngữ đánh dấu / đánh dấu |
| Element | /ˈel.ɪ.mənt/ | Phần tử |
| Opening tag | /ˈəʊ.pən.ɪŋ tæɡ/ | Thẻ mở |
| Closing tag | /ˈkləʊ.zɪŋ tæɡ/ | Thẻ đóng |
| Heading | /ˈhed.ɪŋ/ | Tiêu đề |
| Paragraph | /ˈpær.ə.ɡrɑːf/ | Đoạn văn |
| Hierarchy | /ˈhaɪə.rɑː.ki/ | Hệ phân cấp |
| Semantic | /sɪˈmæn.tɪk/ | Mang ngữ nghĩa |
| Curriculum | /kəˈrɪk.jə.ləm/ | Chương trình học |
| Outline | /ˈaʊt.laɪn/ | Dàn ý |
| Browser | /ˈbraʊ.zə/ | Trình duyệt |
| Rendering | /ˈren.dər.ɪŋ/ | Quá trình dựng/hiển thị |
| Accessibility | /əkˌses.əˈbɪl.ə.ti/ | Khả năng tiếp cận |

### Conceptual questions — answer before looking for help

These questions synthesize the topic rather than repeating the [workshop's ten questions](./workshops/build-a-curriculum-outline/REVIEW.md#4-six-levels-of-self-assessment-không-kèm-đáp-án). No answer key is included here.

1. **Understand:** Why does wrapping the same text in `<h1>` change its normal visual appearance, even without author-written CSS? Separate **semantics** from **default styling**.
2. **Analyze:** Sketch the DOM relationship among the page's `h1`, `h2`, three `h3` elements and four `p` elements. Which headings are peers? Which heading describes a broader topic?
3. **Evaluate:** Explain what **8/8 local tests passed** guarantees in this repository, and name two important properties it does **not** establish.
4. **Create (extension):** Design an HTML-only outline of a coastal engineering course with a title, subject areas and explanatory paragraphs. Justify every heading level.

**Personal mastery checklist (not independently graded):** I can distinguish a tag from an element; explain `h1`–`h3` and `p`; distinguish HTML/CSS/JavaScript responsibilities; explain browser default styling; and articulate the limits of automated testing.

---

## Future chapters — pending curriculum work

The following are **outlines, not completed notes**. Add supported explanations and evidence as the relevant freeCodeCamp activities are completed.

### Chapter 02 — HTML attributes and boilerplate

Attributes and attribute values; document type, language, head metadata, title and viewport; correct use and common errors.

### Chapter 03 — HTML content, structure and accessibility

Links, image alternatives, lists, semantic landmarks, tables, forms, labels, validation and navigation behavior.

### Chapter 04 — CSS fundamentals

Rules and declarations, selectors, specificity, cascade, inheritance, typography, colors, box model and computed styles.

### Chapter 05 — CSS layout and responsive behavior

Dimensions and units, positioning, Flexbox, Grid, media queries, mobile-first reasoning and overflow analysis.

### Chapter 06 — CSS states and effects

Pseudo-classes, pseudo-elements, custom properties, transitions, transforms and animations, including reduced-motion considerations.

### Chapter 07 — Verification and final synthesis

Browser developer tools, independent validation, keyboard/accessibility testing, responsive visual checks, common failure modes, project comparisons and final course-wide conceptual map.

## Maintenance rule

After each **verified** lesson or project, update its own source and documentation first; then add a concise, evidence-backed concept to this root review. Maintain a distinction among **course content**, **engineering interpretation**, **optional extension** and **unverified assumptions**. Do not convert future topics into completion claims. At the end of the practical curriculum, perform a **full final review** rather than merely changing this document's status line.
