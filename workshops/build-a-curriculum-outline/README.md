# Workshop 01 — Build a Curriculum Outline

> **Curriculum:** freeCodeCamp Responsive Web Design V9 → Basic HTML  
> **Type:** Guided workshop  
> **Status:** Completed — **11/11 steps**  
> **Official activity:** [Build a Curriculum Outline](https://www.freecodecamp.org/learn/responsive-web-design-v9/workshop-curriculum-outline/step-1)

## Objective

Build a short curriculum webpage and understand how HTML elements define content and heading structure. The page introduces the roles of HTML, CSS and JavaScript, although the activity itself writes **HTML only**.

## Files

```text
workshops/build-a-curriculum-outline/
├── index.html   # Final source
├── README.md    # Activity notes and review of the steps
└── REVIEW.md    # Detailed concepts, IPA vocabulary and questions
```

## Steps completed

| Step | Task | Key idea |
| ---: | --- | --- |
| 1 | Enter `Welcome to freeCodeCamp` | Plain text can be displayed |
| 2 | Enclose the greeting in `h1` | Opening tag + content + closing tag |
| 3 | Add `Full-Stack Curriculum` | Add new content |
| 4 | Convert the curriculum label to `h2` | Heading hierarchy |
| 5 | Write a one-sentence introduction | Ordinary explanatory text |
| 6 | Wrap the sentence in `p` | Paragraph semantics |
| 7 | Add `Introduction to HTML` as `h3` | Subtopic heading |
| 8 | Add a paragraph describing HTML | Structured prose |
| 9 | Add `Introduction to CSS` as `h3` | Same-level headings |
| 10 | Add a paragraph describing CSS | Presentation versus content |
| 11 | Add a JavaScript heading and paragraph | Interaction versus document structure |

## Resulting structure

```text
h1  Welcome to freeCodeCamp
h2  Full-Stack Curriculum
p   Learn the skills to become a full-stack developer
h3  Introduction to HTML
p   HTML represents the content and structure of a webpage
h3  Introduction to CSS
p   CSS is used to style a webpage
h3  Introduction to Javascript
p   javaScript adds interactivity to a webpage
```

The capitalization of `Javascript` and `javaScript` mirrors the completed learning example. The correct language name in professional writing is **JavaScript**.

## Source versus local HTML document

The freeCodeCamp editor focuses on a short markup **fragment**. For convenient use outside the platform, the archived `index.html` additionally includes the standard HTML5 document skeleton (`DOCTYPE`, `html`, `head`, `title`, metadata and `body`). These extra tags are for local packaging and should not be mistaken for concepts assessed in this particular workshop.

## View and inspect

Open [`index.html`](./index.html) in a browser. Confirm that headings and paragraphs display in the expected order. To investigate further, use browser **Developer Tools → Elements** and compare the DOM to the source.

A browser's normal default styling makes headings look larger and bolder; the semantic purpose of an `h1`, `h2` or `h3` is the **content hierarchy**, not a preferred font size. No custom CSS or JavaScript is required for this activity.

## Learning outcomes

- Distinguish an HTML tag from a complete HTML element.
- Write correct opening and closing tags for headings and paragraphs.
- Organize a document with hierarchical headings rather than styling tricks.
- Explain the separate responsibilities of HTML, CSS and JavaScript.
- Recognize the difference between a course exercise fragment and a standalone document shell.

Detailed technical reasoning, common mistakes, English IPA and independent questions are in [REVIEW.md](./REVIEW.md). Broader connections are collected in the [root review](../../RWD_REVIEW.md).
