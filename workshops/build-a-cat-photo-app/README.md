# Workshop 02 — Build a Cat Photo App

> **Curriculum:** [freeCodeCamp Responsive Web Design V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/) → Basic HTML
> **Type:** Guided workshop
> **Status:** Completed — **42/42 steps (100%)**, as confirmed by the freeCodeCamp result screenshots
> **Official workshop:** [Build a Cat Photo App](https://www.freecodecamp.org/learn/responsive-web-design-v9/workshop-cat-photo-app/step-1)

## Goal

Build an HTML-only cat photo page while learning document structure, links, images, lists, semantic containers, captions, text emphasis and metadata. This workshop **does not** add custom CSS or JavaScript.

## Files

```text
workshops/build-a-cat-photo-app/
├── index.html   # Final HTML supplied by the learner
├── README.md    # Activity, source map and manual verification
└── REVIEW.md    # Conceptual explanations, IPA vocabulary and self-assessment
```

The `index.html` in this folder reproduces the complete code provided after the successful final step, including its element order, visible text, three image source URLs, anchors, and the `UTF-8` metadata. Unlike earlier archived exercises, **the standalone document structure was included in this freeCodeCamp workshop**. Do not add a stylesheet or other markup just to make the page look more elaborate.

## Main learning areas

The workshop has 42 steps; the following grouping is **by topic**, not an invented one-to-one transcript of the steps.

| Topic | HTML encountered | Practical purpose |
| --- | --- | --- |
| Document structure | `<!DOCTYPE html>`, `html`, `head`, `body`, `title`, `meta` | Provide an HTML document, title and character encoding |
| Main content | `main`, `section`, `h1`, `h2`, `h3`, `p` | Organize page sections and readable heading hierarchy |
| Links | `a`, `href`, `target="_blank"` | Link to images and another website |
| Images | `img`, `src`, `alt` | Embed cat and food images with text alternatives |
| Lists | `ul`, `ol`, `li` | Present unordered and ordered items |
| Figures | `figure`, `figcaption` | Connect an image to a descriptive caption |
| Meaningful emphasis | `em`, `strong` | Express emphasis and stronger importance |
| Footer | `footer`, `p`, `a` | Distinguish footer information from main content |

## Structure of the final page

```text
html[lang="en"]
├── head
│   ├── meta[charset="UTF-8"]
│   └── title: CatPhotoApp
└── body
    ├── main
    │   ├── h1: CatPhotoApp
    │   ├── section: Cat Photos
    │   │   ├── h2
    │   │   ├── p with link to running-cats.jpg
    │   │   ├── p with external link (opens new tab/window)
    │   │   └── a containing img: relaxing-cat.jpg
    │   └── section: Cat Lists
    │       ├── h2
    │       ├── h3 + ul (three items)
    │       ├── figure (lasagna.jpg + caption using em)
    │       ├── h3 + ol (three items)
    │       └── figure (cats.jpg + caption using strong)
    └── footer
        └── p with a link to freeCodeCamp.org
```

**Preserved from the learner's completed code:** two `section` elements, one `main`, one `footer`, three `img` elements, two `figure`/`figcaption` pairs, two three-item lists and the supplied link destinations.

## Notes about semantics and behavior

- **`ul` versus `ol`:** an unordered list conveys a collection without ranking or sequence; an ordered list represents items whose order matters in context.
- **`figure` and `figcaption`:** the caption belongs to the illustration as a unit, rather than being an arbitrary paragraph placed nearby.
- **`em` versus `strong`:** emphasis and stronger importance are *semantic* distinctions; italic/bold browser defaults are not their full meaning.
- **`meta charset="UTF-8"`:** declares the document's character encoding; `meta` is a **void element** and has no `</meta>` closing tag.
- **`target="_blank"`:** asks the browser to open a new browsing context. For production websites, consider the user experience and security implications of opening new tabs. The archive retains the workshop's exact source.
- **External resources:** the images load from freeCodeCamp's CDN, and `https://freecatphotoapp.com` is an external destination; access depends on connectivity and the destination being available.
- **No viewport meta:** the supplied final HTML has `meta charset` but no viewport meta. This is faithfully preserved. Responsive viewport configuration belongs to a separate lesson.

## View and inspect locally

1. Open `index.html` directly in a modern web browser; no build process or dependencies are needed.
2. Verify the headings **Cat Photos** and **Cat Lists**, three photographs, both lists, image captions and the footer.
3. Open **Developer Tools → Elements** and inspect the `head`, `main`, nested `section`s, lists, figures and footer.
4. Inspect the three `img` elements for `src` and `alt`; the network is needed for external images.
5. Inspect the `href` and `target` of each anchor. An external link's availability is different from the correctness of its HTML.

**Verification boundary:** freeCodeCamp showed 100% for the workshop. This confirms its exercise requirements, **not** a complete accessibility audit, independent browser validation or cross-browser compatibility assessment.

## Further review

- [Workshop 02 — REVIEW.md](./REVIEW.md): technical interpretation, terminology with British English IPA, pitfalls and 18 unanswered questions.
- [Root README](../../README.md): progress and navigation across exercises.
- [Cumulative RWD review](../../RWD_REVIEW.md): connections among the four completed practical activities.
