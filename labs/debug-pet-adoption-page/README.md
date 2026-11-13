# Lab 02 — Debug a Pet Adoption Page

> **Curriculum:** freeCodeCamp Responsive Web Design V9 → Basic HTML  
> **Type:** Independent debugging lab  
> **Status:** Completed — **5/5 freeCodeCamp checks passed**  
> **Official activity:** [Debug a Pet Adoption Page](https://www.freecodecamp.org/learn/responsive-web-design-v9/lab-debug-pet-adoption-page/lab-debug-pet-adoption-page)

## Objective

Fix a small pet-adoption page so that its image displays and its two anchor elements use the correct URL attributes. Preserve the original visible text, image address and link destinations.

This exercise introduces the roles of **`src`**, **`alt`**, **`href`**, the difference between an image and a link, and the reason an `img` element has no closing tag.

## Files

```text
labs/debug-pet-adoption-page/
├── index.html
├── README.md
└── REVIEW.md
```

## Errors corrected

| # | Original defect | Correct use | Reason |
| ---: | --- | --- | --- |
| 1 | `img` used `href` | `img src="..."` | `src` provides the image resource |
| 2 | `img` used `att` | `img alt="..."` | `alt` is the text alternative attribute |
| 3 | Unnecessary `</img>` | Omit the closing tag | `img` is a void element |
| 4 | Cat anchor used `src` | `<a href="/cats">` | `href` identifies the link target |
| 5 | Dog anchor used `src` | `<a href="/dogs">` | An anchor navigates using `href` |

## Completed page content

- `h1`: **Welcome to XYZ Pet Adoption!**
- Introductory paragraph: **Consider adopting a pet today. We have cats, dogs, rabbits and more.**
- `h2`: **See our cats!**
- Image source: `https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg`
- Image alternative text: **Two tabby kittens sleeping together on a couch.**
- `h2`: **Adopt a cat!** with anchor `Visit cats page` pointing to `/cats`
- `h2`: **Adopt a dog!** with anchor `Visit dogs page` pointing to `/dogs`

The source is archived in [`index.html`](./index.html). The additional HTML5 document wrapper is for convenient local viewing, not a separate requirement of the exercise.

## Important details

### Why `img` does not use `</img>`

`img` is a **void element**: it does not contain child elements or text content. HTML does not use a closing `</img>` tag. In contrast, the anchor element encloses link text, so it has an opening tag and a closing `</a>`.

### What `alt` means

The `alt` attribute provides text that conveys the purpose or relevant information of the image. It is valuable for accessibility and can also be useful when the image does not load. It is not simply a tooltip.

### Why a valid link may fail locally

The `/cats` and `/dogs` values are **root-relative paths**. They are preserved exactly as required. Opening the file locally does not automatically create server routes at those paths. A link can have syntactically correct HTML while the destination is unavailable.

The cat image is hosted externally; displaying it requires access to the freeCodeCamp CDN.

## View and inspect

Open `index.html` in a browser. Confirm the headings, cat photograph and clickable link text. Use **Developer Tools → Elements** to examine `img[src][alt]` and `a[href]`. If a resource or destination does not load, use the browser's Network panel to distinguish URL availability from markup correctness.

The freeCodeCamp checks for this lab have passed. This does not, by itself, mean the page has received a complete accessibility or cross-browser audit.

## Learning outcomes

- Match an HTML attribute to its element's role.
- Explain why `src`, `alt` and `href` are not interchangeable.
- Correctly write an `img` void element and a text-containing `a` element.
- Distinguish an absolute resource URL from root-relative navigation paths.
- Explain the difference between valid HTML, available resources and accessible content.

See [REVIEW.md](./REVIEW.md) for detailed theory, English IPA, common errors and independent questions. See [RWD_REVIEW.md](../../RWD_REVIEW.md) for connections to other lessons.
