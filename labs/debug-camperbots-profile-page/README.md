# Lab 01 — Debug Camperbot's Profile Page

> **Curriculum:** freeCodeCamp Responsive Web Design V9 — Basic HTML  
> **Activity:** Independent Lab 01  
> **freeCodeCamp status:** Completed — **100%**, “Congratulations. Your code passes.”  
> **Evidence:** final code, preview and passed-tests screenshot supplied by the learner on **2026-11-11**.  
> **Official curriculum:** [Responsive Web Design V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/)

## Goal

Debug an existing HTML profile page by correcting incorrect element names and a malformed closing tag, while preserving the required text. This lab practices diagnosing an HTML source rather than following individual workshop steps.

## Project structure

```text
labs/debug-camperbots-profile-page/
├── index.html             # Final corrected HTML; opens directly in a browser
├── README.md              # Lab requirements and verification
├── REVIEW.md              # Concepts, IPA, pitfalls, and questions
└── tests/
    └── test_html.py       # Dependency-free local structural tests
```

## Errors resolved

| Original markup | Corrected markup | Reason |
| --- | --- | --- |
| `<heading2>About</heading2>` | `<h2>About</h2>` | `heading2` is not the standard HTML level-two heading element. |
| `<pp>My name ...</pp>` | `<p>My name ...</p>` | Paragraphs use the `p` element. |
| `<h3>Background and Interests<h3/>` | `<h3>Background and Interests</h3>` | Closing tags use `</name>`, not `<name/>`. |
| `<pp>I enjoy ...</pp>` | `<p>I enjoy ...</p>` | The second paragraph needs a valid `p` element too. |

### Completed hierarchy

```text
body
├── h1  Hello from Camperbot!
├── h2  About
├── p   My name is Camperbot and I love learning new things.
├── h3  Background and Interests
└── p   I enjoy solving puzzles.
```

The final visible strings and capitalization match the learner's screenshot. The **standalone** `index.html` adds `<!DOCTYPE html>`, `<html lang="en">`, `<head>`, metadata and `<body>` for convenient local use; freeCodeCamp's editor only showed the inner HTML fragment. Those additional document elements are *packaging additions*, not claims about what Lab 01 taught or checked.

No CSS stylesheet, JavaScript program, framework or package dependency was introduced.

## What was verified

| Evidence | Result | Scope |
| --- | --- | --- |
| freeCodeCamp | **Passed — 100%** | Lab's official checks, shown in screenshot dated 2026-11-11 |
| Local test suite | Run using command below | Exact text/order, heading counts, balanced tags, metadata, unexpected markup |
| Browser compatibility / accessibility | Not independently verified | Separate testing would be required |

## Open and test locally

Open `index.html` directly in a modern browser. A development server is **not needed** for static HTML.

From the **repository root** run:

```powershell
py -m unittest discover -s labs/debug-camperbots-profile-page/tests -p "test_*.py" -v
```

Replace `py` with `python` if necessary. The suite contains **eight** standard-library tests. A successful run should report `Ran 8 tests` and `OK`.

Optionally start a local server:

```powershell
py -m http.server 8000 -d labs/debug-camperbots-profile-page
```

Then navigate to `http://localhost:8000/` and stop the server with `Ctrl+C`.

## Manual debugging exercise

Work on a **temporary copy** of `index.html` so the archived result stays unchanged:

1. Change `<h2>` to `<heading2>` and observe how browser presentation and semantics differ.
2. Change `<p>` to `<pp>` and inspect the *Elements* panel in Developer Tools.
3. Change `</h3>` to `<h3/>` and inspect the DOM tree the parser actually constructed.
4. Restore the correct source and rerun all local tests.

## Learning record

- **HTML elements practiced:** `h1`, `h2`, `h3`, `p`.
- **Skills added:** correcting nonstandard element names and malformed closing-tag syntax; distinguishing markup, browser preview and DOM.
- **Broader caveat:** a visible page or passing local test does not prove full accessibility or cross-browser compatibility.
- **Next freeCodeCamp activity shown in the learner's curriculum:** *Understanding HTML Attributes* (theory; not yet marked complete).

Read [REVIEW.md](./REVIEW.md) for a deeper explanation, pronunciation glossary, and independent self-assessment. The root [README.md](../../README.md) and [RWD_REVIEW.md](../../RWD_REVIEW.md) track overall progress and cumulative knowledge.
