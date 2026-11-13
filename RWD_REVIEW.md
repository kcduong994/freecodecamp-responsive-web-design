# Responsive Web Design — Cumulative Conceptual Review

> **Status:** In progress — concepts from Workshop 01 and Labs 01–02 documented.  
> **Curriculum:** freeCodeCamp Responsive Web Design V9.  
> **Final review:** Not yet complete; later topics will be added after corresponding study and practice.

## Purpose and structure

This document is a **cross-lesson technical synthesis**, not a copy of freeCodeCamp's instructions. Each activity also has a dedicated `REVIEW.md` with detailed explanations, English vocabulary and independent practice questions.

For every new topic, ask six questions:

1. **What is it?** What purpose does the HTML construct serve?
2. **What does the browser receive?** Which markup, attributes and resource URLs were supplied?
3. **What does the browser do?** How does it create a DOM, load resources and interpret elements?
4. **What does the user experience?** How are semantics, appearance and interaction exposed?
5. **What can fail?** Which syntax, semantic, resource or navigation mistakes are possible?
6. **How do we inspect the result?** What do freeCodeCamp checks, source inspection and browser tools actually establish?

**Scope labels:** *Practiced* = used in a completed activity; *Explained* = conceptual interpretation of that practice; *Extension* = useful background beyond the exercise; *Planned* = not yet covered by completed work.

## Learning map

| Part | Subject | Status | Evidence |
| --- | --- | --- | --- |
| 01 | HTML elements, heading hierarchy and paragraphs | Practiced / explained | [Workshop 01](./workshops/build-a-curriculum-outline/) |
| 02 | Debugging malformed element names and closing syntax | Practiced / explained | [Lab 01](./labs/debug-camperbots-profile-page/) |
| 03 | Images, anchor links and HTML attributes | Practiced / explained | [Lab 02](./labs/debug-pet-adoption-page/) |
| 04 | HTML boilerplate and additional content semantics | Planned / partial packaging exposure | Standalone archived HTML wrappers are not proof of completed theory |
| 05 | CSS syntax, selectors, cascade and box model | Planned | Not yet documented as completed |
| 06 | Flexbox, Grid, positioning and responsive design | Planned | Not yet documented as completed |
| 07 | Forms, accessibility and full project verification | Planned | Not yet documented as completed |

---

## Part 01 — HTML structure and hierarchy

### What is HTML?

**HTML** means *HyperText Markup Language*. HTML describes the **structure and semantics** of web content. It is a markup language; it does not express application logic in the same way JavaScript does.

In the curriculum-outline workshop, we used one `h1`, one `h2`, three sibling `h3` headings, and four `p` paragraphs.

| Element | Meaning in that page | Caution |
| --- | --- | --- |
| `h1` | Main welcome heading | Do not choose a heading merely for large font size |
| `h2` | Curriculum heading | Level indicates a logical hierarchy |
| `h3` | HTML, CSS and JavaScript topic headings | Same-level headings are sibling topics |
| `p` | Ordinary explanatory prose | Plain text may display without `p`, but lacks explicit paragraph semantics |

**Tag vs element:** in `<h3>Introduction to CSS</h3>`, `<h3>` is the opening tag, `Introduction to CSS` is the text node, `</h3>` is the closing tag, and together they represent an HTML element.

### What happens in the browser?

```text
HTML input → parser → DOM (document tree)
                       ↓
            default browser styles
                       ↓
              layout and preview
```

The default browser stylesheet usually makes headings larger and heavier than paragraphs. These visual defaults do not define the semantic purpose of a heading.

**Extension:** browser CSS processing involves stylesheets, style calculation, layout, painting and compositing. Detailed CSS rendering is reserved for later topics.

### Local archive versus curriculum fragment

The freeCodeCamp exercise editor showed fragments such as headings and paragraphs. Our browser-openable archive adds `<!DOCTYPE html>`, `<html lang="en">`, `<head>`, a title and a `<body>`. These additions facilitate local inspection. They are **not** claims that the boilerplate theory was completed during Workshop 01.

The screenshot's nonstandard capitalization of `Javascript`/`javaScript` is preserved in the archived lesson output. In professional writing, the language is **JavaScript**.

---

## Part 02 — HTML debugging and error recovery

### The key lesson

A browser displaying text is **not** proof that the HTML uses the correct elements. Lab 01 corrected mistyped or malformed markup:

| Original mistake | Correct markup | Underlying reason |
| --- | --- | --- |
| `<heading2>About</heading2>` | `<h2>About</h2>` | Unknown element names do not become standard headings |
| `<pp>...</pp>` | `<p>...</p>` | Paragraphs use the `p` element |
| `<h3>...<h3/>` | `<h3>...</h3>` | A closing tag begins with `</` |

Browsers have **HTML parsing and error-recovery rules**. Unknown tags can still appear in the DOM; poorly formed markup may also cause unexpected nesting. Fixing the source can change both its semantic tree and its visible output.

**Extension:** a trailing slash in a non-void HTML opening tag is not a replacement for the corresponding closing tag. `h3` requires a proper `</h3>` ending.

### Practical debugging discipline

Read the user stories → inspect actual tags and attribute names → make small corrections → compare the DOM and preview → use the freeCodeCamp checks → document what was and was not verified.

Never conflate an exercise's passing status with full accessibility or browser compatibility.

---

## Part 03 — HTML attributes, images and links

### An element's purpose determines its attributes

An **attribute** adds information to an HTML element in its opening tag. Names that look similar cannot be substituted arbitrarily.

```html
<img src="cats.jpg" alt="Two tabby kittens sleeping together">
<a href="/cats">Visit cats page</a>
```

| Element / attribute | Purpose | Used in Lab 02 |
| --- | --- | --- |
| `img` | Embed an image | Cat photograph |
| `src` | URL of the resource to load | CDN image URL |
| `alt` | Text alternative for the image | Description of two kittens |
| `a` | Anchor / hyperlink element | Cat and dog navigation links |
| `href` | Destination of a hyperlink | `/cats`, `/dogs` |

The lab's initial code used `href` on `img`, `att` instead of `alt`, a forbidden `</img>` closing tag, and `src` on both anchor elements. All five issues were corrected in the completed page.

### Why `img` differs from `a`

`img` is a **void element**: it has no content children and does not accept a closing `</img>` tag in HTML. An anchor such as `<a href="/cats">Visit cats page</a>` contains link text and does have an explicit closing tag.

`alt` is not merely a tooltip. It provides a meaningful textual alternative when an image cannot be perceived or loaded. **Extension:** decorative images can sometimes appropriately use `alt=""`, depending on context and purpose.

### Local URLs and resource availability

The source of the kitten image is an absolute HTTPS URL. The values `/cats` and `/dogs` are root-relative paths. An `href` can be syntactically correct even if a local file or test server has no route at that path. A broken route is a **navigation/resource availability** issue, not necessarily an HTML attribute issue. The external image also requires network access.

### What should be inspected?

1. Check the `img` element's `src` and `alt` values in DevTools → Elements.
2. Observe whether the image resource loads in the browser's Network panel.
3. Inspect `a[href]` values and distinguish a navigable element from a working destination.
4. Ensure no `</img>` appears in the markup.
5. Separate freeCodeCamp's five user-story checks from wider accessibility and production concerns.

---

## Technical vocabulary — British English IPA

| Term | IPA | Vietnamese |
| --- | --- | --- |
| Markup | /ˈmɑː.kʌp/ | Đánh dấu |
| Element | /ˈel.ɪ.mənt/ | Phần tử |
| Attribute | /ˈæt.rɪ.bjuːt/ | Thuộc tính |
| Heading | /ˈhed.ɪŋ/ | Tiêu đề |
| Paragraph | /ˈpær.ə.ɡrɑːf/ | Đoạn văn |
| Hierarchy | /ˈhaɪə.rɑː.ki/ | Hệ phân cấp |
| Debugging | /ˌdiːˈbʌɡ.ɪŋ/ | Gỡ lỗi |
| Syntax | /ˈsɪn.tæks/ | Cú pháp |
| Semantic | /sɪˈmæn.tɪk/ | Mang ngữ nghĩa |
| Image | /ˈɪm.ɪdʒ/ | Hình ảnh |
| Anchor | /ˈæŋ.kə/ | Liên kết neo |
| Hyperlink | /ˈhaɪ.pə.lɪŋk/ | Siêu liên kết |
| Alternative | /ɒlˈtɜː.nə.tɪv/ | Thay thế |
| Void element | /vɔɪd ˈel.ɪ.mənt/ | Phần tử rỗng |
| Accessibility | /əkˌses.əˈbɪl.ə.ti/ | Khả năng tiếp cận |
| Browser | /ˈbraʊ.zə/ | Trình duyệt |

## Cross-lesson questions — answer independently

1. **Remember:** What is the distinction between an opening tag and an HTML element?
2. **Understand:** Why does `<h1>` normally appear larger than plain text even without author-written CSS?
3. **Apply:** Give a heading hierarchy for an engineering course with three subject areas.
4. **Analyze:** Why may `<heading2>About</heading2>` show text but not behave as an `h2`?
5. **Understand:** Why must `img` use `src` instead of `href` to identify its image resource?
6. **Apply:** Correct `<img href="photo.jpg" att="River mouth"></img>`.
7. **Analyze:** An anchor has `href="/stations"` but the destination returns 404. Is the markup necessarily incorrect?
8. **Evaluate:** What does a passing freeCodeCamp exercise establish, and what must still be inspected manually?
9. **Create:** Sketch an HTML-only coastal-observation page with headings, two paragraphs, one informative image and navigation links.

Answers are intentionally omitted. Detailed activity-specific questions remain in each activity's `REVIEW.md`.

---

## Future topics — not yet completed

- **HTML document structure and attributes:** doctype, language, metadata, additional global attributes and correct usage.
- **Further semantic HTML:** lists, tables, forms, labels, navigation and landmarks.
- **CSS basics:** rules, selectors, inheritance, cascade, colors, units, typography and box model.
- **CSS layout:** positioning, Flexbox, Grid, media queries, mobile-first design and overflow handling.
- **Interaction and visual behavior:** pseudo-classes, pseudo-elements, transitions, transforms and animations.
- **Advanced quality:** accessibility, keyboard use, browser differences and complete certification projects.

**Maintenance principle:** update the individual activity notes first, then add only the concepts actually supported by the new exercise to this review. Maintain a clear separation between completed practice, technical explanation and planned material. No completion-date fields or auxiliary Python scripts are necessary.
