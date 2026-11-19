# Responsive Web Design — Cumulative Conceptual Review

> **Status:** In progress — Workshops 01–03 and Labs 01–04 documented.
> **Curriculum:** freeCodeCamp Responsive Web Design V9.
> **Final course review:** Not yet complete; future subjects remain a roadmap, not completed practice.

## Purpose and learning framework

This document is a **cross-lesson technical synthesis**, not a transcription of freeCodeCamp. Each finished practical exercise contains its own `REVIEW.md` with deeper explanations, British English IPA and self-assessment questions.

For every concept, ask:

1. **What is it?** What does the construct mean?
2. **What does the browser receive?** Which tags, attributes and resources are present?
3. **What does the browser do?** How does the parser build the DOM and load external resources?
4. **What does the user experience?** What content and structure are exposed?
5. **What can fail?** Which errors cause wrong syntax, semantics or actual behavior?
6. **How can we inspect it?** What do the source, Preview, Elements and Network panels establish?

**Scope labels:** *Practiced* = used in completed coursework; *Explained* = interpretation; *Extension* = material beyond the exercise; *Planned* = future topic.

## Learning map

| Part | Subject | Status | Evidence |
| --- | --- | --- | --- |
| 01 | HTML elements, headings and paragraphs | Practiced / explained | [Workshop 01](./workshops/build-a-curriculum-outline/) |
| 02 | Debugging element names and closing syntax | Practiced / explained | [Lab 01](./labs/debug-camperbots-profile-page/) |
| 03 | Images, anchor links and attributes | Practiced / explained | [Lab 02](./labs/debug-pet-adoption-page/) |
| 04 | Document structure, semantic sections, lists, figures, captions and metadata | Practiced / explained | [Workshop 02](./workshops/build-a-cat-photo-app/), **42/42 steps** |
| 05 | Recipe page: independent user stories, `head`/`body`, ingredient and procedure lists, image behavior | Practiced / explained | [Lab 03](./labs/build-a-recipe-page/), original submission **100%** |
| 06 | Generic `div` containers, repeated classes, unique IDs and grouped buttons | Practiced / explained | [Workshop 03](./workshops/build-a-bookstore-page/), **19/19 steps** |
| 07 | Travel agency: description metadata, package links and image/caption nesting | Practiced / explained | [Lab 04](./labs/build-a-travel-agency-page/), original submission **100%** |
| 08 | Deeper accessibility, tables and forms | Planned | Future curriculum work |
| 09 | CSS foundations, selectors, cascade and box model | Planned | Future curriculum work |
| 10 | Flexbox, Grid, positioning and responsive behavior | Planned | Future curriculum work |
| 11 | Certification projects and cross-browser/accessibility reviews | Planned | Future curriculum work |

---

## Part 01 — HTML structure, headings and paragraphs

### Meaning of HTML

**HTML** (*HyperText Markup Language*) describes the **structure and semantics** of webpage content. It is a markup language, not a replacement for application logic expressed in JavaScript.

Workshop 01 created one `h1`, one `h2`, three sibling `h3` headings and four `p` paragraphs:

| Element | Role in the exercise | Important distinction |
| --- | --- | --- |
| `h1` | Main welcome heading | Represents meaning, not merely a large font |
| `h2` | Curriculum heading | Signals section hierarchy |
| `h3` | Three parallel subject headings | Equal level suggests related peer topics |
| `p` | Ordinary explanatory text | Raw text may render without paragraph semantics |

**Tag versus element:** `<h3>Introduction to CSS</h3>` comprises an opening tag, text and a closing tag. The complete construct is an HTML element.

### Browser interpretation

```text
HTML source → HTML parser → DOM tree
                                 ↓
                     user-agent default styles
                                 ↓
                         layout and preview
```

Browsers ordinarily make headings larger and bolder via default stylesheets, but this is not the semantic purpose of a heading.

**Archive distinction:** the workshop editor supplied an HTML fragment. The repository adds a standalone document wrapper to allow direct browser opening. This addition is not a claim about further official lessons. The learner's spelling `Javascript`/`javaScript` was preserved where it appeared in the completed work; the conventional name is **JavaScript**.

---

## Part 02 — Debugging HTML syntax and element names

Lab 01 corrected:

| Incorrect markup | Intended markup | Lesson |
| --- | --- | --- |
| `<heading2>About</heading2>` | `<h2>About</h2>` | A made-up element does not automatically become a standard heading |
| `<pp>...</pp>` | `<p>...</p>` | Standard paragraph tag is `p` |
| `<h3>...<h3/>` | `<h3>...</h3>` | An HTML closing tag starts with `</` |

Browsers recover from many HTML mistakes, so source may still display text without producing the intended DOM or semantics. An unknown element can exist in the DOM without gaining the role/default styling of `h2` or `p`.

**Debugging sequence:** read requirements → compare expected/actual tags → change the smallest possible source span → inspect DOM and Preview → check the official challenge. Rendering alone is not proof of validity or accessibility.

---

## Part 03 — Images, hyperlinks and attributes

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
| `a` | Create a hyperlink when it has a suitable `href` |
| `href` | Identify a link destination |

The lab starter used `href` on `img`, `att` instead of `alt`, an invalid `</img>` and `src` on two links. Fixing those five faults restored the intended markup.

An `img` is a **void element**, having no content children or closing `</img>` tag. An anchor encloses linked content and closes with `</a>`. Alternative text is not merely a tooltip; it conveys useful information when the image cannot be perceived. **Extension:** some purely decorative images correctly use `alt=""`.

**URL nuance:** an image CDN URL is typically an absolute HTTPS URL. `/cats` and `/dogs` are root-relative. A valid `href` can still point to a missing page—HTML semantics and resource availability are different kinds of correctness.

---

## Part 04 — Complete HTML documents, semantic sections, lists and captions

**Evidence:** [Workshop 02 — Build a Cat Photo App](./workshops/build-a-cat-photo-app/) completed **42/42** steps. Unlike the older archived fragments, the complete document shell was included in this workshop's submitted source.

### 1. HTML skeleton and metadata

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

- The doctype requests standards mode.
- The `html` element is the root and `lang="en"` identifies the primary document language.
- The `head` contains metadata, including `title` and character encoding.
- The `title` is **not** the visible page heading.
- `meta charset="UTF-8"` declares character encoding; `meta` is a void element.
- The `body` contains page content.

**Do not confuse** human language (`lang`) with character encoding (`charset`). No authored CSS, JavaScript or viewport meta element was used in this particular completed workshop.

### 2. Semantic groups and heading hierarchy

```text
body
├── main
│   ├── h1 (CatPhotoApp)
│   ├── section (Cat Photos)
│   │   └── h2, paragraphs, links and an image
│   └── section (Cat Lists)
│       └── h2, h3 headings, lists and two figures
└── footer
    └── attribution paragraph with a link
```

`main` signals primary content, `section` groups related topics and `footer` identifies supplementary final information. Heading level reflects hierarchy, not desired font size. **Extension:** when to use `section`, `article` or a generic container depends on their actual semantic role.

### 3. Unordered versus ordered lists

“Things cats love” uses `ul` with three items; “Top 3 things cats hate” uses `ol` with three items. Unordered lists convey collections; ordered lists convey sequence or ranking. Browser presentation can later change with CSS, independently of the underlying semantics.

### 4. Figure, caption and textual emphasis

```html
<figure>
  <img src="..." alt="A slice of lasagna on a plate.">
  <figcaption>Cats <em>love</em> lasagna.</figcaption>
</figure>
```

`figure` represents a self-contained illustration or supporting unit; `figcaption` supplies its caption. `em` indicates stress emphasis; `strong` expresses importance, seriousness or urgency. Default italic/bold styling does not exhaust their meaning.

### 5. Clickable images and external navigation

A relaxing-cat `img` sits inside an `a`, making the image linked content. The `alt` describes the image; the containing anchor's `href` identifies the destination. Another link uses `target="_blank"` to request a new browsing context. **Extension:** use new-tab navigation deliberately; its security and usability implications merit consideration beyond this exercise.

### 6. Verification boundaries

The learner's screenshots showed **42/42** accepted steps and a page Preview with photos, lists, captions and footer. This does not independently establish accessibility conformance, cross-browser layout, live deployment, source availability of every external asset or production performance.

---

## Part 05 — Independent Recipe Page Lab: structure, sequence and real image loading

**Evidence:** [Lab 03 — Build a Recipe Page](./labs/build-a-recipe-page/) was accepted by freeCodeCamp at **100%** using the learner's original Fish Recipe code. The learner also supplied a Preview showing a broken image despite passing the tests. The archived `index.html` is a **lightly polished local edition**, and that revised edition has **not** been independently re-submitted to freeCodeCamp.

### 1. From a user story to actual HTML

Lab 03 did not lead the learner step-by-step. It required selecting an appropriate collection of elements and assigning them the proper hierarchy. The page's user stories specify a valid HTML5 document, a visible recipe title, an introduction, ingredient and cooking sections, lists with at least four items each, and an image with `src` and `alt`.

This is a transition from **following instructions** to **implementing requirements**:

| Requirement | HTML representation | What it conveys |
| --- | --- | --- |
| Recipe identity | `title` and `h1` | Browser/tab identity vs visible main heading |
| Introduction | `p` | Introductory prose |
| Ingredients | `h2` + `ul > li` | A collection of ingredients |
| Instructions | `h2` + `ol > li` | An ordered procedure |
| Illustration | `img` with `src`, `alt` | External visual content with a textual alternative |

### 2. `head` and `body` are siblings

The learner initially wrote `<body><head>...</head></body>` and received failed checks for elements that appeared to be present. The corrected structure is:

```html
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Fish Recipe</title>
  </head>
  <body>
    <h1>Fish Recipe</h1>
  </body>
</html>
```

The `head` does not belong inside the `body`. Browsers use HTML parsing and error recovery; a tag's textual presence does not guarantee it becomes the intended DOM node in the intended location. A tester may check structure, not mere substring presence.

This reinforces the earlier lessons: **DOM is what the browser constructs, not necessarily exactly the tree the author imagined from the source text**.

### 3. Why ingredient lists differ from cooking procedures

A recipe typically has two forms of organization:

- `ul` for ingredients: the items usually form a set, not an ordered operation.
- `ol` for cooking steps: the order typically affects the result.

The `li` items are children of their associated list container, not independent paragraphs. CSS may alter marker appearance later, without changing these semantics.

### 4. A passing source test is not a successful asset request

The original solution included `<img src="abcd.com/fish.jpg" alt="that is fish">` and still passed the exercise checks. The screenshot showed a **broken image icon** and displayed the alternative text. Without a scheme and valid available local file, `abcd.com/fish.jpg` is a relative path; the browser cannot be assumed to retrieve a photo from the domain `abcd.com`.

The locally polished archive uses an externally hosted Wikimedia Commons fish photo and more descriptive `alt` text. Its source/licensing information is recorded in [Lab 03 README](./labs/build-a-recipe-page/README.md). Whether the image is retrievable on the learner's browser must be verified separately.

**Practical distinction:**

```text
HTML elements present and well arranged
              ≠
External image URL resolves and transfers successfully
              ≠
Full accessibility and cross-browser acceptance
```

Diagnose with **Developer Tools → Network** for image status/URL/content type and **Elements** for the actual DOM attributes. This is a useful lesson in not overclaiming automated checks.

### 5. Content quality beyond exact element counts

Four instructions named `cook1`, `cook2`, `cook3`, `cook4` can meet a minimum list length but do not constitute a useful recipe. The edited archive replaces placeholders with meaningful sequential actions and makes ingredients consistent with those actions.

**Engineering lesson:** passing acceptance checks is necessary for the exercise, but a quality page must also communicate real information accurately and intelligibly. The coursework remains an HTML fundamentals task, not proof of a culinary, safety or professional content review.

### 6. Bridge to future CSS

Without custom CSS, the browser's default styles already present `h1`/`h2`, bullet and numbered markers, and images. In later CSS lessons, layout and appearance may change, but **HTML semantics must remain correct**. This separation is the foundation for responsive web design.

---

## Part 06 — Bookstore Workshop: `div`, `class`, `id`, grouping and buttons

**Evidence:** [Workshop 03 — Build a Bookstore Page](./workshops/build-a-bookstore-page/) was accepted by freeCodeCamp at **19/19 steps (100%)**, according to the learner's final screenshot. The archived `index.html` preserves the learner's source content and structure, with only whitespace normalization.

### 1. The next structural idea: grouping beyond headings and lists

The page uses `<div class="card-container">` to contain **two** `<div class="card">` children. Each child has a unique `id`, a book-title `h2`, a descriptive paragraph and a `button` labeled "Buy Now". A second `<div class="btn-container">` groups "View Cart" and "Checkout".

The `div` element has **no intrinsic book, product or commerce semantics**. Its purpose here is neutral grouping. The words `card` and `btn-container` are human-authored class values, not built-in browser layout features.

### 2. Different roles for `class` and `id`

| Source | Actual purpose | Reuse expectation |
| --- | --- | --- |
| `class="card"` | Identifies both book-card elements as a group | Shared on multiple elements |
| `class="btn"` | Groups all four buttons | Shared on multiple elements |
| `id="sally-adventure-book"` | Distinguishes Sally's book | Unique per document |
| `id="dave-cooking-book"` | Distinguishes Dave's book | Unique per document |
| `id="view-cart-btn"` | Distinguishes the cart button | Unique per document |
| `id="checkout-btn"` | Distinguishes the checkout button | Unique per document |

A class may contain several whitespace-separated tokens. An ID is intended to identify exactly one element. A future CSS selector `.btn` targets the class, while `#checkout-btn` targets the ID. These selectors are **extensions**, because the submitted workshop contains no CSS.

### 3. Nested DOM structure determines ownership

The two book cards are siblings inside `.card-container`, **not** nested inside each other. Their `h2`, `p` and `button` descendants belong to the relevant card. The final two buttons are in `.btn-container`, outside both book cards. This distinction matters for source reading order, future CSS selectors and event handling.

The page's only `h1` labels the bookstore; each `h2` identifies a book title. A generic wrapper does not replace heading semantics. Inspect the DOM tree rather than inferring structure from indentation alone.

### 4. A clickable element is not a working business feature

A native `button` is keyboard-focusable and has an accessible text label by default. However, the four buttons have **no click logic** in the submitted HTML. `Buy Now`, `View Cart` and `Checkout` are labels, not evidence of working purchases, cart state or payment processing. This reinforces the Lab 03 lesson: **passing a source checker does not prove that an external or interactive feature actually works**.

### 5. Relation to earlier tasks and future CSS

- **Workshop 01:** headings and paragraphs organize text; Workshop 03 groups repeated text into larger components.
- **Lab 01:** malformed closing tags can change the DOM hierarchy and misplace a book into another card.
- **Lab 02:** `class` and `id` are attributes like `src` and `href`, but have different meaning.
- **Workshop 02:** `section`/`main` convey semantics, while `div` provides neutral grouping.
- **Lab 03:** `ul`/`ol` express list meaning, while `div` does not automatically create a list.
- **Future CSS/JavaScript:** class/ID selectors can target elements, and event handlers may add behavior; neither is implemented in this workshop.

**Checks still needed outside freeCodeCamp:** independent browser re-open, keyboard Tab order, responsive inspection and accessibility audit. A passing 19/19 screenshot is evidence for this workshop's acceptance tests only.

For British English IPA, detailed diagnostic examples and 20 unanswered questions, see [Workshop 03 REVIEW](./workshops/build-a-bookstore-page/REVIEW.md).

---

## Part 07 — Travel Agency Lab: metadata, package links and linked figures

**Evidence:** The learner's **original** [Lab 04 — Build a Travel Agency Page](./labs/build-a-travel-agency-page/) passed the freeCodeCamp checker at **100%**, while the Preview showed broken images because the three `img` elements used empty `src` values. The repository archives a **polished version** with source improvements and three working freeCodeCamp CDN URLs; it has **not** been re-submitted to freeCodeCamp.

### 1. New metadata: page description and character encoding serve different roles

Lab 04 required both `<meta charset="UTF-8">` and a separate `<meta name="description" content="...">` inside `head`. The first describes encoding; the second supplies an optional page summary to consumers such as search engines. The `title` is distinct from the on-page `h1` and must meet the lab's specified text.

The description alone is neither a visible paragraph nor proof of search rankings, accessibility or SEO performance. This exercise establishes the **HTML structure** only.

### 2. `ul > li > a`: list structure before link behavior

The two package choices are direct `li` children of `ul`, each with a nested anchor containing exact text **Group Travels** and **Private Tours**. The learner's earlier malformed `<a <li>` attempt made both list structure and link requirements fail; correcting the actual DOM hierarchy resolved the root cause. For this lab, each of the two links must point to `https://www.freecodecamp.org/learn` and use `target="_blank"`.

### 3. `figure > a > img` and sibling `figcaption`

Each itinerary figure has two direct children: the first is `a` containing `img`, and the second is `figcaption` containing visible text. The original attempt used `text="1"` as though it were visible content, but HTML caption text belongs **between** opening and closing tags. A caption inside the anchor does not meet this challenge's required nesting.

| Construct | Question answered | Consequence |
| --- | --- | --- |
| `href` | Where does this anchor navigate? | Can be a valid link even when an image is broken |
| `target="_blank"` | Where should navigation open? | Usually opens a new tab; usability needs independent consideration |
| `src` | What image should the browser fetch? | Empty or missing resources may show broken-image placeholders |
| `alt` | What textual alternative conveys the image? | Should describe meaningful visual content, not `img1` |
| `figcaption` | What visible text accompanies the figure? | Does not replace the image's `alt` requirement |

### 4. Acceptance tests versus real resource requests

The screenshot establishes the original lab's **100% checker result**, not working image downloads. In the polished edition, empty `src` values were replaced with the course's images of the Colosseum, the Alps and the sea, and placeholder captions were replaced with descriptions. These changes were reviewed structurally but were not tested through a new freeCodeCamp submission. Use the browser's **Elements** and **Network** panels to separate source structure from actual resource delivery.

### 5. Relationships to earlier material

- **Lab 02:** the image `src` and anchor `href` attributes are different, even when an image itself is clickable.
- **Workshop 02:** `figure`, `figcaption` and `target="_blank"` become combined requirements rather than individually guided steps.
- **Lab 03:** a passing source check can coexist with failed external resources.
- **Workshop 03:** a generic `div` is neutral grouping; `figure` and `ul` express more specific meaning.
- **Future work:** richer accessible link naming, keyboard review, verified image availability, responsive image sizing, actual itinerary navigation and booking interactions remain extensions.

For British English IPA, eight diagnostic cases and 24 unanswered questions, see [Lab 04 REVIEW](./labs/build-a-travel-agency-page/REVIEW.md).

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
| Semantic | /sɪˈmæn.tɪk/ | Ngữ nghĩa |
| Image | /ˈɪm.ɪdʒ/ | Hình ảnh |
| Anchor | /ˈæŋ.kə/ | Phần tử neo/liên kết |
| Alternative text | /ɒlˈtɜː.nə.tɪv tekst/ | Văn bản thay thế |
| Void element | /vɔɪd ˈel.ɪ.mənt/ | Phần tử rỗng |
| Document | /ˈdɒk.jə.mənt/ | Tài liệu |
| Character encoding | /ˈkær.ək.tə ɪnˈkəʊ.dɪŋ/ | Mã hóa ký tự |
| Section | /ˈsek.ʃən/ | Mục/phần nội dung |
| Unordered list | /ʌnˈɔː.dəd lɪst/ | Danh sách không thứ tự |
| Ordered list | /ˈɔː.dəd lɪst/ | Danh sách theo thứ tự |
| Figure | /ˈfɪɡ.ə/ | Hình minh họa |
| Caption | /ˈkæp.ʃən/ | Chú thích |
| Emphasis | /ˈem.fə.sɪs/ | Sự nhấn mạnh |
| Recipe | /ˈres.ɪ.pi/ | Công thức nấu ăn |
| Ingredient | /ɪnˈɡriː.di.ənt/ | Nguyên liệu |
| Instruction | /ɪnˈstrʌk.ʃən/ | Hướng dẫn |
| Sequence | /ˈsiː.kwəns/ | Trình tự |
| Accessibility | /əkˌses.əˈbɪl.ə.ti/ | Khả năng tiếp cận |
| Browser | /ˈbraʊ.zə/ | Trình duyệt |
| Bookstore | /ˈbʊk.stɔː/ | Cửa hàng sách |
| Container | /kənˈteɪ.nə/ | Vùng chứa |
| Card | /kɑːd/ | Thẻ nội dung |
| Class | /klɑːs/ | Nhóm/lớp |
| Identifier | /aɪˈden.tɪ.faɪ.ə/ | Định danh |
| Button | /ˈbʌt.ən/ | Nút bấm |
| Checkout | /ˈtʃek.aʊt/ | Thanh toán |
| Travel agency | /ˈtræv.əl ˈeɪ.dʒən.si/ | Công ty du lịch |
| Destination | /ˌdes.tɪˈneɪ.ʃən/ | Điểm đến |
| Itinerary | /aɪˈtɪn.ə.rər.i/ | Lịch trình |
| Package | /ˈpæk.ɪdʒ/ | Gói du lịch |
| Metadata | /ˈmet.əˌdeɪ.tə/ | Siêu dữ liệu |
| Description | /dɪˈskrɪp.ʃən/ | Mô tả |

## Cross-lesson self-assessment — answer independently

1. **Remember:** Explain the difference between an opening tag and an HTML element.
2. **Understand:** Why does a heading appear bold/larger than raw text without authored CSS?
3. **Analyze:** Why might `<heading2>About</heading2>` render but not behave semantically like `h2`?
4. **Apply:** Correct `<img href="photo.jpg" att="River mouth"></img>`.
5. **Understand:** How does an `img` become a clickable image when nested within `a`?
6. **Analyze:** An anchor has `href="/stations"` but returns HTTP 404. Is the HTML necessarily wrong?
7. **Understand:** Distinguish `lang="en"` from `meta charset="UTF-8"`.
8. **Apply:** Explain when `ul`, `ol` and `li` should be used in a coastal survey procedure vs an equipment inventory.
9. **Analyze:** Explain the relationship between `figure`, `img`, `figcaption`, `em` and `strong`.
10. **Evaluate — extension:** Is `target="_blank"` appropriate for every external link? Why or why not?
11. **Analyze:** Why does `<body><head>...</head></body>` create unexpected freeCodeCamp structural failures?
12. **Evaluate:** Why could the original recipe receive **100%** while its fish image was broken?
13. **Create:** Design a short HTML-only engineering procedure with an inventory, ordered steps, source-attributed image and descriptive `alt`.
14. **Evaluate — extension:** Which observations would you need to make before claiming a page is accessible and cross-browser compatible?
15. **Understand:** Why may both bookstore cards have `class="card"`, but not the same `id`?
16. **Analyze:** What relationships in the DOM would change if the first book card were missing its closing `</div>`?
17. **Evaluate:** Why is a `button` labeled "Checkout" not evidence of a working purchase flow?
18. **Apply:** Design a third card that retains the shared `card` class but has its own ID and heading.
19. **Compare:** When should a page use `div`, `section`, `article`, `ul` or `ol` rather than treating them as interchangeable?
20. **Evaluate — extension:** How would you verify correct keyboard focus order in an unstyled bookstore page?
21. **Apply:** Why must the two package choices be `li > a` rather than `a > li`?
22. **Analyze:** What exact child-order relationship must each itinerary `figure` satisfy?
23. **Evaluate:** Why could the original Travel Agency Page pass at 100% while all three images appeared broken?
24. **Understand:** What is the difference between `meta name="description"` and an introductory `p` paragraph?
25. **Create:** Describe three itinerary images with meaningful `alt` and `figcaption` text, avoiding redundant placeholders.

Answers are intentionally not supplied. Exercise-specific questions are preserved in each activity's `REVIEW.md`, including [Lab 03 REVIEW](./labs/build-a-recipe-page/REVIEW.md), [Workshop 03 REVIEW](./workshops/build-a-bookstore-page/REVIEW.md) and [Lab 04 REVIEW](./labs/build-a-travel-agency-page/REVIEW.md).

---

## Future topics — not yet completed

- **Further HTML:** form controls, labels, validation, tables, navigation landmarks and accessibility.
- **CSS basics:** rules, selectors, specificity, inheritance, cascade, color, typography and the box model.
- **CSS layout:** dimensions, Flexbox, Grid, positioning, overflow, media queries and mobile-first design.
- **Visual behavior:** pseudo-classes, pseudo-elements, CSS variables, transitions, transforms and animations.
- **Project quality:** keyboard checks, responsive inspection, cross-browser behavior and certification projects.

**Maintenance:** keep the cumulative review grounded in completed work, separating what was practiced, technically explained, introduced as an extension and not yet studied. Do not add completion dates, Python tests or repository-update scripts.
