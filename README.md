# freeCodeCamp — Responsive Web Design

> **Curriculum:** [Responsive Web Design Certification V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/)
> **Status:** In progress
> **Current track:** HTML → Basic HTML
> **Learning approach:** Study → Practice → Explain → Review → Advance

## Purpose

This repository is a structured record of my work through freeCodeCamp's **Responsive Web Design V9** curriculum. It preserves the HTML/CSS source created in workshops, labs and certification projects, together with technical explanations and self-assessment material.

The purpose is to understand how HTML and CSS work, not merely to complete a checklist: connect source code to document structure, the browser's interpretation, user experience, accessibility and engineering practice. Longer-term applications include coastal engineering, scientific communication, environmental data presentation and engineering web interfaces.

This repository is distinct from my Back-End Development and APIs coursework.

## Learning method

Follow the official curriculum in order:

1. **Theory** — study the concept in freeCodeCamp. Separate files are unnecessary for each theory page.
2. **Workshop** — follow the guided steps; archive the completed source and the concepts learned.
3. **Lab** — independently debug or implement the user stories; preserve the final solution and reasoning.
4. **Review** — explain mechanisms, common errors and practical checks; answer questions from recall through independent design.
5. **Certification projects** — complete the required projects and verify the acceptance criteria before recording completion.
6. **Final synthesis** — critically revise the cumulative [RWD_REVIEW.md](./RWD_REVIEW.md) after practical coursework.

The repository emphasizes **HTML/CSS source and documentation**, not auxiliary scripts or generated artifacts. Use freeCodeCamp's checks, browser preview and the browser's Developer Tools for practice and manual inspection, while recognizing what each confirms.

## Learning progress

| Area | Progress | Notes |
| --- | ---: | --- |
| Workshops | **2 completed** | Build a Curriculum Outline (**11/11**); Build a Cat Photo App (**42/42**) |
| Labs | **2 completed** | Debug Camperbot's Profile Page; Debug a Pet Adoption Page |
| Certification projects | **0 / 5** | Not started |
| Cumulative review | **In progress** | [RWD_REVIEW.md](./RWD_REVIEW.md) covers concepts from four completed activities |
| Final course review | Not complete | Revisit after practical work |
| Certification exam | Not attempted | Awaiting required coursework |
| Certificate | Not issued | Add only when earned |

### Completed activities

| # | Type | Activity | Core concepts | Source |
| ---: | --- | --- | --- | --- |
| 01 | Workshop | Build a Curriculum Outline | HTML elements, `h1`–`h3`, `p`, heading hierarchy | [Open](./workshops/build-a-curriculum-outline/) |
| 02 | Lab | Debug Camperbot's Profile Page | Correct tag names and closing syntax; browser error recovery | [Open](./labs/debug-camperbots-profile-page/) |
| 03 | Lab | Debug a Pet Adoption Page | `img`, `a`, `src`, `alt`, `href`, void elements, links and images | [Open](./labs/debug-pet-adoption-page/) |
| 04 | Workshop | **Build a Cat Photo App** | Full HTML document; `head`, `main`, `section`, `footer`; lists; figures/captions; emphasis; `meta charset` | [Open](./workshops/build-a-cat-photo-app/) |

Completion claims reflect the learner's successful freeCodeCamp results (including Workshop 02 at **100%, 42/42 steps**). They do not imply independent cross-browser, accessibility or production validation.

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
│   └── build-a-cat-photo-app/
│       ├── index.html
│       ├── README.md
│       └── REVIEW.md
├── labs/
│   ├── debug-camperbots-profile-page/
│   │   ├── index.html
│   │   ├── README.md
│   │   └── REVIEW.md
│   └── debug-pet-adoption-page/
│       ├── index.html
│       ├── README.md
│       └── REVIEW.md
└── certification-projects/
    └── .gitkeep
```

The `.gitkeep` file is a placeholder, not a completed certification project.

## Documentation guide

Each practical activity contains exactly three learning artifacts:

- **`index.html`** — the final HTML source, browser-openable without a build step.
- **`README.md`** — purpose, structure, learned topics, verification boundaries and local inspection.
- **`REVIEW.md`** — detailed technical concepts, British English IPA terminology, mistakes and unanswered self-assessment questions.

The cumulative [RWD_REVIEW.md](./RWD_REVIEW.md) links concepts across lessons. It does **not** reproduce every step of a workshop, and it separates completed practice from background explanations and future topics.

### Quick activity links

| Activity | Source | Notes | Review |
| --- | --- | --- | --- |
| Curriculum Outline | [HTML](./workshops/build-a-curriculum-outline/index.html) | [README](./workshops/build-a-curriculum-outline/README.md) | [REVIEW](./workshops/build-a-curriculum-outline/REVIEW.md) |
| Camperbot Profile | [HTML](./labs/debug-camperbots-profile-page/index.html) | [README](./labs/debug-camperbots-profile-page/README.md) | [REVIEW](./labs/debug-camperbots-profile-page/REVIEW.md) |
| Pet Adoption | [HTML](./labs/debug-pet-adoption-page/index.html) | [README](./labs/debug-pet-adoption-page/README.md) | [REVIEW](./labs/debug-pet-adoption-page/REVIEW.md) |
| Cat Photo App | [HTML](./workshops/build-a-cat-photo-app/index.html) | [README](./workshops/build-a-cat-photo-app/README.md) | [REVIEW](./workshops/build-a-cat-photo-app/REVIEW.md) |

## View and inspect the work

Open any activity's `index.html` in a browser. No Node.js installation, build process or external package is required. Some images are hosted on freeCodeCamp's CDN and need network access; some links lead to external websites.

To review the source:

1. Compare visible content with HTML headings, paragraphs, links, images, lists and figures.
2. Open **Developer Tools → Elements** to inspect the DOM and nested relationships.
3. Check `src`, `alt`, `href`, `target` and language/character metadata where the lesson uses them.
4. Distinguish valid markup from the availability of an external resource or link destination.
5. Do not treat passing an exercise as a complete audit of accessibility, responsive layout or browser compatibility.

Workshop 02 uses a complete HTML5 document supplied by the lesson, including `<!DOCTYPE html>`, `html lang="en"`, `head`, `meta charset="UTF-8"`, `title` and `body`. The older Workshop 01 and Lab 01/02 archives include a standalone HTML wrapper added for local viewing, which is **not** evidence of having completed separate boilerplate lessons.

## Subject roadmap

| Subject | Coverage | Status |
| --- | --- | --- |
| HTML elements and headings | Tags, elements, `h1`–`h3`, `p`, nesting | Practiced |
| HTML debugging | Incorrect element names and closing syntax | Practiced |
| Links and images | `img`, `a`, `src`, `alt`, `href`, `target` | Practiced |
| Document structure and semantic groups | `html`, `head`, `body`, `main`, `section`, `footer`, metadata | Practiced in Workshop 02; deeper study continues |
| Lists and figure semantics | `ul`, `ol`, `li`, `figure`, `figcaption`, `em`, `strong` | Practiced in Workshop 02 |
| Further HTML | Tables, forms, labels and expanded accessibility | Planned |
| CSS fundamentals | Selectors, cascade, colors, typography and box model | Planned |
| CSS layout and responsive design | Flexbox, Grid, positioning, media queries | Planned |
| Advanced CSS and projects | States, effects, accessibility and certification projects | Planned |

## Repository conventions

- Preserve the original completed exercise content and exact resource paths where possible. Document any extra local-only wrapper.
- Use clear, consistent directory names corresponding to the freeCodeCamp activity titles.
- **Do not record completion dates in learning documentation.**
- Keep the archive focused on HTML/CSS source and learning notes, without auxiliary testing or update scripts.
- Update the exercise's README/REVIEW and the two root documents when a new practical activity is completed.
- Review intended changes before committing; avoid overwriting unrelated work.

## Official resource

[freeCodeCamp Responsive Web Design Certification V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/)
