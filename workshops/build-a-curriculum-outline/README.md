# Build a Curriculum Outline

> **freeCodeCamp — Responsive Web Design Certification V9**  
> **Track:** HTML → Basic HTML  
> **Activity:** Guided workshop  
> **Status:** Completed — **11 / 11 steps (100%)**  
> **Evidence:** freeCodeCamp's “Congratulations. Your code passes.” message and the course outline showing all 11 steps completed in screenshots supplied on **2026-11-10**.  
> **Official workshop:** [Build a Curriculum Outline](https://www.freecodecamp.org/learn/responsive-web-design-v9/workshop-curriculum-outline/step-1)

## Purpose

Build a small curriculum-outline webpage while learning how HTML uses **elements** to define document content and heading hierarchy. This workshop introduces the roles of **HTML, CSS and JavaScript**, without requiring the learner to write styles or scripts yet.

This directory archives the source produced during the first freeCodeCamp Responsive Web Design V9 workshop, the workshop-specific conceptual review, and dependency-free local checks. No completion claim is made for later lessons, labs, or the certification.

## Files

```text
workshops/build-a-curriculum-outline/
├── index.html       # Completed curriculum outline (browser-openable HTML5 document)
├── README.md        # Workshop goal, learning steps and verification
├── REVIEW.md        # Concepts, terminology, questions and pitfalls
└── tests/
    └── test_html.py # Python standard-library structural tests
```

## Completed steps

| Step | Work completed | Key learning |
| ---: | --- | --- |
| 1 | Enter the welcome text | Plain text can appear in the browser preview |
| 2 | Wrap the welcome text in `<h1>` | Opening tag + content + closing tag |
| 3 | Add `Full-Stack Curriculum` | Text content before semantic markup |
| 4 | Wrap that text in `<h2>` | Subheading / second-level heading |
| 5 | Add a one-sentence introduction | Descriptive prose |
| 6 | Wrap the sentence in `<p>` | Paragraph element |
| 7 | Add `Introduction to HTML` as `<h3>` | Third-level heading |
| 8 | Add a paragraph about HTML | Content and structure |
| 9 | Add `Introduction to CSS` as `<h3>` | Reusing a heading level for sibling topics |
| 10 | Add a paragraph about CSS | Styling versus document content |
| 11 | Add the JavaScript heading and paragraph | Interactivity; finish all 11 steps |

## Source fidelity and standalone-document additions

The **visible page content and its capitalization reproduce the completed Step 11 editor screenshot**, including `Introduction to Javascript` and `javaScript adds interactivity to a webpage`. The unusual capitalization is retained intentionally as learning evidence, **not** endorsed as recommended terminology. Standard product capitalization is **JavaScript**.

The freeCodeCamp editor initially contains only HTML fragments (`<h1>`, `<h2>`, `<h3>`, `<p>`). For reliable local use, `index.html` adds the following **standalone document scaffolding**; it is a local packaging improvement, not something claimed as taught/completed in this specific workshop:

- `<!DOCTYPE html>` — requests standards-mode HTML parsing;
- `<html lang="en">` — identifies the document and its language;
- `<head>` with `charset`, `viewport` and `<title>` metadata;
- `<body>` — encloses the content.

No JavaScript, stylesheets, dependencies, frameworks or generated build artifacts have been added. The browser supplies its own default styles for headings and paragraphs.

## How to open locally

From the repository root, open `workshops/build-a-curriculum-outline/index.html` directly in a modern browser. A local HTTP server is **not needed** for this static HTML lesson.

Optional server, if you already have Python installed:

```bash
python -m http.server 8000 -d workshops/build-a-curriculum-outline
```

Then open `http://localhost:8000/`. Stop the server with `Ctrl+C`.

## Automated local tests (no external packages)

From the **repository root**:

```bash
python -m unittest discover -s workshops/build-a-curriculum-outline/tests -p 'test_*.py' -v
```

On Windows, if `python` is not recognized:

```powershell
py -m unittest discover -s workshops/build-a-curriculum-outline/tests -p 'test_*.py' -v
```

The tests inspect HTML source structure and check document metadata, tag pairing, text content, heading hierarchy, element order and absence of unintended CSS/JavaScript. **They do not replace the official freeCodeCamp assessment** or a visual/keyboard/browser audit.

## Manual checks

1. Open `index.html` in the browser. Confirm one large heading, one subordinate heading, the introduction, and HTML/CSS/JavaScript subsections.
2. Open browser DevTools → **Elements** to inspect the element tree; verify heading levels and paragraph siblings.
3. Temporarily change one `<h3>` to `<p>` and note how the display and semantics differ; restore the file before committing.
4. Rerun the local tests, then review `git diff` before staging changes.

## Learning record

- **Official freeCodeCamp result:** completed, 11/11 steps, 100% (user-supplied screenshots, 2026-11-10).
- **Repository status:** source files prepared for local import; **not automatically committed or pushed**.
- **Local tests:** run the command above and use your own terminal output as evidence on your machine.
- **Next curriculum activity:** *Debug Camperbot's Profile Page* (lab), as displayed in the user-supplied curriculum screenshot.

See [REVIEW.md](./REVIEW.md) for glossary (IPA), detailed concept review, common mistakes, and self-assessment questions.
