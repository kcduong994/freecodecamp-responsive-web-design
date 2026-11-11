# freeCodeCamp — Responsive Web Design

> **Status:** In progress  
> **Curriculum:** [Responsive Web Design Certification — freeCodeCamp V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/)  
> **Current track:** HTML → Basic HTML  
> **Latest completed activity:** Lab 01 — Debug Camperbot's Profile Page (2026-11-11)  
> **Evidence:** Workshop 01 (2026-11-10) and Lab 01 (2026-11-11) completed in freeCodeCamp; local Lab 01 source tests archived for verification.

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

**Verified snapshot: 11 November 2026.** Counts below refer to repository documentation and the supplied freeCodeCamp completion evidence, not an independently queried freeCodeCamp account.

| Activity | Verified progress | Evidence / next action |
| --- | ---: | --- |
| Workshops | **1 completed** | [Build a Curriculum Outline](./workshops/build-a-curriculum-outline/README.md): **11/11 steps, 100%**, freeCodeCamp screenshots |
| Labs | **1 completed** | [Debug Camperbot's Profile Page](./labs/debug-camperbots-profile-page/README.md): **100%**, freeCodeCamp screenshot (2026-11-11) |
| Certification projects | **0 / 5** | Not started |
| Cumulative conceptual review | **In progress** | [RWD_REVIEW.md](./RWD_REVIEW.md): Chapter 01 completed; later chapters planned |
| Final curriculum review | Not completed | Consolidate and revisit all concepts after practical work |
| Certification exam | Not attempted | Do not mark as passed without evidence |
| Certificate | Not issued | Add a verification link only after certification |

### Completed activities

| # | Track / activity | Source | Technical scope | Verified result |
| ---: | --- | --- | --- | --- |
| 01 | HTML · Workshop · **Build a Curriculum Outline** | [Open workshop](./workshops/build-a-curriculum-outline/) | HTML element anatomy; headings, paragraphs; semantic hierarchy | **11/11 freeCodeCamp steps**, **8/8 Windows local tests** (2026-11-10); pushed to `main` |
| 02 | HTML · Lab · **Debug Camperbot's Profile Page** | [Open lab](./labs/debug-camperbots-profile-page/) | Correct unknown elements, mistyped paragraph tags and closing-tag syntax | **freeCodeCamp 100%** (2026-11-11 screenshot); new local tests packaged for verification |

**Evidence boundaries:** freeCodeCamp screenshots confirm Workshop 01 (11 steps) and Lab 01 (100%). The Windows `unittest` screenshot confirms Workshop 01's eight checks. Lab 01's eight additional tests are included in the source package and must be run separately. None of these results substitutes for full accessibility, browser compatibility or certification testing.

## Workshop 01 — learning record

- [Source: `index.html`](./workshops/build-a-curriculum-outline/index.html)
- [Workshop README: steps, file structure and verification](./workshops/build-a-curriculum-outline/README.md)
- [Workshop REVIEW: detailed concepts, IPA glossary and self-assessment](./workshops/build-a-curriculum-outline/REVIEW.md)
- [Local test suite: `tests/test_html.py`](./workshops/build-a-curriculum-outline/tests/test_html.py)
- [Cumulative review: Chapter 01](./RWD_REVIEW.md#chapter-01--html-structure-and-heading-hierarchy-workshop-01)

The freeCodeCamp editor used an HTML **fragment**. The archived file adds standard HTML5 document scaffolding (`DOCTYPE`, `html`, `head`, metadata, `body`) so it opens locally. These additions are **packaging choices**, not claims that these topics were taught in Workshop 01. The archived visible text retains the capitalization shown in the completed lesson screenshot; professional spelling is **JavaScript**.

## Lab 01 — learning record

- [Source: `index.html`](./labs/debug-camperbots-profile-page/index.html)
- [Lab README: error fixes and verification](./labs/debug-camperbots-profile-page/README.md)
- [Lab REVIEW: concepts, IPA and independent questions](./labs/debug-camperbots-profile-page/REVIEW.md)
- [Local tests: `tests/test_html.py`](./labs/debug-camperbots-profile-page/tests/test_html.py)
- [Cumulative review: Lab 01 section](./RWD_REVIEW.md#lab-01--html-debugging-and-error-recovery)

The archived lab uses an HTML5 wrapper for standalone viewing; the freeCodeCamp editor itself contained only a short HTML fragment. Its completed text and element order match the screenshot.

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
│   ├── .gitkeep
│   └── debug-camperbots-profile-page/
│       ├── index.html
│       ├── README.md
│       ├── REVIEW.md
│       └── tests/
│           └── test_html.py
└── certification-projects/
    └── .gitkeep
```

The `.gitkeep` files are placeholders retained from initial setup; they are not evidence of completed work.

## Local verification

From the repository root, with Python 3 installed:

```powershell
py -m unittest discover -s workshops/build-a-curriculum-outline/tests -p "test_*.py" -v
```

To run Lab 01's independent checks:

```powershell
py -m unittest discover -s labs/debug-camperbots-profile-page/tests -p "test_*.py" -v
```

Use `python` instead of `py` when appropriate. **Each suite contains eight tests.** The Windows screenshots supplied on 2026-11-10 verify Workshop 01; run the new Lab 01 suite on your machine before claiming its Windows verification.

Open each activity's `index.html` directly in a browser. No Node.js or external dependency is required. Both Python suites check source markup; they do **not** measure rendering, keyboard operation or accessibility.

## Subject roadmap (not a completion claim)

| Area | Topics to study | Status |
| --- | --- | --- |
| HTML foundations | Elements, tags, headings, paragraphs, document structure and basic syntax debugging | **Workshop 01 + Lab 01: introductory coverage** |
| HTML content and accessibility | Attributes, links, images, lists, tables, forms, semantic elements | Planned |
| CSS foundations | Selectors, cascade, specificity, inheritance, colors, typography, box model | Planned |
| CSS layouts | Units, sizing, positioning, Flexbox, Grid, responsive layouts and media queries | Planned |
| CSS effects | Pseudo-classes, pseudo-elements, variables, transforms, transitions and animations | Planned |
| Project quality | Debugging, accessibility checks, browser developer tools and validation | **Lab 01: syntax debugging introduced**; broader quality checks planned |
| Certification | Five required projects, review, exam and certificate | Not completed |

The exact exercise sequence and names follow the official freeCodeCamp V9 curriculum. The **next visible activity** after Lab 01 is *Understanding HTML Attributes* (theory); this is not yet claimed as completed.

## Documentation and verification rules

1. **Evidence before status:** distinguish *completed in freeCodeCamp*, *source committed*, *local test passed*, and *browser/a11y verified*. These are separate claims.
2. **Archive actual work:** preserve the final workshop code and use a separate temporary copy for experiments.
3. **Make tests inspectable:** document each test suite's scope and avoid treating a passing test as broad product acceptance.
4. **Use reviews for understanding:** the workshop `REVIEW.md` can explain individual steps; root `RWD_REVIEW.md` synthesizes cross-cutting concepts and should not duplicate the full workshop transcript.
5. **Protect the learning record:** update only intended files, inspect `git status`/`git diff`, and commit descriptive changes without rewriting unrelated history.

*Last documentation update: 2026-11-11. Lab 01 local tests are included for reproducibility; Windows execution should be recorded after verification.*
