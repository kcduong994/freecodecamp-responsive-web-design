# Workshop 09 — Build Quincy's Job Tips Page

> **Curriculum:** [freeCodeCamp — Responsive Web Design V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/)
> **Area:** HTML → Semantic HTML
> **Activity:** [Build Quincy's Job Tips Page](https://www.freecodecamp.org/learn/responsive-web-design-v9/workshop-quincys-job-tips/step-1)
> **Evidence:** The learner supplied the complete final HTML and reported finishing the workshop. A final passing-check screenshot and exact step count were not supplied with this source.
> **Status:** Learner-reported complete; independent freeCodeCamp retest, browser accessibility audit and quotation/source verification not performed.

## Objective / Mục tiêu

Practice semantic HTML (*semantic markup* /sɪˈmæn.tɪk ˈmɑː.kʌp/ — đánh dấu có ngữ nghĩa), especially inline and block quotations and citation metadata, while presenting career advice attributed to Quincy Larson. This workshop is a static HTML document; it has no CSS, JavaScript, account functionality or external media player.

## Source files

- [`index.html`](./index.html) — the complete final source supplied by the learner, preserving the quotation text, markup, attribution and nesting.
- [`README.md`](./README.md) — structure, scope, provenance and verification boundaries.
- [`REVIEW.md`](./REVIEW.md) — conceptual review with British English IPA, common mistakes, debugging and self-assessment.

## Document structure

```text
html[lang=en]
├── head
│   ├── meta[charset=UTF-8]
│   ├── meta[name=viewport]
│   └── title
└── body
    ├── h1 — Quincy's Tips for Getting a Developer Job
    ├── p
    │   └── q[cite=source URL] — inline quotation
    └── main
        ├── section — Envisioning Success
        │   ├── h2
        │   ├── blockquote[cite=source URL]
        │   └── p — attribution with cite element
        ├── section — Importance of Networking
        │   ├── h2
        │   └── blockquote[cite=source URL]
        │       └── four p elements
        └── section — Importance of Building a Reputation
            ├── h2
            └── blockquote[cite=source URL]
                └── three p elements
```

The source contains **one `h1`, one `main`, three `section`, three `h2`, one `q`, three `blockquote`, one `cite` element**, and four `cite` attributes in total (one on `q` and three on `blockquote`). All source citations point to the same freeCodeCamp article URL.

## Semantic concepts practiced

| Construct | Function | Distinction |
| --- | --- | --- |
| `h1`, `h2` | Main heading and subordinate section headings | Heading levels communicate hierarchy, not merely font size |
| `main` | Landmark for primary page content | The learner's introductory `h1` and paragraph sit before `main`; that is the supplied final structure |
| `section` | Named thematic grouping | Three clearly titled sections |
| `q` | Short inline quotation | Browser may add quotation marks automatically |
| `blockquote` | Extended or block-level quotation | Does not itself prove words match an external publication |
| `cite` **attribute** | URL identifying a cited source for `q`/`blockquote` | A source pointer, not a rendered hyperlink or automatic verification |
| `<cite>` **element** | Title of a work | Wraps the book/article title in the attribution paragraph |
| `&mdash;` | HTML character reference for an em dash (—) | Text punctuation, not source metadata |

The `cite` attribute and the `<cite>` element are different constructs. The browser does not automatically show the citation URL or turn it into a clickable reference. Explicitly linking to a source would be a separate design choice.

## Provenance and boundaries

- **Learner-provided material:** all HTML, including the quotation wording, was supplied in the conversation. The archive does not silently paraphrase or independently authenticate the quoted text.
- **Attribution:** the cited URL is `https://www.freecodecamp.org/news/learn-to-code-book/`; the URL in markup is attribution metadata rather than a downloaded resource. Do not infer that the words have been checked verbatim against the published book.
- **Verification:** the nested element structure was checked using an HTML parser while packaging. That is not a substitute for the official freeCodeCamp checker or assistive-technology testing.
- **Accessibility extensions (not claimed completed):** review whether moving the page heading and introduction inside `main` better expresses the page's primary content; evaluate heading/landmark traversal and readable quotation attribution in an actual browser or screen reader. Do not change the archived submission without identifying it as a revised edition.

## Quick local inspection

Open `index.html` directly in a browser. With Developer Tools → Elements, inspect `q[cite]`, each `section > h2`, the three `blockquote[cite]`, and the single `<cite>` element. Compare source and the DOM, then check the official activity separately if required.

Continue to [REVIEW.md](./REVIEW.md) and the cumulative [RWD_REVIEW.md](../../RWD_REVIEW.md).

**Repository convention:** the downloadable installer is a transfer tool only; it is not copied into the Git repository. Do not record completion dates or generated utility code in this workshop folder.
