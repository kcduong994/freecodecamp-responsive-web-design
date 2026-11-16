# Lab 03 — Build a Recipe Page

> **Course:** [freeCodeCamp — Responsive Web Design V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/) → Basic HTML
> **Type:** Independent lab
> **Status:** Completed on freeCodeCamp in the original learner submission (**100%**). The archived version contains minor editorial and image improvements that have **not** been re-submitted to freeCodeCamp.
> **Activity:** [Build a Recipe Page](https://www.freecodecamp.org/learn/responsive-web-design-v9/lab-recipe-page/build-a-recipe-page)

## Objective

Build an HTML-only recipe page from a blank editor. Unlike a guided workshop, this lab requires translating **user stories** into the correct document structure and ordered content. The learner chose **Fish Recipe** as the original topic and passed the official checks.

The original freeCodeCamp solution was intentionally minimal: its paragraph was “This is a good meal”; the ingredients were `water`, `salt`, `oil`, `pepper`; the four procedure items were `cook1`–`cook4`; and the image had `src="abcd.com/fish.jpg"`. The screenshot shows **100% code-check completion** but a broken image in Preview. The final source in this repository is a lightly polished archive, not an exact byte-for-byte copy of that screenshot.

## What was improved — without changing the lesson scope

| Aspect | Learner's passing submission | Archived edition | Reason |
| --- | --- | --- | --- |
| Recipe | Fish Recipe | **Fish Recipe** | Preserve topic and main title |
| Introduction | “This is a good meal” | One-sentence explanation of pan-fried fish | Meaningful paragraph |
| Ingredients | Water, salt, oil, pepper | Fish fillets, oil, salt, pepper, lemon | Realistic ingredient list (5 items) |
| Instructions | `cook1`–`cook4` | 5 practical preparation/cooking steps | Meaningful ordered procedure |
| Image | `abcd.com/fish.jpg` | Wikimedia Commons fish-fillet photograph | Replace visibly broken source with a real, relevant image URL |
| Structure | Valid HTML5 skeleton | Same skeleton, headings, `ul`, `ol`, `img` | Retain freeCodeCamp acceptance requirements |

**Image provenance:** [Fried Fish Fillet.JPG](https://commons.wikimedia.org/wiki/File:Fried_Fish_Fillet.JPG) by **Miansari66**, dedicated to the public domain under **CC0 1.0**. The page embeds a 960px Wikimedia thumbnail remotely; it does not copy an image into the repository. The source and its license were checked, but whether the remote thumbnail loads in the learner's own browser is not independently verified.

## Source structure

```text
labs/build-a-recipe-page/
├── index.html
├── README.md
└── REVIEW.md
```

```text
html (lang="en")
├── head
│   ├── meta (charset="UTF-8")
│   └── title (Fish Recipe)
└── body
    ├── h1 (Fish Recipe)
    ├── p  (introduction)
    ├── h2 (Ingredients)
    ├── ul → 5 li items
    ├── h2 (Instructions)
    ├── ol → 5 li steps
    └── img (src, alt, dimensions)
```

## Requirements mapped to the archive

- `<!DOCTYPE html>`, `<html lang="en">`, `<head>`, `<title>`, `<meta charset="UTF-8">`, and `<body>`.
- Exactly one `<h1>` containing the recipe name.
- An introductory `<p>` immediately after the heading.
- Two `<h2>` elements with the exact texts **Ingredients** and **Instructions**.
- An unordered ingredients list (`ul`) containing **at least four** `li` items.
- An ordered procedure (`ol`) containing **at least four** `li` items.
- An image (`img`) with a meaningful `alt` and a real HTTPS source URL.

These conditions are satisfied by source inspection. The **edited archive has not been independently run through freeCodeCamp**. Completing the challenge and confirming every external image loads are distinct quality checks.

## Local viewing and manual review

1. Open `index.html` directly in a browser; no build process, CSS, JavaScript, Python or package manager is required.
2. Check the document tab title and visible heading.
3. Verify that `Ingredients` uses bullets and `Instructions` uses sequential numbering.
4. Open **Developer Tools → Elements** to inspect the `head`/`body` nesting, two `h2` headings, lists and the `img` attributes.
5. With internet access, confirm the image loads. If it does not, examine **Developer Tools → Network**; external hosts may be inaccessible even when HTML is correctly structured.
6. For optional further study, paste the archived source into the freeCodeCamp challenge and run its own tests again. Treat that result as separate from the original 100% screenshot.

## Scope and review

This is an **HTML fundamentals** exercise, not a complete food-safety guide or styled production recipe website. There is no CSS, JavaScript, form, database or deployed backend. The fish cooking instructions are illustrative; thickness and cooking method affect cooking times.

Continue with [REVIEW.md](./REVIEW.md) for conceptual analysis, UK English IPA vocabulary, common failure modes and self-assessment questions. See [the cumulative review](../../RWD_REVIEW.md) for the connections to earlier labs and workshops.
