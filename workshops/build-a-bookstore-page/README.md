# Workshop 03 — Build a Bookstore Page

> **Curriculum:** [freeCodeCamp — Responsive Web Design V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/) → Basic HTML
> **Type:** Guided HTML workshop
> **Status:** Completed — **19/19 steps (100%)**, evidenced by the learner's final-step freeCodeCamp screenshot
> **Official workshop:** [Build a Bookstore Page](https://www.freecodecamp.org/learn/responsive-web-design-v9/workshop-bookstore-page/step-1)

## Objective

Create an **HTML-only bookstore page** with two book cards and a separate cart/checkout action group. The workshop practices **generic containers (`div`), reusable classes (`class`), unique identifiers (`id`), nested content, headings, paragraphs and buttons**.

This page is a **structural exercise**: it does not implement a shopping cart, payment flow, book inventory service, styling, or JavaScript. The visible buttons have no programmed purchase behavior. Passing a freeCodeCamp check is not evidence of working e-commerce functionality.

## Learning evidence and source integrity

The learner supplied the complete code and an image from **Step 19** showing **100%** / "Congratulations. Your code passes." The archived `index.html` keeps all text, attributes, identifiers, element order and behavior of that accepted source. Changes are limited to **indentation, blank lines and removal of trailing spaces**; no CSS, script, or additional page content was introduced.

The learner-provided source is the evidence for course completion. The local archive has not been separately submitted to freeCodeCamp, and no browser-interaction acceptance has been performed here.

## Files

```text
workshops/build-a-bookstore-page/
├── index.html   # Learner's passing final HTML, formatting normalized
├── README.md    # Objectives, structural map, verification and limitations
└── REVIEW.md    # In-depth concepts, British IPA, pitfalls and questions
```

## What this workshop practices

| Concept | Exact source | Why it matters |
| --- | --- | --- |
| HTML document | `<!DOCTYPE html>`, `html lang="en"`, `head`, `body` | Basic HTML5 document and language declaration |
| Head metadata | `meta charset="UTF-8"`, `title` | Character encoding and browser/tab title |
| Visible hierarchy | One `h1`, two `h2`, paragraphs | Global page heading and book titles |
| Generic grouping | `div.card-container`, two `div.card`, `div.btn-container` | Group related elements without claiming semantics not provided by `div` |
| Reusable class | Both books have `class="card"`; all four buttons use `class="btn"` | A common identifier for a group of elements |
| Unique IDs | `sally-adventure-book`, `dave-cooking-book`, `view-cart-btn`, `checkout-btn` | Individual elements can be unambiguously targeted |
| Native controls | Two `Buy Now` buttons, `View Cart`, `Checkout` | Correct interactive element type, though no functionality is attached |

## Source hierarchy

```text
html[lang=en]
├── head
│   ├── meta[charset=UTF-8]
│   └── title: XYZ Bookstore Page
└── body
    ├── h1: XYZ Bookstore
    ├── p: bookstore introduction
    ├── div.card-container
    │   ├── div.card#sally-adventure-book
    │   │   ├── h2: Sally's SciFi Adventure
    │   │   ├── p: book description
    │   │   └── button.btn: Buy Now
    │   └── div.card#dave-cooking-book
    │       ├── h2: Dave's Cooking Adventure
    │       ├── p: book description
    │       └── button.btn: Buy Now
    ├── p: checkout guidance
    └── div.btn-container
        ├── button.btn#view-cart-btn: View Cart
        └── button.btn#checkout-btn: Checkout
```

Note: `.card`, `#view-cart-btn` etc. in the diagram are **CSS-style shorthand**, not literal tag syntax required in the HTML. They are used only to make the hierarchy readable.

## Manual inspection checklist

- [ ] Open `index.html` locally and confirm that the title in the browser tab is `XYZ Bookstore Page`.
- [ ] Confirm one `h1`, two book-title `h2` headings, two descriptions and four displayed buttons.
- [ ] In **Developer Tools → Elements**, verify both `.card` nodes are children of `.card-container`.
- [ ] Verify all four `id` values are unique and their values match the source.
- [ ] Verify both book buttons and both lower buttons have the `.btn` class.
- [ ] Use Tab / Shift+Tab to check the four buttons are keyboard-focusable in source order.
- [ ] Notice that clicking these buttons has **no cart or checkout effect** without JavaScript/backend behavior.
- [ ] Inspect at narrow width; do **not** claim a designed responsive layout because the workshop intentionally contains no CSS.

**Verification boundaries:** the freeCodeCamp screenshot proves acceptance of the learner's submitted workshop code according to that exercise's tests. It does not prove functional commerce, visual card styling, production deployment, cross-browser or WCAG conformance.

## Connection to earlier exercises

- **Workshop 01:** heading hierarchy and paragraphs; applied here to a set of book descriptions.
- **Lab 01:** correctly nested tags; essential for card/group parent–child relationships.
- **Lab 02:** meaning and role of attributes; here the focus is on `class` and `id` instead of `src` and `href`.
- **Workshop 02:** full HTML document and semantic grouping; contrast a semantic `section` with a neutral `div`.
- **Lab 03:** constructing a page from requirements; contrast recipe `ul`/`ol` and bookstore content containers.

## Further study

Read [REVIEW.md](./REVIEW.md) for detailed explanations, phonetic vocabulary, comparison tables, accessibility notes and **unanswered self-check questions**. Broader connections are recorded in [RWD_REVIEW.md](../../RWD_REVIEW.md).

No completion dates, Python tests, build-system configuration or helper scripts are part of this archive.
