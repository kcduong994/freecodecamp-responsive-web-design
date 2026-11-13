# freeCodeCamp — Responsive Web Design

> **Curriculum:** [Responsive Web Design Certification V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/)  
> **Status:** In progress  
> **Current track:** HTML → Basic HTML  
> **Learning approach:** Study → Practice → Explain → Review → Advance

## Purpose

This repository is a structured record of my work through freeCodeCamp's **Responsive Web Design V9** curriculum. It stores the HTML/CSS source created in workshops, labs and certification projects together with technical explanations and self-assessment notes.

The purpose is to understand how HTML and CSS work, not merely to complete a checklist. I want to connect the code to the document structure, the browser's interpretation, the user experience and good engineering practice. Longer-term applications include coastal engineering, scientific communication, environmental data presentation and engineering web interfaces.

This repository is distinct from my Back-End Development and APIs coursework.

## Learning method

The official freeCodeCamp curriculum is followed in order:

1. **Theory** — study the concept in freeCodeCamp. Separate files are unnecessary for every theory step.
2. **Workshop** — follow the guided activity, then archive the completed source and the concepts learned.
3. **Lab** — independently debug or implement the user stories, then preserve the final solution and reasoning.
4. **Review** — explain underlying mechanisms, common mistakes and practical checks; answer questions from recall through independent design.
5. **Certification projects** — work through the required projects without declaring them complete before passing their requirements.
6. **Final synthesis** — revise the cumulative [RWD_REVIEW.md](./RWD_REVIEW.md) when the practical curriculum is finished.

The repository emphasizes **source files and documentation**. Routine HTML/CSS learning exercises do not require additional Python test scripts, generated verification utilities or automated documentation updaters. The official freeCodeCamp checks, browser preview and manual developer-tools inspection are sufficient for this stage of learning, each within its own scope.

## Learning progress

| Area | Progress | Notes |
| --- | ---: | --- |
| Workshops | **1 completed** | Build a Curriculum Outline — all 11 steps completed |
| Labs | **2 completed** | Debug Camperbot's Profile Page; Debug a Pet Adoption Page |
| Certification projects | **0 / 5** | Not started |
| Cumulative review | **In progress** | Covers the material learned so far |
| Final course review | Not complete | Revisit after practical work |
| Certification exam | Not attempted | Awaiting required coursework |
| Certificate | Not issued | Add only when earned |

### Completed activities

| # | Type | Activity | Core concepts | Source |
| ---: | --- | --- | --- | --- |
| 01 | Workshop | Build a Curriculum Outline | HTML elements, `h1`–`h3`, `p`, heading hierarchy | [Open](./workshops/build-a-curriculum-outline/) |
| 02 | Lab | Debug Camperbot's Profile Page | Correct HTML tag names and closing syntax; browser error recovery | [Open](./labs/debug-camperbots-profile-page/) |
| 03 | Lab | Debug a Pet Adoption Page | `img`, `a`, `src`, `alt`, `href`, void elements, links and images | [Open](./labs/debug-pet-adoption-page/) |

The learning record reflects the completed freeCodeCamp activities shown in the supplied results. It does not claim that every page has undergone independent accessibility, browser compatibility or production testing.

## Repository structure

```text
freecodecamp-responsive-web-design/
├── README.md
├── RWD_REVIEW.md
├── .gitignore
├── workshops/
│   └── build-a-curriculum-outline/
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
```

The repository may retain `.gitkeep` placeholders in parent folders; these are not learning deliverables.

## Documentation guide

Each practical activity has three files:

- **`index.html`** — the completed HTML source, packaged as a browser-openable HTML5 document.
- **`README.md`** — objective, requirements, the solution's structure, lessons learned and how to inspect the result.
- **`REVIEW.md`** — conceptual explanations, English vocabulary with IPA, common mistakes and unanswered self-assessment questions.

The root **[RWD_REVIEW.md](./RWD_REVIEW.md)** connects concepts across lessons and keeps future curriculum topics clearly distinguished from what has been learned. The review should expand meaningfully, rather than copying every lesson transcript.

## View and inspect the work

Open an activity's `index.html` in a browser. The three activities are plain HTML and require no build process or package installation.

For manual verification, compare the browser's display with the source, inspect the **Elements** panel in Developer Tools, and confirm that the semantic heading, paragraph, image and link elements match the activity's requirements. In the pet-adoption lab, `/cats` and `/dogs` are root-relative links supplied by freeCodeCamp; they need corresponding routes to navigate successfully outside the learning platform.

**Important distinction:** a successful freeCodeCamp result confirms its specified requirements. It does not automatically establish complete accessibility, cross-browser behavior or production readiness.

## Subject roadmap

| Subject | Coverage | Status |
| --- | --- | --- |
| HTML elements and headings | Tags, elements, `h1`–`h3`, `p` | Introduced |
| HTML debugging | Incorrect element names, misplaced closing syntax | Introduced |
| Images and links | `img`, `a`, `src`, `alt`, `href`, void elements | Introduced |
| Full HTML documents and attributes | Metadata, document language, broader attribute semantics | Further study planned |
| Additional semantic HTML | Lists, tables, forms, landmarks, accessibility | Planned |
| CSS fundamentals | Selectors, cascade, colors, typography, box model | Planned |
| CSS layout and responsive design | Flexbox, Grid, positioning, media queries | Planned |
| Advanced CSS and projects | States, effects, accessibility, certification projects | Planned |

## Repository conventions

- Preserve the original completed exercise content. If an HTML5 wrapper is added for local viewing, document that distinction.
- Use clear, consistent directory names matching the exercise titles.
- Do not record completion dates in learning documents.
- Keep the repository focused on HTML/CSS source and learning notes, rather than auxiliary testing or update scripts.
- Update both the relevant activity notes and the root progress/review after completing a new practical activity.
- Review changes before committing; avoid rewriting unrelated completed exercises.

## Official resource

[freeCodeCamp Responsive Web Design V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/)
