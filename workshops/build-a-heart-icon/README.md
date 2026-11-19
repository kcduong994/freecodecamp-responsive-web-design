# Workshop 06 — Build a Heart Icon

> **Curriculum:** [freeCodeCamp — Responsive Web Design V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/)
> **Area:** HTML → Basic HTML
> **Activity:** [Build a Heart Icon](https://www.freecodecamp.org/learn/responsive-web-design-v9/workshop-build-a-heart-icon/step-1)
> **Evidence:** Learner's Step 6 screenshot shows **100% complete** and **"Congratulations. Your code passes."**
> **Status:** Completed in the freeCodeCamp workshop; browser and assistive-technology testing are separate.

## Objective / Mục tiêu

Create a small red heart using **inline SVG** (*Scalable Vector Graphics* /ˈskeɪ.lə.bəl ˈvek.tə ˈɡræf.ɪks/, đồ họa vector có thể mở rộng). Learn how an SVG viewport, internal coordinate system, fill colour and path geometry work together.

This is the learner's final submitted HTML, not a CSS icon, image download or JavaScript application.

## Files

- [`index.html`](./index.html) — complete standalone page, including the SVG and its path.
- [`README.md`](./README.md) — activity context, implementation and evidence boundaries.
- [`REVIEW.md`](./REVIEW.md) — detailed conceptual review, pronunciation and self-study prompts.

## Completed markup

```html
<svg width="24" height="24" viewBox="0 0 24 24" fill="red">
  <path
    d="M12 21s-6-4.35-9.33-8.22C-.5 7.39 3.24 1 8.4 4.28 10.08 5.32 12 7.5 12 7.5s1.92-2.18 3.6-3.22C20.76 1 24.5 7.39 21.33 12.78 18 16.65 12 21 12 21z"
  ></path>
</svg>
```

## What the exercise practices

| Construct | Actual role in the submitted source |
| --- | --- |
| `<svg>` | Creates an inline vector graphic within the HTML document. |
| `width="24"` | Specifies an SVG viewport width of 24 CSS pixels in this context. |
| `height="24"` | Specifies an SVG viewport height of 24 CSS pixels. |
| `viewBox="0 0 24 24"` | Maps an internal coordinate region beginning at (0, 0), 24 units wide and 24 units high. |
| `fill="red"` | Supplies a red fill to the descendant path through SVG presentation-property inheritance. |
| `<path d="...">` | Describes the heart contour using compact path commands and coordinates. |
| `</path>` | An explicit closing tag, as used in the original submission. |

**Key distinction:** `viewBox` establishes the internal drawing coordinates; `width` and `height` determine the element's displayed viewport. They are related but not interchangeable. The path data is *geometry*, not a downloaded bitmap.

## Preview and verification

1. Open `index.html` in a browser. A small red heart should appear near the start of the document body.
2. Inspect `<svg>` and `<path>` using browser Developer Tools → Elements.
3. Change the viewport width and height **temporarily** in Developer Tools to investigate scaling; leave the committed source as submitted.
4. Compare `fill="red"` with a different colour in Developer Tools to observe the SVG fill property.
5. Optional extension: test how to provide an accessible text alternative to a meaningful icon; such markup was **not** part of the submitted workshop.

**Verified by the learner's screenshot:** the freeCodeCamp checker accepted Step 6 and reported **100%**. **Not independently verified:** rendering in multiple browsers, exact pixel appearance at different zoom levels, assistive-technology output or a complete accessibility audit.

## Connections and boundaries

- Earlier HTML work introduced document structure, attributes and the distinction between elements and visible output. SVG reuses a tag-and-attribute syntax but describes shapes rather than ordinary prose.
- Unlike an `<img src="...">`, this icon contains its vector geometry directly in the document; it does not require fetching an external image file.
- The heart is static: the source includes **no external libraries, CSS, JavaScript, animation or interaction**.
- For interface use, the icon might be decorative or meaningful; its accessible label or hiding strategy depends on that usage. Do not claim that completing this workshop alone makes it accessible.

Continue with the [conceptual review](./REVIEW.md) and the repository-wide [cumulative review](../../RWD_REVIEW.md).

**Repository conventions:** no completion dates, Python tests, generated helper scripts or binary assets are committed.
