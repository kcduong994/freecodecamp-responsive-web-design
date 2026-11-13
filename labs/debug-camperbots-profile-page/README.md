# Lab 01 — Debug Camperbot's Profile Page

> **Curriculum:** freeCodeCamp Responsive Web Design V9 → Basic HTML  
> **Type:** Independent debugging lab  
> **Status:** Completed — freeCodeCamp checks passed  
> **Official curriculum:** [Responsive Web Design V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/)

## Objective

Correct the HTML mistakes in Camperbot's profile page while keeping the required headings and exact text. This lab develops the ability to read markup carefully rather than relying only on how the page appears in Preview.

## Files

```text
labs/debug-camperbots-profile-page/
├── index.html
├── README.md
└── REVIEW.md
```

## Problems fixed

| Initial markup | Correct form | Why |
| --- | --- | --- |
| `<heading2>About</heading2>` | `<h2>About</h2>` | A standard second-level heading is `h2` |
| `<pp>My name ...</pp>` | `<p>My name ...</p>` | A paragraph uses the `p` element |
| `<h3>Background and Interests<h3/>` | `<h3>Background and Interests</h3>` | Closing tags use `</name>` |
| `<pp>I enjoy ...</pp>` | `<p>I enjoy ...</p>` | The final sentence is also a paragraph |

## Correct structure

```text
h1  Hello from Camperbot!
h2  About
p   My name is Camperbot and I love learning new things.
h3  Background and Interests
p   I enjoy solving puzzles.
```

The freeCodeCamp solution is a short HTML fragment. The archived `index.html` includes an ordinary HTML5 document wrapper to open locally. That wrapper is for packaging; it was not part of the errors being debugged.

## What this teaches

- HTML tag names must match their intended standard elements.
- An unknown tag such as `heading2` may still produce visible text, but not the semantics of `h2`.
- `<h3/>` is not a valid way to close an existing `h3` in ordinary HTML.
- Browsers may recover from malformed markup, changing the DOM and the displayed result.
- Source correctness, rendered appearance and accessibility are related, but different concerns.

## Inspect locally

Open [`index.html`](./index.html) in a browser. Check that the About and Background and Interests labels are headings, while the two descriptive sentences are ordinary paragraphs. In **Developer Tools → Elements**, inspect the actual element names and hierarchy. If experimenting with incorrect tags, use a disposable copy and keep the archived solution unchanged.

The lab's successful freeCodeCamp result confirms its course requirements, not a full accessibility or cross-browser audit.

For terminology, browser parsing details, common mistakes and questions, read [REVIEW.md](./REVIEW.md). The broader connections appear in [RWD_REVIEW.md](../../RWD_REVIEW.md).
