# Responsive Web Design — Cumulative Conceptual Review

> **Status:** In progress — concepts from Workshop 01, Labs 01–02 and Workshop 02 documented.
> **Curriculum:** freeCodeCamp Responsive Web Design V9.
> **Final review:** Not yet complete; future subjects are included only as a learning roadmap.

## Purpose and framework

This is a **cross-lesson technical synthesis**, not a transcription of freeCodeCamp or a duplicate of individual activity notes. Every practical exercise has a dedicated `REVIEW.md` containing terminology with pronunciation, common mistakes and self-assessment questions.

For each topic, ask:

1. **What is it?** What is the purpose of the construct?
2. **What does the browser receive?** What elements, attributes and resources appear in the HTML?
3. **What does the browser do?** How does parsing build a DOM, apply defaults and load resources?
4. **What does the user experience?** What meaning, navigation and content are exposed?
5. **What can fail?** What mistakes could produce incorrect semantics or behavior?
6. **How can it be inspected?** What do source, preview and browser tools establish?

**Scope labels:** *Practiced* = used in a completed exercise; *Explained* = relevant technical interpretation; *Extension* = useful background beyond its instructions; *Planned* = not yet covered by completed practice.

## Learning map

| Part | Subject | Status | Evidence |
| --- | --- | --- | --- |
| 01 | HTML elements, headings and paragraphs | Practiced / explained | [Workshop 01](./workshops/build-a-curriculum-outline/) |
| 02 | Debugging element names and closing syntax | Practiced / explained | [Lab 01](./labs/debug-camperbots-profile-page/) |
| 03 | Images, anchor links and attributes | Practiced / explained | [Lab 02](./labs/debug-pet-adoption-page/) |
| 04 | HTML document, semantic sections, lists, figures, captions and metadata | Practiced / explained | [Workshop 02](./workshops/build-a-cat-photo-app/), **42/42 steps** |
| 05 | Deeper HTML accessibility, tables and forms | Planned | Future curriculum work |
| 06 | CSS foundations, selectors, cascade and box model | Planned | Future curriculum work |
| 07 | Flexbox, Grid, positioning and responsive behavior | Planned | Future curriculum work |
| 08 | Certification projects and cross-browser/accessibility reviews | Planned | Future curriculum work |

---

## Part 01 — HTML structure, headings and paragraphs

### Meaning of HTML

**HTML** (*HyperText Markup Language*) describes the **structure and semantics** of webpage content. It is a markup language, not a replacement for application logic expressed in a programming language such as JavaScript.

Workshop 01 created one `h1`, one `h2`, three sibling `h3` headings and four `p` paragraphs:

| Element | Role in the exercise | Important distinction |
| --- | --- | --- |
| `h1` | Main welcome heading | Represents a heading, not just large typography |
| `h2` | Curriculum heading | Indicates relative section level |
| `h3` | Three parallel subject headings | Same heading level conveys peer topics |
| `p` | Ordinary explanatory prose | Raw text may display but lacks paragraph markup |

**Tag versus element:** in `<h3>Introduction to CSS</h3>`, `<h3>` is the opening tag; `Introduction to CSS` is the text; `</h3>` is the closing tag; the complete structure is an HTML element.

### Browser interpretation

```text
HTML source → HTML parser → DOM element tree
                                 ↓
                        default styles
                                 ↓
                        layout / preview
```

Browsers ordinarily make headings larger and bolder through their default user-agent stylesheets. This visual convention is not the *semantic purpose* of the heading.

**Archive distinction:** Workshop 01's freeCodeCamp editor supplied a fragment. The archived `index.html` adds an HTML document wrapper for direct local browsing. That wrapper is not a claim about curriculum topics taught in Workshop 01. The screenshot's `Javascript`/`javaScript` spelling was preserved as learner output; the conventional name is **JavaScript**.

---

## Part 02 — Debugging HTML syntax and element names

A page can show text despite containing malformed HTML. Lab 01 corrected the following:

| Incorrect source | Intended source | Why it matters |
| --- | --- | --- |
| `<heading2>About</heading2>` | `<h2>About</h2>` | A made-up element name does not become a standard heading |
| `<pp>...</pp>` | `<p>...</p>` | A paragraph uses the `p` element |
| `<h3>...<h3/>` | `<h3>...</h3>` | The closing tag begins with `</` |

HTML parsers apply error-recovery rules, but their ability to construct *some* DOM does not guarantee the author received the intended hierarchy. Mistyped element names can still appear as DOM nodes without acquiring the semantics or default presentation of genuine `h2` and `p` elements.

**Debugging discipline:** read the user stories → compare actual and expected HTML → make minimal corrections → inspect DOM and preview → check official exercise requirements. A visible page is not, by itself, proof of valid semantics or accessibility.

---

## Part 03 — HTML attributes, images and hyperlinks

Lab 02 introduced the distinct roles of `img`, `a`, `src`, `alt` and `href`:

```html
<img src="cats.jpg" alt="Two kittens sleeping">
<a href="/cats">Visit cats page</a>
```

| Construct | Purpose |
| --- | --- |
| `img` | Embed an image |
| `src` | Identify an embedded resource URL |
| `alt` | Supply alternative text for an image |
| `a` | Make a hyperlink when it has a suitable `href` |
| `href` | Identify a link destination |

The original lab used `href` on `img`, `att` instead of `alt`, an incorrect `</img>` and `src` on two anchors. Fixing those five faults restored the intended markup.

### Void element versus an ordinary element

An `img` is a **void element**: it has no child content and must not have a closing `</img>` in HTML. An anchor normally encloses linked content and uses `</a>`.

`alt` is *not just a tooltip*: it supplies a textual alternative, especially important when an image cannot be perceived. **Extension:** purely decorative images can appropriately have empty `alt` in some circumstances.

### URL and route nuance

A CDN image uses an absolute HTTPS URL. `/cats` and `/dogs` are root-relative paths. An anchor can have the correct `href` even when the destination does not exist on an arbitrary local site. Markup correctness and resource availability are separate issues.

---

## Part 04 — Full HTML documents, semantic groups, lists and figures

**Primary evidence:** [Workshop 02 — Build a Cat Photo App](./workshops/build-a-cat-photo-app/), **42/42 steps completed** in freeCodeCamp. Unlike the earlier archived fragments, the complete document shell is supplied in the workshop's final code.

### 1. The document skeleton and metadata

The final source includes:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>CatPhotoApp</title>
  </head>
  <body>...</body>
</html>
```

- `DOCTYPE` asks modern browsers to use standards mode.
- `html` is the root element; `lang="en"` identifies the primary language.
- `head` provides metadata, including `title` and the character encoding declaration.
- `title` is document metadata, not a visible page heading.
- `meta charset="UTF-8"` declares the encoding; `meta` is a void element.
- `body` holds the page's content, including `main` and `footer`.

**Do not conflate:** character encoding (`charset`) with human language (`lang`). **Scope limit:** the completed source does not contain a viewport meta tag, CSS or JavaScript; none should be claimed as implemented here.

### 2. Meaningful groups and heading hierarchy

```text
body
├── main
│   ├── h1 (CatPhotoApp)
│   ├── section (Cat Photos)
│   │   └── h2, paragraphs, links and an image
│   └── section (Cat Lists)
│       └── h2, h3 headings, lists and two figures
└── footer
    └── attribution paragraph with link
```

`main` signals primary page content; `section` groups related content; `footer` identifies final information distinct from the main article. The `h1 → h2 → h3` hierarchy communicates document structure, not only different font sizes.

**Extension:** whether a grouping should use `section`, `article` or a generic container depends on semantic meaning and document context, not decorative layout. This exercise uses `section` explicitly.

### 3. Unordered and ordered list semantics

The section “Things cats love” uses `ul` with three `li` items; “Top 3 things cats hate” uses `ol` with three items. The choice of ordered versus unordered list communicates whether sequence/ranking is part of the content's meaning. CSS can later control appearance without changing list semantics.

### 4. Figures, captions and emphasis

The workshop groups images and captions using `figure` and `figcaption`:

```html
<figure>
  <img src="..." alt="A slice of lasagna on a plate.">
  <figcaption>Cats <em>love</em> lasagna.</figcaption>
</figure>
```

- `figure` represents a self-contained unit of illustration or related content.
- `figcaption` provides a semantic caption for that figure.
- `em` expresses stress emphasis, commonly rendered italic by default.
- `strong` expresses strong importance, seriousness or urgency, commonly rendered bold by default.

**Important:** `em` and `strong` are not just shortcuts for italic or bold presentation.

### 5. A clickable image and new browsing contexts

The image of a relaxing cat sits *inside* an `a` element, so the image functions as linked content. Its `alt` identifies the image; the surrounding anchor's `href` identifies the navigation destination. The text link with `target="_blank"` requests a new browsing context.

**Extension:** new tabs should be used deliberately for usability and accessibility. In modern browsers, `_blank` generally implies `noopener` for links, but deployment requirements and browser support deserve separate consideration. The archived markup is deliberately unchanged from the completed workshop.

### 6. What freeCodeCamp completion does and does not establish

**Verified in supplied screenshots:** all **42/42 steps** were accepted; the page preview displayed headings, embedded photos, two lists, captions and a footer.

**Not independently established:** screen-reader support, cross-browser rendering, destination availability, accessibility conformance, production performance, or responsive design. External images depend on the CDN being reachable.

**Practical browser inspection:** inspect the `head`, `main`, two `section`s, nested lists and `figure` elements in Developer Tools; check the `img` attributes and the anchor `href`/`target` values; inspect which resources are loaded rather than assuming a successful build means all network requests succeeded.

---

## Technical vocabulary — British English IPA

| Term | IPA | Vietnamese |
| --- | --- | --- |
| Markup | /ˈmɑː.kʌp/ | Đánh dấu |
| Element | /ˈel.ɪ.mənt/ | Phần tử |
| Attribute | /ˈæt.rɪ.bjuːt/ | Thuộc tính |
| Heading | /ˈhed.ɪŋ/ | Tiêu đề |
| Paragraph | /ˈpær.ə.ɡrɑːf/ | Đoạn văn |
| Hierarchy | /ˈhaɪə.rɑː.ki/ | Hệ phân cấp |
| Debugging | /ˌdiːˈbʌɡ.ɪŋ/ | Gỡ lỗi |
| Syntax | /ˈsɪn.tæks/ | Cú pháp |
| Semantic | /sɪˈmæn.tɪk/ | Mang ngữ nghĩa |
| Image | /ˈɪm.ɪdʒ/ | Hình ảnh |
| Anchor | /ˈæŋ.kə/ | Liên kết neo |
| Alternative text | /ɒlˈtɜː.nə.tɪv tekst/ | Văn bản thay thế |
| Void element | /vɔɪd ˈel.ɪ.mənt/ | Phần tử rỗng |
| Document | /ˈdɒk.jə.mənt/ | Tài liệu |
| Character encoding | /ˈkær.ək.tə ɪnˈkəʊ.dɪŋ/ | Mã hóa ký tự |
| Section | /ˈsek.ʃən/ | Phần/mục nội dung |
| Unordered list | /ʌnˈɔː.dəd lɪst/ | Danh sách không thứ tự |
| Ordered list | /ˈɔː.dəd lɪst/ | Danh sách có thứ tự |
| Figure | /ˈfɪɡ.ə/ | Hình minh họa |
| Caption | /ˈkæp.ʃən/ | Chú thích |
| Emphasis | /ˈem.fə.sɪs/ | Sự nhấn mạnh |
| Accessibility | /əkˌses.əˈbɪl.ə.ti/ | Khả năng tiếp cận |
| Browser | /ˈbraʊ.zə/ | Trình duyệt |

## Cross-lesson self-assessment — answer independently

1. **Remember:** Explain the difference between an opening tag and an HTML element.
2. **Understand:** Why does `h1` normally appear larger than plain text even without authored CSS?
3. **Analyze:** Why might `<heading2>About</heading2>` display text but not act as an `h2`?
4. **Apply:** Correct `<img href="photo.jpg" att="River mouth"></img>`.
5. **Understand:** How does an `img` element become linked content when placed inside `a`?
6. **Analyze:** An anchor has `href="/stations"` but clicking returns HTTP 404. Does that prove a markup error?
7. **Understand:** Distinguish `lang="en"` from `meta charset="UTF-8"`.
8. **Apply:** Explain when `ul`, `ol` and `li` should be used in a coastal survey procedure versus equipment inventory.
9. **Analyze:** What is the relation between `figure`, `img`, `figcaption`, `em` and `strong`?
10. **Evaluate — extension:** Should an external link always open with `target="_blank"`? Explain your criteria.
11. **Evaluate — extension:** What can a successful freeCodeCamp challenge verify, and which quality dimensions need more evidence?
12. **Create — extension:** Design an HTML-only coastal-monitoring page with a title, two semantic sections, an equipment list, an ordered field procedure, an annotated image and a footer.

Answers are deliberately not supplied. Detailed questions for Workshop 02 are in [its REVIEW.md](./workshops/build-a-cat-photo-app/REVIEW.md).

---

## Future topics — not yet completed

- **More HTML:** forms, labels, input controls, tables, navigation landmarks and deeper accessibility.
- **CSS basics:** rules, selectors, specificity, inheritance, cascade, color, typography and box model.
- **CSS layout:** dimensions, Flexbox, Grid, positioning, overflow, media queries and mobile-first design.
- **Visual behavior:** pseudo-classes, pseudo-elements, CSS custom properties, transitions, transforms and animations.
- **Project quality:** keyboard checks, responsive inspection, cross-browser behavior and certification projects.

**Maintenance principle:** update the individual activity notes and the cumulative review from *completed* work, while separating practiced facts, explanation, optional extensions and future subjects. The learning documents do not need completion dates or auxiliary test scripts.
