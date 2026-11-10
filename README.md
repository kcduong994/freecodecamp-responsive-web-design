# freeCodeCamp — Responsive Web Design

> **Status:** In progress  
> **Curriculum:** [Responsive Web Design Certification — freeCodeCamp V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/)  
> **Focus:** HTML, CSS, semantic structure, accessibility, responsive layouts, and tested front-end projects.

## Purpose

This repository documents my **freeCodeCamp Responsive Web Design V9** learning journey.

It serves as a structured archive of completed workshops, labs, and certification projects, including their source code and supporting documentation.

This repository is separate from my completed Back-End Development and APIs coursework.

My long-term goal is to apply web development skills to coastal engineering, hydrodynamic modeling, scientific computing, and engineering software.

## Learning Progress

| Activity | Completed | Notes |
|---|---:|---|
| Workshops | **1** | [Build a Curriculum Outline](./workshops/build-a-curriculum-outline/) — 11/11 steps; freeCodeCamp screenshot confirms 100% (2026-11-10) |
| Labs | 0 | Not started |
| Certification Projects | 0 / 5 | Five required projects |
| Curriculum Review | Not started | Repository-wide review after completing the practical curriculum; workshop-level notes are available separately |
| Certification Exam | Not attempted | Official examination |
| Certificate | Not issued | Verification link will be added after certification |

Progress will be updated as each challenge is completed and verified.

## Completed Workshops

| # | Workshop | Focus | Evidence |
|---:|---|---|---|
| 01 | [Build a Curriculum Outline](./workshops/build-a-curriculum-outline/) | `h1`–`h3`, `p`, HTML element anatomy; roles of HTML, CSS and JavaScript | 11/11 freeCodeCamp steps, 100%, screenshots from 2026-11-10 |

The workshop folder contains its HTML source, a detailed README, workshop-specific `REVIEW.md`, and a dependency-free local test suite. Local verification is separate from freeCodeCamp's own checks.

## Curriculum Areas

### HTML

- HTML elements and attributes
- Document structure
- Semantic HTML
- Links, images, and lists
- Tables and forms
- Accessibility fundamentals

### CSS

- CSS selectors and properties
- Cascade, inheritance, and specificity
- Colors and typography
- Box model
- Units and sizing
- Positioning
- Flexbox and Grid
- Responsive layouts and media queries
- Pseudo-classes and pseudo-elements
- Transitions, transforms, and animations

### Certification

- Guided workshops
- Independent labs
- Five certification projects
- Curriculum review
- Certification exam

The exact exercises and project titles will follow the official freeCodeCamp V9 curriculum.

## Repository Structure

```text
freecodecamp-responsive-web-design/
├── README.md
├── RWD_REVIEW.md                # Final review: planned, not yet completed
├── .gitignore
├── workshops/
│   └── build-a-curriculum-outline/
│       ├── index.html
│       ├── README.md
│       ├── REVIEW.md
│       └── tests/
│           └── test_html.py
├── labs/
└── certification-projects/
```

Project source files and individual README files will be added as each workshop, lab, or certification project is completed.

## Local verification

From the repository root, with Python 3 installed:

```bash
python -m unittest discover -s workshops/build-a-curriculum-outline/tests -p 'test_*.py' -v
```

On Windows, use `py -m unittest ...` if the `python` launcher is unavailable. See the [workshop README](./workshops/build-a-curriculum-outline/README.md) for the exact command and the scope of the tests.
