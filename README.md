# freeCodeCamp — Responsive Web Design

> **Curriculum:** [Responsive Web Design Certification V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/)
> **Status:** In progress
> **Current track:** HTML → Basic HTML
> **Learning approach:** Study → Practice → Explain → Review → Advance

## Purpose

This repository is a structured record of my work through freeCodeCamp's **Responsive Web Design V9** curriculum. It preserves the HTML/CSS source created in workshops, labs and certification projects, together with technical explanations and self-assessment material.

The goal is to understand how HTML and CSS work—not simply to pass tests: connect source code to document structure, browser interpretation, user experience, accessibility and engineering practice. Longer-term applications include coastal engineering, scientific communication, environmental data presentation and engineering web interfaces.

This repository is distinct from my Back-End Development and APIs coursework.

## Learning method

Follow the official curriculum in order:

1. **Theory** — study each concept on freeCodeCamp; no separate source file is required for every theory page.
2. **Workshop** — follow the guided steps; archive the completed HTML and the concepts learned.
3. **Lab** — independently implement or debug the user stories; preserve the final source and reasoning.
4. **Review** — explain mechanisms, typical errors and manual checks; answer questions from recall to independent design.
5. **Certification projects** — complete the required projects and verify their acceptance criteria before recording completion.
6. **Final synthesis** — critically revise the cumulative [RWD_REVIEW.md](./RWD_REVIEW.md) after practical coursework.

The repository emphasizes **HTML/CSS source and documentation**, not auxiliary scripts or generated artifacts. Use the freeCodeCamp checker, browser preview and Developer Tools, while recognizing what each actually verifies.

## Learning progress

| Area | Progress | Notes |
| --- | ---: | --- |
| Workshops | **8 completed** | Build a Curriculum Outline (**11/11**); Build a Cat Photo App (**42/42**); Build a Bookstore Page (**19/19**); Build an HTML Music Player (**9/9**); Build an HTML Video Player (**13/13**); Build a Heart Icon (**6/6**); Build a Video Display Using iframe (**7/7**); Build a List of Major Web Browsers (**7/7**) |
| Labs | **6 completed** | Debug Camperbot's Profile Page; Debug a Pet Adoption Page; Build a Recipe Page; Build a Travel Agency Page; Build an HTML Audio and Video Player (**18/18**); Build a Video Compilation Page (completion marker; reconstructed archive) |
| Certification projects | **0 / 5** | Not started |
| Cumulative review | **In progress** | [RWD_REVIEW.md](./RWD_REVIEW.md) synthesizes fourteen practical activities |
| Final course review | Not complete | Revisit after practical work |
| Certification exam | Not attempted | Awaiting required coursework |
| Certificate | Not issued | Record only when earned |

### Completed activities

| # | Type | Activity | Core concepts | Source |
| ---: | --- | --- | --- | --- |
| 01 | Workshop | Build a Curriculum Outline | HTML elements, `h1`–`h3`, `p`, heading hierarchy | [Open](./workshops/build-a-curriculum-outline/) |
| 02 | Lab | Debug Camperbot's Profile Page | Correct tag names and closing syntax; browser error recovery | [Open](./labs/debug-camperbots-profile-page/) |
| 03 | Lab | Debug a Pet Adoption Page | `img`, `a`, `src`, `alt`, `href`, void elements | [Open](./labs/debug-pet-adoption-page/) |
| 04 | Workshop | Build a Cat Photo App | Full document; `head`, `main`, `section`, `footer`; lists; figures/captions; emphasis; charset | [Open](./workshops/build-a-cat-photo-app/) |
| 05 | Lab | **Build a Recipe Page** | HTML document hierarchy; translating user stories to code; `ul` vs `ol`; image loading vs code checks | [Open](./labs/build-a-recipe-page/) |
| 06 | Workshop | **Build a Bookstore Page** | Generic `div` grouping; `class` reuse, unique `id`; nested book cards; native buttons vs application behavior | [Open](./workshops/build-a-bookstore-page/) |
| 07 | Lab | **Build a Travel Agency Page** | SEO description metadata; `ul > li > a`; `figure > a > img` and `figcaption`; exact link attributes; real image requests | [Open](./labs/build-a-travel-agency-page/) |
| 08 | Workshop | **Build an HTML Music Player** | Native `audio`, `src`, Boolean `controls`/`loop`; MP3 resources, track headings, viewport metadata | [Open](./workshops/build-an-html-music-player/) |
| 09 | Workshop | **Build an HTML Video Player** | Native `video`; multiple `source` candidates and MIME hints; `controls`, `loop`, `muted`, `poster`, width | [Open](./workshops/build-an-html-video-player/) |
| 10 | Lab | **Build an HTML Audio and Video Player** | `section` hierarchy; native `video > source` and `audio` playback; direct media URLs and MIME type; code acceptance versus real playback | [Open](./labs/build-an-html-audio-and-video-player/) |
| 11 | Workshop | **Build a Heart Icon** | Inline SVG, `path` geometry, `viewBox`, `fill`, and vector sizing | [Open](./workshops/build-a-heart-icon/) |
| 12 | Workshop | **Build a Video Display Using iframe** | Embedded third-party browsing context; YouTube `/embed/` URL; `allow`, `referrerpolicy`, `allowfullscreen` | [Open](./workshops/build-a-video-display-using-iframe/) |
| 13 | Lab | **Build a Video Compilation Page** | One `main` element; three `section` elements each with `h2`, `p`, and `iframe`; descriptive titles and dimensions | [Open](./labs/build-a-video-compilation-page/) |
| 14 | Workshop | **Build a List of Major Web Browsers** | `dl`, five `dt`/`dd` pairs, description semantics and browser defaults | [Open](./workshops/build-a-list-of-major-web-browsers/) |

**Evidence boundaries:** the learner's freeCodeCamp screenshots confirm the activities, including Workshop 02 (**42/42**) and the **original Recipe Page submission at 100%**, plus Workshop 03 **19/19 (100%)** and the **original Travel Agency Page at 100%**, plus **Workshop 04 (9/9 steps, 100%)** and **Workshop 05 (13/13 steps, 100%)**. The archived Recipe Page and Travel Agency Page sources are **revised editions**; their edited content has not been independently re-tested in freeCodeCamp or in the learner's browser. Code-check success does not establish cross-browser compliance, accessible behavior or resource availability.

**Lab 05 evidence:** The original HTML Audio and Video Player submission passed **18/18 checks (100%)**. The archived version replaces a relative MP3 path that displayed `0:00 / 0:00` in Preview with the freeCodeCamp-provided MP3 URL. The revised edition has not been independently resubmitted or browser-tested.

**Lab 06 evidence:** The freeCodeCamp learning dashboard shows Build a Video Compilation Page as completed. The original HTML was not supplied; the local archived source is a reconstructed example based on the 20 specified tests and has not been independently resubmitted.

**Workshop 06 evidence:** The Step 6 screenshot shows **6/6 (100%)** and "Congratulations. Your code passes." for the inline SVG heart. Browser accessibility and cross-browser behaviour have not been independently audited.

**Workshop 07 evidence:** The learner supplied the completed seven-step iframe source. The code archive retains the submitted attributes; more explicit `allow` permission separators, an iframe `title`, and responsive sizing are documented as optional improvements, not silently presented as the learner's final submission.

## Repository structure

```text
freecodecamp-responsive-web-design/
├── README.md
├── RWD_REVIEW.md
├── .gitignore
├── workshops/
│   ├── build-a-curriculum-outline/
│   │   ├── index.html
│   │   ├── README.md
│   │   └── REVIEW.md
│   ├── build-a-cat-photo-app/
│   │   ├── index.html
│   │   ├── README.md
│   │   └── REVIEW.md
│   ├── build-a-bookstore-page/
│   │   ├── index.html
│   │   ├── README.md
│   │   └── REVIEW.md
│   ├── build-an-html-music-player/
│   │   ├── index.html
│   │   ├── README.md
│   │   └── REVIEW.md
│   ├── build-an-html-video-player/
│   │   ├── index.html
│   │   ├── README.md
│   │   └── REVIEW.md
│   ├── build-a-heart-icon/
│   │   ├── index.html
│   │   ├── README.md
│   │   └── REVIEW.md
│   ├── build-a-video-display-using-iframe/
│   │   ├── index.html
│   │   ├── README.md
│   │   └── REVIEW.md
│   └── build-a-list-of-major-web-browsers/
│       ├── index.html
│       ├── README.md
│       └── REVIEW.md
├── labs/
│   ├── debug-camperbots-profile-page/
│   │   ├── index.html
│   │   ├── README.md
│   │   └── REVIEW.md
│   ├── debug-pet-adoption-page/
│   │   ├── index.html
│   │   ├── README.md
│   │   └── REVIEW.md
│   ├── build-a-recipe-page/
│   │   ├── index.html
│   │   ├── README.md
│   │   └── REVIEW.md
│   ├── build-a-travel-agency-page/
│   │   ├── index.html
│   │   ├── README.md
│   │   └── REVIEW.md
│   ├── build-an-html-audio-and-video-player/
│       ├── index.html
│       ├── README.md
│       └── REVIEW.md
│   └── build-a-video-compilation-page/
│       ├── index.html
│       ├── README.md
│       └── REVIEW.md
└── certification-projects/
    └── .gitkeep
```

The `.gitkeep` file is a placeholder, **not** a completed certification project.

## Documentation guide

Each practical activity contains exactly three learning artifacts:

- **`index.html`** — browser-openable HTML source, without a build step.
- **`README.md`** — purpose, source structure, learning record, external assets and verification limits.
- **`REVIEW.md`** — concepts, British English IPA, pitfalls and unanswered self-assessment questions.

The cumulative [RWD_REVIEW.md](./RWD_REVIEW.md) links concepts across lessons, distinguishing completed practice, background explanations and future topics.

### Quick activity links

| Activity | Source | Notes | Review |
| --- | --- | --- | --- |
| Curriculum Outline | [HTML](./workshops/build-a-curriculum-outline/index.html) | [README](./workshops/build-a-curriculum-outline/README.md) | [REVIEW](./workshops/build-a-curriculum-outline/REVIEW.md) |
| Camperbot Profile | [HTML](./labs/debug-camperbots-profile-page/index.html) | [README](./labs/debug-camperbots-profile-page/README.md) | [REVIEW](./labs/debug-camperbots-profile-page/REVIEW.md) |
| Pet Adoption | [HTML](./labs/debug-pet-adoption-page/index.html) | [README](./labs/debug-pet-adoption-page/README.md) | [REVIEW](./labs/debug-pet-adoption-page/REVIEW.md) |
| Cat Photo App | [HTML](./workshops/build-a-cat-photo-app/index.html) | [README](./workshops/build-a-cat-photo-app/README.md) | [REVIEW](./workshops/build-a-cat-photo-app/REVIEW.md) |
| Recipe Page | [HTML](./labs/build-a-recipe-page/index.html) | [README](./labs/build-a-recipe-page/README.md) | [REVIEW](./labs/build-a-recipe-page/REVIEW.md) |
| Bookstore Page | [HTML](./workshops/build-a-bookstore-page/index.html) | [README](./workshops/build-a-bookstore-page/README.md) | [REVIEW](./workshops/build-a-bookstore-page/REVIEW.md) |
| Travel Agency Page | [HTML](./labs/build-a-travel-agency-page/index.html) | [README](./labs/build-a-travel-agency-page/README.md) | [REVIEW](./labs/build-a-travel-agency-page/REVIEW.md) |
| HTML Music Player | [HTML](./workshops/build-an-html-music-player/index.html) | [README](./workshops/build-an-html-music-player/README.md) | [REVIEW](./workshops/build-an-html-music-player/REVIEW.md) |
| HTML Video Player | [HTML](./workshops/build-an-html-video-player/index.html) | [README](./workshops/build-an-html-video-player/README.md) | [REVIEW](./workshops/build-an-html-video-player/REVIEW.md) |
| HTML Audio and Video Lab | [HTML](./labs/build-an-html-audio-and-video-player/index.html) | [README](./labs/build-an-html-audio-and-video-player/README.md) | [REVIEW](./labs/build-an-html-audio-and-video-player/REVIEW.md) |
| Heart Icon | [HTML](./workshops/build-a-heart-icon/index.html) | [README](./workshops/build-a-heart-icon/README.md) | [REVIEW](./workshops/build-a-heart-icon/REVIEW.md) |
| iframe Video Display | [HTML](./workshops/build-a-video-display-using-iframe/index.html) | [README](./workshops/build-a-video-display-using-iframe/README.md) | [REVIEW](./workshops/build-a-video-display-using-iframe/REVIEW.md) |
| Video Compilation Page | [HTML](./labs/build-a-video-compilation-page/index.html) | [README](./labs/build-a-video-compilation-page/README.md) | [REVIEW](./labs/build-a-video-compilation-page/REVIEW.md) |
| Major Web Browsers | [HTML](./workshops/build-a-list-of-major-web-browsers/index.html) | [README](./workshops/build-a-list-of-major-web-browsers/README.md) | [REVIEW](./workshops/build-a-list-of-major-web-browsers/REVIEW.md) |

## View and inspect the work

Open any activity's `index.html` in a browser. No Node.js installation, package manager or local development server is required. Some images, the Music Player audio files, and the Video Player poster/video sources are hosted on remote CDNs and therefore require internet access. The Music Player includes three native audio controls; the Video Player includes one native video player with four alternative sources.

To inspect the source:

1. Compare visible content with HTML headings, paragraphs, lists, figures, links and images.
2. Use **Developer Tools → Elements** to inspect the DOM and nested relationships.
3. Check `src`, `alt`, `href`, `target`, document language and character encoding where the lesson uses them.
4. Check **Developer Tools → Network** when an image fails to load; a syntactically valid `src` can still reference a missing resource.
5. Do not treat passing an exercise as a full accessibility, responsive-layout or cross-browser audit.

Workshop 02 uses a complete HTML5 document supplied by the lesson. Older Workshop 01 and Lab 01/02 archives include standalone document wrappers added for local viewing; those wrappers are **not** claims that the lessons separately taught boilerplate. Lab 03 directly practiced the document skeleton and revealed the difference between a **100% code-check result** and a **broken image in Preview**. Workshop 03 adds `div` containers, reusable classes, distinct IDs and native buttons; its static HTML does **not** implement cart or payment functionality. Lab 04 extends the earlier image/link lessons with **SEO description metadata**, exactly two package links, and three figures containing linked images and captions. The original Lab 04 passed the checker despite empty image sources; the archived edition uses the freeCodeCamp-provided images and more descriptive content. Workshop 04 uses three separate native `audio` players with `controls` and `loop`; it does not implement playlist coordination or autoplay. Its supplied HTML passed **9/9** steps without custom CSS or JavaScript. Workshop 05 adds one native `video` with `muted`, `poster`, `width`, and four `source` candidates with MIME hints; the original Step 13 submission passed **13/13**. The local document adds only the previously supplied opening HTML boilerplate missing from the pasted final fragment.

**Lab 05 connection:** two semantic media sections combine the earlier audio/video workshop patterns. A passing source checker validates the required HTML structure, but not successful download, playable duration, codec support, captions or mobile layout. See the [Lab 05 review](./labs/build-an-html-audio-and-video-player/REVIEW.md).

Workshop 06 uses an inline SVG heart with a single `path`. Its 24×24 drawing coordinates, displayed dimensions and inherited red `fill` are distinct concepts. The source has no JavaScript, CSS or external icon image.

Workshop 07 introduces an embedded YouTube page via `iframe`, with fixed dimensions, a third-party `src`, an `allow` permissions-policy string, a cross-origin `referrerpolicy` and `allowfullscreen`. Its exercise completion does not independently validate playback restrictions, responsive layout or accessibility. See the [Workshop 07 review](./workshops/build-a-video-display-using-iframe/REVIEW.md).

**Lab 06 connection:** This exercise combines three embedded videos in a single `main` landmark, with one `h2`, one `p` and one `iframe` in each `section`. Valid embed URLs and iframe titles are independently meaningful, but the curriculum completion marker does not reveal the original submitted code. See the [Lab 06 review](./labs/build-a-video-compilation-page/REVIEW.md).

**Workshop 08 evidence:** The learner supplied the full HTML and a Step 7 screenshot showing **7/7 (100%)**. The archive preserves five `dt` / five `dd` pairs; it has not been independently cross-browser audited.

## Subject roadmap

| Subject | Coverage | Status |
| --- | --- | --- |
| HTML elements and headings | Tags, `h1`–`h3`, `p`, nesting | Practiced |
| HTML debugging | Incorrect element names, closing syntax, DOM repair | Practiced |
| Links and images | `img`, `a`, `src`, `alt`, `href`, `target` | Practiced |
| Document structure | `html`, `head`, `body`, `title`, `meta charset`, `lang` | Practiced |
| Semantic grouping | `main`, `section`, `footer`, `figure`, `figcaption` | Practiced in Workshop 02 |
| Lists and sequence | `ul`, `ol`, `li`, rank vs procedure | Practiced in Workshop 02 and Lab 03 |
| Practical validation | User stories, DOM/Preview, external image resource loading | Practiced in Lab 03; deeper audits remain future work |
| Generic containers and identifiers | `div`, shared `class`, unique `id`, parent–child nesting | Practiced in Workshop 03 |
| Native buttons | `button`, shared classes and individual IDs | HTML structure practiced in Workshop 03; dynamic cart/checkout behavior not implemented |
| Travel descriptions and linked figures | `meta name="description"`, `ul > li > a`, `figure > a > img`, `figcaption` | Practiced in Lab 04; real-world image loading checked separately from source acceptance |
| HTML audio playback | `audio`, `src`, `controls`, `loop`; supplied `meta viewport` | Practiced in Workshop 04; native controls and online media availability are browser-dependent |
| HTML video playback | `video`, `source`, `type`, `poster`, `muted`, `width`, `controls`, `loop` | Practiced in Workshop 05; alternative formats and real browser decoding are separate concerns |
| Combined audio/video playback | Two `section` elements; `video > source` and `audio[src]`; remote media URL debugging | Practiced in Lab 05; original submission passed 18/18 while audio remained unverified |
| Inline SVG icons | `svg`, `path`, `d`, `width`, `height`, `viewBox`, `fill` | Practised in Workshop 06; detailed accessibility remains future work |
| Video embedding with iframe | Third-party embedded documents, embed URL, permissions policy, referrer policy, fullscreen | Practiced in Workshop 07; responsiveness and accessible naming are extensions |
| Compiling embedded videos | `main` as sole `body` child; three `section > h2 + p + iframe` blocks; embed `src`, `title`, `width` and `height` | Practiced in Lab 06; archived reconstruction not officially retested |
| Description lists | `dl` groups associated `dt` term / `dd` description pairs | Practiced in Workshop 08, **7/7** steps |
| Further HTML | Forms, labels, tables, expanded accessibility | Planned |
| CSS fundamentals | Selectors, cascade, colors, typography, box model | Planned |
| CSS layout and responsive design | Flexbox, Grid, positioning, media queries | Planned |
| Advanced CSS and projects | Interaction states, effects and certification projects | Planned |

## Repository conventions

- Keep original learner completion evidence distinct from subsequent edits to an archived local edition.
- Use consistent directory names based on the official freeCodeCamp activity.
- **Do not record completion dates in learning documentation.**
- Keep the repository focused on HTML/CSS source and learning notes: **no Python test files or update scripts**.
- Update each activity's README/REVIEW and both cumulative root documents when completing a practical lesson.
- Review intended changes before committing. Never overwrite unrelated local work.

## Official resource

[freeCodeCamp Responsive Web Design Certification V9](https://www.freecodecamp.org/learn/responsive-web-design-v9/)
