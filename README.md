# freeCodeCamp — Responsive Web Design

> **Status:** In progress  
> **Curriculum:** [Responsive Web Design Certification — freeCodeCamp V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/)  
> **Current track:** HTML → Basic HTML  
> **Latest completed activity:** Workshop 01 — Build a Curriculum Outline (2026-11-10)  
> **Last evidence checkpoint:** [`83af1c7`](https://github.com/kcduong994/freecodecamp-responsive-web-design/commit/83af1c7d02ab4c835c1ce78d1feac82ce4150bdb) on `main` (verified 2026-11-10)

## Purpose

This repository documents my **freeCodeCamp Responsive Web Design V9** learning journey. It preserves the HTML/CSS source developed in workshops, labs and certification projects, together with repeatable local checks and technical study notes.

The goal is not merely to pass freeCodeCamp challenges. I want to understand **what the browser receives, how it interprets the document, what the user experiences, what can go wrong, and how to verify the result**. These skills will later support coastal engineering, hydrodynamic modeling, scientific computing, environmental data presentation and engineering software.

This repository is separate from my Back-End Development and APIs coursework.

## Learning method

Follow the official curriculum **in order**, without treating all lesson types as the same activity:

```text
Theory → Workshop / Lab → Review → Quiz / checks
       → Certification projects → Final conceptual synthesis
```

- **Theory:** study the official explanations; record concepts in the cumulative [RWD_REVIEW.md](./RWD_REVIEW.md) once understood. A source file is not required for every theory page.
- **Workshop:** complete each guided step; archive the final source and a project-specific `README.md` with verified evidence.
- **Lab:** solve the requirements independently, retain the resulting code, document failure cases, and run checks appropriate to the lab.
- **Review and quiz:** practice recall, explanation, application, debugging and design judgment. Distinguish in-lesson material from explicitly labeled extensions.
- **Certification projects:** preserve requirements, source, testing and acceptance evidence; do not mark anything complete merely because a folder exists.
- **Final conceptual synthesis:** revise the cumulative review *after* the practical curriculum. Its first chapter can already be written while studying.

## Learning progress

**Verified snapshot: 10 November 2026.** Counts below refer to repository documentation and the supplied freeCodeCamp completion evidence, not an independently queried freeCodeCamp account.

| Activity | Verified progress | Evidence / next action |
| --- | ---: | --- |
| Workshops | **1 completed** | [Build a Curriculum Outline](./workshops/build-a-curriculum-outline/README.md): **11/11 steps, 100%**, freeCodeCamp screenshots |
| Labs | **0 documented as complete** | Next: *Debug Camperbot's Profile Page* (listed next in the curriculum screenshot) |
| Certification projects | **0 / 5** | Not started |
| Cumulative conceptual review | **In progress** | [RWD_REVIEW.md](./RWD_REVIEW.md): Chapter 01 completed; later chapters planned |
| Final curriculum review | Not completed | Consolidate and revisit all concepts after practical work |
| Certification exam | Not attempted | Do not mark as passed without evidence |
| Certificate | Not issued | Add a verification link only after certification |

### Completed activities

| # | Track / activity | Source | Technical scope | Verified result |
| ---: | --- | --- | --- | --- |
| 01 | HTML · Workshop · **Build a Curriculum Outline** | [Open workshop](./workshops/build-a-curriculum-outline/) | HTML element anatomy; `<h1>`, `<h2>`, `<h3>`, `<p>`; heading hierarchy; HTML/CSS/JavaScript responsibilities | **11/11 freeCodeCamp steps passed**; **8/8 local Python tests passed** (Windows terminal screenshot, 2026-11-10); committed and pushed to `main` |

**Evidence boundaries:** the freeCodeCamp completion screenshot confirms the workshop exercises, and the local `unittest` result confirms the eight checks implemented in the repository. Neither is a substitute for full HTML validation, browser compatibility testing, an accessibility audit, or certification.

## Workshop 01 — learning record

- [Source: `index.html`](./workshops/build-a-curriculum-outline/index.html)
- [Workshop README: steps, file structure and verification](./workshops/build-a-curriculum-outline/README.md)
- [Workshop REVIEW: detailed concepts, IPA glossary and self-assessment](./workshops/build-a-curriculum-outline/REVIEW.md)
- [Local test suite: `tests/test_html.py`](./workshops/build-a-curriculum-outline/tests/test_html.py)
- [Cumulative review: Chapter 01](./RWD_REVIEW.md#chapter-01--html-structure-and-heading-hierarchy-workshop-01)

The freeCodeCamp editor used an HTML **fragment**. The archived file adds standard HTML5 document scaffolding (`DOCTYPE`, `html`, `head`, metadata, `body`) so it opens locally. These additions are **packaging choices**, not claims that these topics were taught in Workshop 01. The archived visible text retains the capitalization shown in the completed lesson screenshot; professional spelling is **JavaScript**.

## Repository structure

```text
freecodecamp-responsive-web-design/
├── .gitignore
├── README.md                        # Overall progress and learning method
├── RWD_REVIEW.md                    # Cumulative concepts; currently Chapter 01
├── workshops/
│   ├── .gitkeep
│   └── build-a-curriculum-outline/
│       ├── index.html
│       ├── README.md
│       ├── REVIEW.md
│       └── tests/
│           └── test_html.py
├── labs/
│   └── .gitkeep
└── certification-projects/
    └── .gitkeep
```

The `.gitkeep` files simply keep currently empty directories in Git; they do not represent finished exercises.

## Local verification

From the repository root, with Python 3 installed:

```powershell
py -m unittest discover -s workshops/build-a-curriculum-outline/tests -p "test_*.py" -v
```

On systems where `py` is unavailable, use `python` instead. Successful execution reports **8 tests** and `OK`. The Windows terminal screenshots supplied on 2026-11-10 show this result locally.

To inspect the page, open [the HTML file](./workshops/build-a-curriculum-outline/index.html) in a browser. No Node.js, package manager, local HTTP server or external dependency is required for this workshop. The automated tests are intentionally limited to the archived HTML source and do not measure rendering or accessibility.

## Subject roadmap (not a completion claim)

| Area | Topics to study | Status |
| --- | --- | --- |
| HTML foundations | Elements, tags, headings, paragraphs, document structure | **Workshop 01: introductory coverage** |
| HTML content and accessibility | Attributes, links, images, lists, tables, forms, semantic elements | Planned |
| CSS foundations | Selectors, cascade, specificity, inheritance, colors, typography, box model | Planned |
| CSS layouts | Units, sizing, positioning, Flexbox, Grid, responsive layouts and media queries | Planned |
| CSS effects | Pseudo-classes, pseudo-elements, variables, transforms, transitions and animations | Planned |
| Project quality | Debugging, accessibility checks, browser developer tools and validation | Develop incrementally |
| Certification | Five required projects, review, exam and certificate | Not completed |

The exact exercise sequence and names follow the official freeCodeCamp V9 curriculum. The **next visible activity** in the supplied curriculum screenshot is the lab *Debug Camperbot's Profile Page*.

## Documentation and verification rules

1. **Evidence before status:** distinguish *completed in freeCodeCamp*, *source committed*, *local test passed*, and *browser/a11y verified*. These are separate claims.
2. **Archive actual work:** preserve the final workshop code and use a separate temporary copy for experiments.
3. **Make tests inspectable:** document each test suite's scope and avoid treating a passing test as broad product acceptance.
4. **Use reviews for understanding:** the workshop `REVIEW.md` can explain individual steps; root `RWD_REVIEW.md` synthesizes cross-cutting concepts and should not duplicate the full workshop transcript.
5. **Protect the learning record:** update only intended files, inspect `git status`/`git diff`, and commit descriptive changes without rewriting unrelated history.

*Last documentation update: 2026-11-10. This README reports the verified checkpoint above and should be refreshed after subsequent activities.*
