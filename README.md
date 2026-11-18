# freeCodeCamp — Responsive Web Design

> **Curriculum:** [Responsive Web Design Certification V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/)
> **Status:** In progress
> **Current track:** HTML → Basic HTML
> **Learning approach:** Study → Practice → Explain → Review → Advance

## Purpose

This repository is a structured record of my work through freeCodeCamp's **Responsive Web Design V9** curriculum. It preserves the HTML/CSS source created in workshops, labs and certification projects, together with technical explanations and self-assessment material.

The goal is to understand how HTML and CSS work—not simply to pass tests: connect source code to document structure, browser interpretation, user experience, accessibility and engineering practice. Longer-term applications include coastal engineering, scientific communication, environmental data presentation and engineering web interfaces.

This repository is distinct from my Back-End Development and APIs coursework.

## Learning method

Follow the official curriculum in order:

1. **Theory** — study each concept on freeCodeCamp; no separate source file is required for every theory page.
2. **Workshop** — follow the guided steps; archive the completed HTML and the concepts learned.
3. **Lab** — independently implement or debug the user stories; preserve the final source and reasoning.
4. **Review** — explain mechanisms, typical errors and manual checks; answer questions from recall to independent design.
5. **Certification projects** — complete the required projects and verify their acceptance criteria before recording completion.
6. **Final synthesis** — critically revise the cumulative [RWD_REVIEW.md](./RWD_REVIEW.md) after practical coursework.

The repository emphasizes **HTML/CSS source and documentation**, not auxiliary scripts or generated artifacts. Use the freeCodeCamp checker, browser preview and Developer Tools, while recognizing what each actually verifies.

## Learning progress

| Area | Progress | Notes |
| --- | ---: | --- |
| Workshops | **3 completed** | Build a Curriculum Outline (**11/11**); Build a Cat Photo App (**42/42**); Build a Bookstore Page (**19/19**) |
| Labs | **3 completed** | Debug Camperbot's Profile Page; Debug a Pet Adoption Page; Build a Recipe Page |
| Certification projects | **0 / 5** | Not started |
| Cumulative review | **In progress** | [RWD_REVIEW.md](./RWD_REVIEW.md) synthesizes six practical activities |
| Final course review | Not complete | Revisit after practical work |
| Certification exam | Not attempted | Awaiting required coursework |
| Certificate | Not issued | Record only when earned |

### Completed activities

| # | Type | Activity | Core concepts | Source |
| ---: | --- | --- | --- | --- |
| 01 | Workshop | Build a Curriculum Outline | HTML elements, `h1`–`h3`, `p`, heading hierarchy | [Open](./workshops/build-a-curriculum-outline/) |
| 02 | Lab | Debug Camperbot's Profile Page | Correct tag names and closing syntax; browser error recovery | [Open](./labs/debug-camperbots-profile-page/) |
| 03 | Lab | Debug a Pet Adoption Page | `img`, `a`, `src`, `alt`, `href`, void elements | [Open](./labs/debug-pet-adoption-page/) |
| 04 | Workshop | Build a Cat Photo App | Full document; `head`, `main`, `section`, `footer`; lists; figures/captions; emphasis; charset | [Open](./workshops/build-a-cat-photo-app/) |
| 05 | Lab | **Build a Recipe Page** | HTML document hierarchy; translating user stories to code; `ul` vs `ol`; image loading vs code checks | [Open](./labs/build-a-recipe-page/) |
| 06 | Workshop | **Build a Bookstore Page** | Generic `div` grouping; `class` reuse, unique `id`; nested book cards; native buttons vs application behavior | [Open](./workshops/build-a-bookstore-page/) |

**Evidence boundaries:** the learner's freeCodeCamp screenshots confirm the activities, including Workshop 02 (**42/42**) and the **original Recipe Page submission at 100%**, plus Workshop 03 **19/19 (100%)**. The archived Recipe Page source is a lightly **revised edition**; its image and edited content have not been independently re-tested in freeCodeCamp or in the learner's browser. Code-check success does not establish cross-browser compliance, accessible behavior or resource availability.

## Repository structure

```text
freecodecamp-responsive-web-design/
├── README.md
├── RWD_REVIEW.md
├── .gitignore
├── workshops/
│   ├── build-a-curriculum-outline/
│   │   ├── index.html
│   │   ├── README.md
│   │   └── REVIEW.md
│   ├── build-a-cat-photo-app/
│   │   ├── index.html
│   │   ├── README.md
│   │   └── REVIEW.md
│   └── build-a-bookstore-page/
│       ├── index.html
│       ├── README.md
│       └── REVIEW.md
├── labs/
│   ├── debug-camperbots-profile-page/
│   │   ├── index.html
│   │   ├── README.md
│   │   └── REVIEW.md
│   ├── debug-pet-adoption-page/
│   │   ├── index.html
│   │   ├── README.md
│   │   └── REVIEW.md
│   └── build-a-recipe-page/
│       ├── index.html
│       ├── README.md
│       └── REVIEW.md
└── certification-projects/
    └── .gitkeep
```

The `.gitkeep` file is a placeholder, **not** a completed certification project.

## Documentation guide

Each practical activity contains exactly three learning artifacts:

- **`index.html`** — browser-openable HTML source, without a build step.
- **`README.md`** — purpose, source structure, learning record, external assets and verification limits.
- **`REVIEW.md`** — concepts, British English IPA, pitfalls and unanswered self-assessment questions.

The cumulative [RWD_REVIEW.md](./RWD_REVIEW.md) links concepts across lessons, distinguishing completed practice, background explanations and future topics.

### Quick activity links

| Activity | Source | Notes | Review |
| --- | --- | --- | --- |
| Curriculum Outline | [HTML](./workshops/build-a-curriculum-outline/index.html) | [README](./workshops/build-a-curriculum-outline/README.md) | [REVIEW](./workshops/build-a-curriculum-outline/REVIEW.md) |
| Camperbot Profile | [HTML](./labs/debug-camperbots-profile-page/index.html) | [README](./labs/debug-camperbots-profile-page/README.md) | [REVIEW](./labs/debug-camperbots-profile-page/REVIEW.md) |
| Pet Adoption | [HTML](./labs/debug-pet-adoption-page/index.html) | [README](./labs/debug-pet-adoption-page/README.md) | [REVIEW](./labs/debug-pet-adoption-page/REVIEW.md) |
| Cat Photo App | [HTML](./workshops/build-a-cat-photo-app/index.html) | [README](./workshops/build-a-cat-photo-app/README.md) | [REVIEW](./workshops/build-a-cat-photo-app/REVIEW.md) |
| Recipe Page | [HTML](./labs/build-a-recipe-page/index.html) | [README](./labs/build-a-recipe-page/README.md) | [REVIEW](./labs/build-a-recipe-page/REVIEW.md) |
| Bookstore Page | [HTML](./workshops/build-a-bookstore-page/index.html) | [README](./workshops/build-a-bookstore-page/README.md) | [REVIEW](./workshops/build-a-bookstore-page/REVIEW.md) |

## View and inspect the work

Open any activity's `index.html` in a browser. No Node.js installation, package manager or local development server is required. Some images are hosted on the freeCodeCamp CDN or Wikimedia Commons and therefore require internet access.

To inspect the source:

1. Compare visible content with HTML headings, paragraphs, lists, figures, links and images.
2. Use **Developer Tools → Elements** to inspect the DOM and nested relationships.
3. Check `src`, `alt`, `href`, `target`, document language and character encoding where the lesson uses them.
4. Check **Developer Tools → Network** when an image fails to load; a syntactically valid `src` can still reference a missing resource.
5. Do not treat passing an exercise as a full accessibility, responsive-layout or cross-browser audit.

Workshop 02 uses a complete HTML5 document supplied by the lesson. Older Workshop 01 and Lab 01/02 archives include standalone document wrappers added for local viewing; those wrappers are **not** claims that the lessons separately taught boilerplate. Lab 03 directly practiced the document skeleton and revealed the difference between a **100% code-check result** and a **broken image in Preview**. Workshop 03 adds `div` containers, reusable classes, distinct IDs and native buttons; its static HTML does **not** implement cart or payment functionality.

## Subject roadmap

| Subject | Coverage | Status |
| --- | --- | --- |
| HTML elements and headings | Tags, `h1`–`h3`, `p`, nesting | Practiced |
| HTML debugging | Incorrect element names, closing syntax, DOM repair | Practiced |
| Links and images | `img`, `a`, `src`, `alt`, `href`, `target` | Practiced |
| Document structure | `html`, `head`, `body`, `title`, `meta charset`, `lang` | Practiced |
| Semantic grouping | `main`, `section`, `footer`, `figure`, `figcaption` | Practiced in Workshop 02 |
| Lists and sequence | `ul`, `ol`, `li`, rank vs procedure | Practiced in Workshop 02 and Lab 03 |
| Practical validation | User stories, DOM/Preview, external image resource loading | Practiced in Lab 03; deeper audits remain future work |
| Generic containers and identifiers | `div`, shared `class`, unique `id`, parent–child nesting | Practiced in Workshop 03 |
| Native buttons | `button`, shared classes and individual IDs | HTML structure practiced in Workshop 03; dynamic cart/checkout behavior not implemented |
| Further HTML | Forms, labels, tables, expanded accessibility | Planned |
| CSS fundamentals | Selectors, cascade, colors, typography, box model | Planned |
| CSS layout and responsive design | Flexbox, Grid, positioning, media queries | Planned |
| Advanced CSS and projects | Interaction states, effects and certification projects | Planned |

## Repository conventions

- Keep original learner completion evidence distinct from subsequent edits to an archived local edition.
- Use consistent directory names based on the official freeCodeCamp activity.
- **Do not record completion dates in learning documentation.**
- Keep the repository focused on HTML/CSS source and learning notes: **no Python test files or update scripts**.
- Update each activity's README/REVIEW and both cumulative root documents when completing a practical lesson.
- Review intended changes before committing. Never overwrite unrelated local work.

## Official resource

[freeCodeCamp Responsive Web Design Certification V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/)
