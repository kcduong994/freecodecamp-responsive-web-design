# Debug a Pet Adoption Page

> **Curriculum:** freeCodeCamp — Responsive Web Design Certification V9  
> **Track:** HTML → Basic HTML  
> **Activity:** Independent debugging lab  
> **Status:** **Completed — 100%**, all five freeCodeCamp checks passed  
> **Evidence:** Learner-supplied screenshots dated **2026-11-13**; “Congratulations. Your code passes.” and five passed checks are visible.  
> **Exercise:** [Debug a Pet Adoption Page](https://www.freecodecamp.org/learn/responsive-web-design-v9/lab-debug-pet-adoption-page/lab-debug-pet-adoption-page)

## Objective

Fix image and hyperlink markup in a small pet-adoption webpage while preserving the original headings, text, image URL and two route strings. This exercise introduces the distinction among **`src`** (resource to embed), **`alt`** (text alternative for an image) and **`href`** (link destination), together with the **void-element** nature of `img`.

The source in `index.html` preserves the final visible result from the learner's code editor. To make this a standalone file, the archive also includes HTML5 document scaffolding (`DOCTYPE`, `html`, `head`, metadata and `body`). That wrapper is a **packaging improvement**, not an additional freeCodeCamp requirement.

## Files

```text
labs/debug-pet-adoption-page/
├── index.html                    # Final HTML, browser-openable
├── README.md                     # Requirements, evidence and verification
├── REVIEW.md                     # Concepts, IPA glossary, self-assessment
├── tests/
│   └── test_html.py              # Dependency-free Python source tests
└── tools/
    └── update_root_docs.py      # Opt-in, additive root-doc update
```

## Five defects corrected

| Check | Incorrect starter markup | Corrected form | Why |
| --- | --- | --- | --- |
| 1 | `img` with `href` | `img src="..."` | An image's URL is specified with `src` |
| 2 | `img` with `att` | `img alt="..."` | `alt` supplies its text alternative |
| 3 | Extra `</img>` | Remove `</img>` | `img` is a void element; it has no closing tag |
| 4 | Cat link with `src` | `<a href="/cats">...` | An anchor navigates via `href` |
| 5 | Dog link with `src` | `<a href="/dogs">...` | Same rule for the dog route |

The screenshot confirms **five passed freeCodeCamp tests**, but does not establish an external accessibility audit or the presence of working local `/cats` and `/dogs` pages.

## What is preserved exactly

- Heading: `Welcome to XYZ Pet Adoption!`
- Introductory paragraph: `Consider adopting a pet today. We have cats, dogs, rabbits and more.`
- Three `h2` headings: `See our cats!`, `Adopt a cat!`, `Adopt a dog!`
- Image address: `https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg`
- Image alternative text: `Two tabby kittens sleeping together on a couch.`
- Links: `Visit cats page` → `/cats`; `Visit dogs page` → `/dogs`

**Important:** `href="/cats"` and `href="/dogs"` are **root-relative** URLs. When opened as a local `file://` HTML file, or served from a minimal localhost server without matching routes, clicking the links may lead to a missing page. This does **not** invalidate the freeCodeCamp task; do not invent local routes or change the official strings just to make the links appear functional in an isolated archive.

The external image needs an internet connection and access to the freeCodeCamp CDN. The archive does not bundle or republish the image.

## Run locally

Open `index.html` in a modern browser. The page itself requires no Node.js, build tool, CSS or JavaScript.

Run the self-contained HTML structure tests from the **repository root**:

```powershell
py -m unittest discover -s labs/debug-pet-adoption-page/tests -p "test_*.py" -v
```

On systems without the Windows `py` launcher, use `python` instead. The test suite checks exact text, structure, image attributes, link attributes, absence of `</img>`, and document metadata. It **does not** make network requests or evaluate screen-reader behavior, CSS, or route availability.

Optional manual inspection: open DevTools → Elements and inspect `img` and `a`. Check that the image has a meaningful `alt`; inspect the actual `href` destinations separately from whether the target routes exist.

## Documentation update

After extracting this folder into the repository, run the **opt-in additive updater** from the repository root:

```powershell
py labs/debug-pet-adoption-page/tools/update_root_docs.py
```

It adds Lab 02 to the existing root `README.md` and `RWD_REVIEW.md` **without replacing the preceding lessons**. It checks expected anchors and refuses ambiguous edits. Review `git diff` before staging; do not run on an unreviewed or dirty working tree.

## Evidence status

- **freeCodeCamp:** 100% and five checks passed, confirmed by learner screenshots (2026-11-13).
- **Source tests:** available in `tests/test_html.py`; an independently run result should be recorded separately.
- **Standalone preview, external CDN and local target routes:** not independently audited.
- **Next curriculum item:** follow the next item actually displayed by freeCodeCamp; no later activity is marked complete here.

Study notes and unanswered self-assessment questions: [REVIEW.md](./REVIEW.md).
