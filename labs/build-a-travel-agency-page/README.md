# Lab 04 — Build a Travel Agency Page

> **Course:** [freeCodeCamp — Responsive Web Design V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/) → Basic HTML  
> **Type:** Independent lab  
> **Status:** Learner's original submission passed freeCodeCamp at **100%**. The archived edition below contains improvements and has **not** been resubmitted to the official checker.  
> **Activity:** [Build a Travel Agency Page](https://www.freecodecamp.org/learn/responsive-web-design-v9/lab-travel-agency-page/build-a-travel-agency-page)

## Objective

Build an HTML-only travel agency page from a blank editor. Translate the freeCodeCamp user stories into a valid document, introduce two travel packages, and present three itinerary illustrations with meaningful links and captions. The exercise deliberately focuses on **structure and HTML semantics**, not CSS styling, booking features, or JavaScript.

## Original submission versus polished archive

The learner's submitted source achieved **100%** in the official freeCodeCamp checker, as shown in the completion screenshot. Nevertheless, its three images had empty `src` attributes and rendered as broken images in Preview. A successful source-code check and a successfully loaded external image are different forms of evidence.

| Aspect | Learner's passing submission | Archived edition in `index.html` |
| --- | --- | --- |
| Document title | `Trave Origin` | `Travel Agency Page`, matching the stated lab title |
| Main heading | `Travel Destinations` | Preserved |
| Introductory paragraphs | Repeated placeholder text | More informative travel/package descriptions |
| Packages | Two list items with correct `a` attributes | Same labels and required links, neatly formatted |
| Itinerary images | Three empty `src` values | Three image URLs supplied by the freeCodeCamp instructions |
| Image alternative text | `img1`, `img2`, `img3` | Short visual descriptions specific to each image |
| Captions | `1`, `2`, `3` | Descriptive itinerary captions |
| Number of anchors | Five | Preserved: exactly five links to the mandated course URL |

**Evidence boundary:** The learner's original code passed the official checker; the improved archive has been checked structurally for this package, but its altered content has not been independently accepted by freeCodeCamp. The three external image URLs were viewed as reachable during package preparation; their availability in any future browser session cannot be guaranteed.

## Required page structure

```text
html[lang=en]
├── head
│   ├── meta[charset=UTF-8]
│   ├── meta[name=description][content=...]
│   └── title — Travel Agency Page
└── body
    ├── h1 — Travel Destinations
    ├── p — Introduction
    ├── h2 — Packages
    ├── p — Package introduction
    ├── ul
    │   ├── li > a — Group Travels
    │   └── li > a — Private Tours
    ├── h2 — Top Itineraries
    ├── figure > a > img + figcaption — Rome
    ├── figure > a > img + figcaption — Alps
    └── figure > a > img + figcaption — Sea
```

For **each** `figure`, the link `a` is the first direct child and contains `img`; `figcaption` is the second direct child and contains visible text. This hierarchy matters because the lab's user stories inspect nesting, not merely whether the output looks plausible.

## Acceptance criteria recorded from the exercise

1. Correct doctype, `html lang="en"`, `head`, `body`, `meta charset="utf-8"` and `title` text `Travel Agency Page`.
2. A non-empty `<meta name="description" content="...">` in `head`.
3. Exactly one `h1`, followed by an introductory paragraph.
4. A `Packages` `h2` followed by a package paragraph and `ul` containing **exactly two** `li` elements.
5. The two list item anchors contain the exact text **Group Travels** and **Private Tours**.
6. A second `h2` with exact text **Top Itineraries**.
7. At least three `figure` elements, each with `a > img` as the first child and a nonempty `figcaption` as the second.
8. Every image has a nonempty, meaningful `src` and `alt`.
9. All five anchors use `href="https://www.freecodecamp.org/learn"` and `target="_blank"`.

The common URL is a **lab-specific requirement**; it is not a real booking destination. Links and images are HTML primitives here, not a working travel reservation application.

## Image sources and local preview

The images are hosted on the freeCodeCamp CDN, which requires internet access:

- Rome / Colosseum: https://cdn.freecodecamp.org/curriculum/labs/colosseo.jpg
- Alps: https://cdn.freecodecamp.org/curriculum/labs/alps.jpg
- Sea: https://cdn.freecodecamp.org/curriculum/labs/sea.jpg

Open [`index.html`](./index.html) directly in a browser. No build step or package manager is needed. In **Developer Tools → Elements**, inspect the document tree; in **Network**, inspect HTTP status and response if any image fails. Inspect link destinations and `target` attributes before clicking. A broken image means resource resolution failed, which does not always make the HTML syntax invalid.

## What was learned

- The distinction between structural acceptance, visual rendering and resource availability.
- The meaning and placement of `meta charset`, `meta name="description"`, and a meaningful `title`.
- `ul > li > a` for the package links; `figure > a > img` with a sibling `figcaption` for itinerary illustrations.
- `href` versus `src`, visual `figcaption` versus alternative text `alt`, and exact `target="_blank"` requirements.
- Why malformed fragments such as `<a <li>`, `<a/>` or `<figcaption text="1">` can break nesting or produce empty captions.
- Why one passing checker should not be mistaken for a complete accessibility or production readiness audit.

For detailed explanations, British English IPA, debugging scenarios and self-assessment questions, read [REVIEW.md](./REVIEW.md).

## Verification and limits

- **Official checker:** learner's original submission accepted, **100%**, evidenced by screenshot.
- **Archived HTML:** structure checked locally using an HTML parser and explicit assertions for link counts, attributes, nesting, headings and nonempty image/caption content.
- **External resources:** URL availability depends on the freeCodeCamp CDN and network access.
- **Not claimed:** official resubmission of this polished edition, automated browser/accessibility audit, SEO ranking, or functioning travel bookings.

Repository policy: keep only `index.html`, `README.md` and `REVIEW.md` for this lab; do not add completion dates, Python test files or repository-update scripts.
