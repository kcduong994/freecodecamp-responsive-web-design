# Workshop 08 — Build a List of Major Web Browsers

> **Curriculum:** [freeCodeCamp — Responsive Web Design V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/)
> **Area:** HTML → Basic HTML
> **Activity:** [Build a List of Major Web Browsers](https://www.freecodecamp.org/learn/responsive-web-design-v9/workshop-major-browsers-list/step-1)
> **Evidence:** Learner screenshot of Step 7 shows **7/7 steps (100% complete)** and **“Congratulations. Your code passes.”**
> **Status:** Completed in freeCodeCamp; independent cross-browser and accessibility testing not performed.

## Objective / Mục tiêu

Use an HTML **description list** (*description list* /dɪˈskrɪp.ʃən lɪst/ — danh sách mô tả) to associate five browser names with short descriptions. The workshop teaches structural and semantic HTML; it does not implement a browser, search function or application logic.

## Source files

- [`index.html`](./index.html) — complete standalone HTML source, preserving the learner's wording and semantic structure.
- [`README.md`](./README.md) — overview, structural inventory and verification limits.
- [`REVIEW.md`](./REVIEW.md) — detailed conceptual review, British English pronunciation and self-assessment.

## What the submitted page contains

```text
html[lang=en]
├── head
│   ├── meta[charset=UTF-8]
│   ├── meta[name=viewport]
│   └── title
└── body
    ├── h1 — List of Major Web Browsers
    └── dl
        ├── dt — Google Chrome
        ├── dd — description
        ├── dt — Firefox
        ├── dd — description
        ├── dt — Safari
        ├── dd — description
        ├── dt — Brave
        ├── dd — description
        ├── dt — Arc
        └── dd — description
```

The page includes exactly **one `h1`**, **one `dl`**, **five `dt`** elements and **five `dd`** elements, with each description immediately following the browser name it explains.

| HTML construct | Meaning | Example in this workshop |
| --- | --- | --- |
| `dl` | Description/association list | Wraps all five browser entries |
| `dt` | Term or name | `Google Chrome` |
| `dd` | Description or value | Its text explanation |
| `h1` | Primary document heading | `List of Major Web Browsers` |
| `title` | Browser-tab/document title | `List of Browsers and Descriptions` |
| `lang="en"` | Document language | English content |
| `meta charset="UTF-8"` | Character encoding | UTF-8 |
| `meta name="viewport"` | Viewport scaling hint | Initial scale 1.0 |

## Important learning points

1. **`dl` is not `ul` or `ol`.** An unordered list groups individual items with `li`; an ordered list expresses sequence; a description list associates terms and explanations.
2. **`dt` and `dd` are separate sibling elements.** Do not wrap each pair inside a `li`, and do not assume `dd` is a child of `dt`.
3. **Content versus formatting:** Browsers commonly indent the `dd` descriptions through user-agent CSS. The HTML itself supplies the semantic relationship; no custom CSS was written.
4. **`head` versus `body`:** The `title`, charset and viewport metadata belong in `head`; the visible heading and list belong in `body`.
5. **Factual scope:** The descriptions and release years are reproduced from the learner's final workshop code, not independently researched historical claims or a ranking of current browsers.

## Verification and limitations

- **Official exercise:** Step 7 screenshot demonstrates the freeCodeCamp checker accepted the original submission at **100%**.
- **Source archive:** The learner's HTML has only been normalized for indentation, blank lines and line endings; the browser descriptions have not been rewritten.
- **Local inspection:** Open `index.html` in a browser and inspect `body > dl > dt/dd` using Developer Tools → Elements. No build step or external assets are needed.
- **Not claimed:** Full cross-browser rendering tests, screen-reader evaluation, responsive QA, external historical-source verification or production deployment.

## Connected learning

Earlier lessons used `ul > li` for unordered lists and `ol > li` for sequences. Workshop 08 adds **term–description associations** without changing the basic document structure. This pattern can later document abbreviations, measurement terms, GIS layers or hydrodynamic parameters, provided their units and values are correct.

Continue with the [activity review](./REVIEW.md) and [cumulative review](../../RWD_REVIEW.md).

**Repository convention:** no completion dates or generated utility scripts are committed; installation tooling is only part of the downloadable transfer package.
