"""Add Lab 02 to repository-wide docs without discarding previous lessons.

Run from the root of kcduong994/freecodecamp-responsive-web-design:
    py labs/debug-pet-adoption-page/tools/update_root_docs.py

This updater is intentionally conservative:
- It does not touch workshop files or earlier lab files.
- It requires matching documentation anchors from the expected main branch.
- It is idempotent when both documents already contain Lab 02.
- It prepares both documents in memory before writing either.
- It makes no Git commits or remote network calls.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
README = ROOT / "README.md"
REVIEW = ROOT / "RWD_REVIEW.md"
LAB = ROOT / "labs" / "debug-pet-adoption-page" / "index.html"


def replace_one(text: str, previous: str, updated: str, name: str) -> str:
    count = text.count(previous)
    if count != 1:
        raise ValueError(f"{name}: expected exactly one match, found {count}: {previous[:75]!r}")
    return text.replace(previous, updated, 1)


def add_completed_lab_row(text: str) -> str:
    pattern = r"(?m)^(\| 02 \| HTML · Lab · \*\*Debug Camperbot's Profile Page\*\* \|[^\n]*\|)$"
    matches = list(re.finditer(pattern, text))
    if len(matches) != 1:
        raise ValueError("README.md: expected exactly one completed Lab 01 row")
    row = (
        "| 03 | HTML · Lab · **Debug a Pet Adoption Page** | "
        "[Open lab](./labs/debug-pet-adoption-page/) | "
        "Fix `img` / `a` attributes: `src`, `alt`, `href`; remove invalid `</img>` | "
        "**freeCodeCamp 5/5 passed, 100%** (2026-11-13 screenshot); "
        "**11/11 packaged source tests passed in preparation**; Windows rerun pending |"
    )
    return text[:matches[0].end()] + "\n" + row + text[matches[0].end():]


def update_readme(original: str) -> str:
    if "## Lab 02 — learning record" in original:
        print("README.md: Lab 02 already present; leaving unchanged")
        return original
    t = original
    t = replace_one(
        t,
        "> **Latest completed activity:** Lab 01 — Debug Camperbot's Profile Page (2026-11-11)",
        "> **Latest completed activity:** Lab 02 — Debug a Pet Adoption Page (2026-11-13)",
        "README.md",
    )
    t = replace_one(
        t,
        "> **Evidence:** Workshop 01 (2026-11-10) and Lab 01 (2026-11-11) completed in freeCodeCamp; local Lab 01 source tests archived for verification.",
        "> **Evidence:** Workshop 01 (2026-11-10), Lab 01 (2026-11-11), and Lab 02 (2026-11-13) completed in freeCodeCamp; source tests and status recorded separately.",
        "README.md",
    )
    t = replace_one(t, "**Verified snapshot: 11 November 2026.**", "**Verified snapshot: 13 November 2026.**", "README.md")
    t = replace_one(
        t,
        "| Labs | **1 completed** | [Debug Camperbot's Profile Page](./labs/debug-camperbots-profile-page/README.md): **100%**, freeCodeCamp screenshot (2026-11-11) |",
        "| Labs | **2 completed** | [Camperbot's Profile Page](./labs/debug-camperbots-profile-page/README.md): 100% (2026-11-11); [Pet Adoption Page](./labs/debug-pet-adoption-page/README.md): 5/5 tests, 100% (2026-11-13) |",
        "README.md",
    )
    t = add_completed_lab_row(t)
    t = replace_one(
        t,
        "Lab 01's eight additional tests are included in the source package and must be run separately.",
        "Lab 01's eight additional tests are included in the source package and must be run separately. Lab 02's source test suite passed **11/11 checks** in the generated package; rerun it on Windows before recording a machine-local result.",
        "README.md",
    ) if "Lab 01's eight additional tests are included in the source package and must be run separately." in t else t
    lab_section = """## Lab 02 — learning record

- [HTML source: `index.html`](./labs/debug-pet-adoption-page/index.html)
- [Lab README: five defects, corrections and evidence](./labs/debug-pet-adoption-page/README.md)
- [Lab REVIEW: image/anchor attributes, UK IPA and practice questions](./labs/debug-pet-adoption-page/REVIEW.md)
- [Local test suite: `tests/test_html.py`](./labs/debug-pet-adoption-page/tests/test_html.py)
- [Cumulative concepts: Lab 02](./RWD_REVIEW.md#lab-02--html-image-and-link-attributes)

**FreeCodeCamp result:** five checks passed, 100% (screenshots dated 2026-11-13). The archived HTML adds standalone document scaffolding without changing the visible text, cat-image URL, or `/cats` and `/dogs` link destinations. Those paths may not be served when the page is opened locally; this does not invalidate the HTML exercise.

"""
    t = replace_one(t, "## Repository structure\n", lab_section + "## Repository structure\n", "README.md")
    t = replace_one(
        t,
        "│   └── debug-camperbots-profile-page/",
        "│   ├── debug-camperbots-profile-page/",
        "README.md",
    )
    tree_section = """│           └── test_html.py
│   └── debug-pet-adoption-page/
│       ├── index.html
│       ├── README.md
│       ├── REVIEW.md
│       ├── tests/
│       │   └── test_html.py
│       └── tools/
│           └── update_root_docs.py
└── certification-projects/"""
    t = replace_one(t, "│           └── test_html.py\n└── certification-projects/", tree_section, "README.md")
    t = replace_one(
        t,
        'py -m unittest discover -s labs/debug-camperbots-profile-page/tests -p "test_*.py" -v\n```',
        'py -m unittest discover -s labs/debug-camperbots-profile-page/tests -p "test_*.py" -v\n```\n\nRun the new Lab 02 suite:\n\n```powershell\npy -m unittest discover -s labs/debug-pet-adoption-page/tests -p "test_*.py" -v\n```',
        "README.md",
    )
    t = replace_one(
        t,
        "**Each suite contains eight tests.**",
        "**Workshop 01 and Lab 01 each contain eight tests; Lab 02 contains eleven.**",
        "README.md",
    )
    t = replace_one(
        t,
        "| HTML content and accessibility | Attributes, links, images, lists, tables, forms, semantic elements | Planned |",
        "| HTML content and accessibility | Attributes, links, images, lists, tables, forms, semantic elements | **Lab 02: `src`, `href`, `alt`, images and links introduced**; remaining topics planned |",
        "README.md",
    )
    t = replace_one(
        t,
        "| Project quality | Debugging, accessibility checks, browser developer tools and validation | **Lab 01: syntax debugging introduced**; broader quality checks planned |",
        "| Project quality | Debugging, accessibility checks, browser developer tools and validation | **Lab 01: tag debugging; Lab 02: attribute and void-element debugging**; broader audits planned |",
        "README.md",
    )
    t = replace_one(
        t,
        "The **next visible activity** after Lab 01 is *Understanding HTML Attributes* (theory); this is not yet claimed as completed.",
        "Lab 02 is complete. No completion is claimed for the *Understanding HTML Attributes* theory section or any later curriculum activity without separate evidence.",
        "README.md",
    )
    t = replace_one(
        t,
        "*Last documentation update: 2026-11-11. Lab 01 local tests are included for reproducibility; Windows execution should be recorded after verification.*",
        "*Last documentation update: 2026-11-13. Lab 02 source tests passed during package preparation; Windows-local verification and remote GitHub push require separate evidence.*",
        "README.md",
    )
    return t


LAB_SUMMARY = """## Lab 02 — HTML image and link attributes

**Exercise:** [Debug a Pet Adoption Page](./labs/debug-pet-adoption-page/) — **5/5 freeCodeCamp checks passed, 100%** in learner screenshots dated **2026-11-13**. This is separate from running source tests locally and from a browser accessibility audit.

### 1. What did we learn?

**Learned:** a correct HTML element still needs the **appropriate attribute name** for the intended behavior. The five corrected issues were `href → src` for the image resource, `att → alt` for the image text alternative, removing invalid `</img>`, and `src → href` for **each** of the two anchor links. The image URL and two link targets `/cats`, `/dogs` were preserved.

### 2. What does the browser receive?

An `img` tag with `src` and `alt`, and two `a` elements with `href`. The local archive includes optional HTML5 scaffolding not shown in the freeCodeCamp lab fragment. The image URL is a full HTTPS URL; `/cats` and `/dogs` are root-relative targets.

### 3. What does the browser do?

**Explained:** `img[src]` identifies an image resource to fetch; `alt` supplies the text alternative. The `img` element is **void** and cannot enclose children or take a `</img>` end tag. By contrast, `a[href]` creates a hyperlink destination. Giving an anchor a `src` does not substitute for its `href`.

```text
<img src="..." alt="...">  → embedded image + text alternative
<a href="/cats">...</a>    → hyperlink destination
```

**Extension:** a valid `href="/cats"` is not evidence that the current server actually implements `/cats`. Similarly, a correct `src` does not guarantee a successful response from an external image server. Distinguish source semantics, network availability and rendered appearance.

### 4. What does the user experience?

After correction, the cats photograph appears in the supplied freeCodeCamp preview and the cat/dog labels become ordinary hyperlinks. The image's meaningful `alt` provides a text alternative for users and tools that cannot use the visual image. It should be appropriate to context, not a random filename.

### 5. What can fail?

| Problem | Example | Diagnosis |
| --- | --- | --- |
| Incorrect image source attribute | `img href` | Inspect `src` and network request |
| Invalid text alternative name | `att` | Check for `alt`, and whether its wording fits the image |
| Invalid void-element end tag | `</img>` | Remove the closing tag |
| Wrong anchor attribute | `a src` | Use `href` |
| Correct markup but missing destination | `href="/dogs"` on a server without `/dogs` | Check route resolution independently |
| False confidence from automated tests | “5/5 means fully accessible” | Separate curriculum, source, network and accessibility checks |

### 6. How do we verify it?

**Official:** 5/5 user stories passed, 100% in freeCodeCamp. **Packaged source:** a dependency-free Python suite checks exact HTML/text, image URL and `alt`, both `href` paths, no invalid closing tag, and basic structure. The suite ran 11/11 successfully in the preparation environment; a Windows result must be independently verified on the learner's machine. **Not established:** CDN uptime, working local routes, keyboard/screen-reader usability or cross-browser compatibility.

```powershell
py -m unittest discover -s labs/debug-pet-adoption-page/tests -p "test_*.py" -v
```

**Vocabulary and practice:** the lab-specific [REVIEW.md](./labs/debug-pet-adoption-page/REVIEW.md) contains IPA pronunciations, explanation of image alternatives and ten unanswered self-assessment questions.

**Conceptual progression:** Workshop 01 introduced elements and headings; Lab 01 corrected broken tag syntax; Lab 02 corrects **attributes** and introduces **void elements**. These are distinct aspects of HTML correctness.

---

"""


def update_review(original: str) -> str:
    if "## Lab 02 — HTML image and link attributes" in original:
        print("RWD_REVIEW.md: Lab 02 already present; leaving unchanged")
        return original
    t = original
    t = replace_one(
        t,
        "> **Status:** **In progress** — Workshop 01 (2026-11-10) and Lab 01 (2026-11-11) documented.",
        "> **Status:** **In progress** — Workshop 01 (2026-11-10), Lab 01 (2026-11-11) and Lab 02 (2026-11-13) documented.",
        "RWD_REVIEW.md",
    )
    t = replace_one(
        t,
        "> **Evidence:** Workshop 01 committed at [`83af1c7`](https://github.com/kcduong994/freecodecamp-responsive-web-design/commit/83af1c7d02ab4c835c1ce78d1feac82ce4150bdb); Lab 01 passed on freeCodeCamp in learner screenshot (2026-11-11).",
        "> **Evidence:** Workshop 01 committed at [`83af1c7`](https://github.com/kcduong994/freecodecamp-responsive-web-design/commit/83af1c7d02ab4c835c1ce78d1feac82ce4150bdb); Lab 01 passed (2026-11-11); Lab 02 passed 5/5 checks, 100% (2026-11-13). These results are from learner-supplied freeCodeCamp screenshots.",
        "RWD_REVIEW.md",
    )
    t = replace_one(
        t,
        "| 02 | HTML attributes and document boilerplate | **Planned** | Some standalone scaffolding was added to Workshop 01's archived file; this does not constitute completion of the theory lessons |",
        "| 02 | HTML attributes and document boilerplate | **Partial practical introduction** | [Lab 02](./labs/debug-pet-adoption-page/): `src`, `alt`, `href`; boilerplate and theory lessons not yet verified |",
        "RWD_REVIEW.md",
    )
    t = replace_one(
        t,
        "| 03 | Links, images, lists, semantic sections, tables and forms | **Planned** | No completed repository exercises |",
        "| 03 | Links, images, lists, semantic sections, tables and forms | **Images and links introduced** | Lab 02 covers an image and two links; other subjects remain planned |",
        "RWD_REVIEW.md",
    )
    t = replace_one(
        t,
        "| 07 | Debugging, accessibility, browser tools and project verification | **Develop gradually** | Lab 01 introduces HTML syntax debugging; full accessibility and browser audits planned |",
        "| 07 | Debugging, accessibility, browser tools and project verification | **Develop gradually** | Lab 01 fixes tag syntax; Lab 02 fixes attributes/void-element usage. Full audits remain planned |",
        "RWD_REVIEW.md",
    )
    t = replace_one(t, "## Future chapters — pending curriculum work", LAB_SUMMARY + "## Future chapters — pending curriculum work", "RWD_REVIEW.md")
    t = replace_one(
        t,
        "### Chapter 02 — HTML attributes and boilerplate\n\nAttributes and attribute values; document type, language, head metadata, title and viewport; correct use and common errors.",
        "### Chapter 02 — HTML attributes and boilerplate (partial introduction only)\n\nLab 02 introduced `src`, `alt` and `href` in practice. Full attribute theory, document type, language, head metadata, title and viewport remain to be studied and independently verified.",
        "RWD_REVIEW.md",
    )
    t = replace_one(
        t,
        "### Chapter 03 — HTML content, structure and accessibility\n\nLinks, image alternatives, lists, semantic landmarks, tables, forms, labels, validation and navigation behavior.",
        "### Chapter 03 — HTML content, structure and accessibility (partial introduction only)\n\nLab 02 introduced a basic image, alternative text and two links. Lists, semantic landmarks, tables, forms, labels, systematic validation and advanced navigation remain planned.",
        "RWD_REVIEW.md",
    )
    return t


def main() -> int:
    if not (README.is_file() and REVIEW.is_file() and LAB.is_file()):
        print("ERROR: Run with Lab 02 extracted under the original repository structure.", file=sys.stderr)
        return 2
    old_r = README.read_text(encoding="utf-8")
    old_v = REVIEW.read_text(encoding="utf-8")
    try:
        new_r = update_readme(old_r)
        new_v = update_review(old_v)
    except ValueError as exc:
        print(f"ERROR: Documentation has changed; no files written. {exc}", file=sys.stderr)
        return 3
    if new_r != old_r:
        README.write_text(new_r, encoding="utf-8", newline="\n")
        print("UPDATED: README.md (Lab 02 progress, links, tests and directory tree)")
    if new_v != old_v:
        REVIEW.write_text(new_v, encoding="utf-8", newline="\n")
        print("UPDATED: RWD_REVIEW.md (Lab 02 conceptual synthesis)")
    if new_r == old_r and new_v == old_v:
        print("No changes required: Lab 02 already documented")
    print("Review: git diff -- README.md RWD_REVIEW.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
