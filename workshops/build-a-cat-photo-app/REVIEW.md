# Workshop 02 — Conceptual Review / Ôn tập kiến thức

**Exercise:** Build a Cat Photo App
**Status:** Completed — 42/42 freeCodeCamp steps
**Scope:** Basic HTML document structure; semantic page sections; links and images; lists; figures; captions; emphasis; footer; charset metadata.

The questions intentionally **do not include answers**. First solve them yourself; explanations can be discussed after you submit your reasoning. The *Extension* sections go beyond what the workshop explicitly required.

## 1. What does the browser receive?

The final file begins with a complete HTML document rather than an isolated fragment:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>CatPhotoApp</title>
  </head>
  <body>...</body>
</html>
```

- `<!DOCTYPE html>` declares the HTML document type and selects standards mode in modern browsers.
- `html` is the document's root element; `lang="en"` identifies the primary language as English.
- `head` contains metadata and the document title, not the visible article content.
- `title` names the document for places such as the browser tab.
- `meta charset="UTF-8"` declares the character encoding; `meta` has no closing tag in HTML.
- `body` contains page content and semantic containers. Elements are nested; in this document, `body` has `main` and `footer` children.

**Distinction:** `charset` concerns how encoded characters are interpreted. It does *not* set the language; `lang` does that. Nor is `charset` a CSS rule.

## 2. Content structure: main, section and headings

The finished HTML uses one `main` containing the primary content, two `section` elements, and a separate `footer`.

- `main` signals the primary content of this document.
- `section` groups related content; the two sections each have their own `h2` heading (`Cat Photos`, `Cat Lists`).
- `h1` names the overall page, and `h3` headings organize topics within `Cat Lists`.
- `footer` groups final information, including the link to freeCodeCamp.

**Key distinction:** headings carry a logical hierarchy; choose levels by the structure, not by desired font size. A `section` does not automatically make unrelated content meaningful: grouping and headings must reflect actual topics.

### Browser interpretation (explained)

```text
HTML bytes → HTML parser → DOM element tree
                                   ↓
                      default browser styles
                                   ↓
                         layout and preview
```

A browser's default styles are why `h1`, `h2` and `h3` appear at different sizes before any CSS is authored. Do not equate visual font size with semantic significance.

## 3. Links and embedded images

```html
<a href="https://freecatphotoapp.com">
  <img
    src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg"
    alt="A cute orange cat lying on its back."
  >
</a>
```

The `a` element creates the link, while its child `img` provides the visual content users can click. `href` identifies the link target; `src` identifies the image resource; `alt` gives an alternative text description. These attributes are **not interchangeable**.

The completed page also contains a link with `target="_blank"`. It requests a new browsing context. **Extension:** for public websites, consider new-tab usability, accessibility and possible privacy/security concerns; modern browsers generally give links with `_blank` an implicit `noopener` behavior, but requirements and support should be evaluated in the actual deployment environment.

**Accessibility:** `alt` describes the *purpose/information* of the image in its context, not necessarily every visible pixel. It is not simply a tooltip. If images fail to load or a user employs assistive technology, meaningful text alternatives become important.

## 4. Unordered lists versus ordered lists

```html
<ul>
  <li>catnip</li>
  <li>laser pointers</li>
  <li>lasagna</li>
</ul>

<ol>
  <li>flea treatment</li>
  <li>thunder</li>
  <li>other cats</li>
</ol>
```

- `ul`: unordered list; the order is not inherently part of the meaning.
- `ol`: ordered list; ordering/ranking/sequence matters in the given context.
- `li`: one list item; used as a child of `ul` or `ol` in this workshop.

The workshop demonstrates both forms. Do not treat `ul` and `ol` solely as different bullet/numbering designs: **they communicate different meanings**.

## 5. Figure, caption and semantic emphasis

```html
<figure>
  <img src="..." alt="A slice of lasagna on a plate.">
  <figcaption>Cats <em>love</em> lasagna.</figcaption>
</figure>
```

`figure` holds a self-contained illustration; `figcaption` provides an associated caption. In the other figure, the caption uses `strong` rather than `em`.

| Element | Semantic meaning | Typical browser default |
| --- | --- | --- |
| `em` | Stress emphasis | Italic |
| `strong` | Strong importance, seriousness or urgency | Bold |
| `figcaption` | Caption attached to a figure | Normal text (styling varies) |

**Important:** `em` is not merely “make italic”, and `strong` is not merely “make bold”. Their semantics should guide use. If you only need appearance, CSS is the more appropriate tool later.

## 6. Common mistakes / Những lỗi thường gặp

| Mistake | Consequence / why to avoid it |
| --- | --- |
| Place the visible content in `head` | Incorrect separation of metadata and body content |
| Omit closing tags for `section`, `figure`, `main` or `footer` | Browser may recover but produce unintended nesting |
| Write `</img>` or `</meta>` | These are void elements in HTML |
| Use `href` instead of `src` on `img` | Image source will not be identified as intended |
| Use `src` instead of `href` on `a` | Link destination is not correctly specified |
| Omit useful `alt` text | Weakens text alternatives for informative images |
| Use `ol` only because numbers look nicer | Can misrepresent the meaning of the list |
| Treat `em` and `strong` as decorative styling only | Loses semantic distinction |
| Assume 100% freeCodeCamp = full production readiness | Exercise checks have limited scope |

## 7. Technical English vocabulary — British IPA

| Term | IPA | Nghĩa tiếng Việt |
| --- | --- | --- |
| Document | /ˈdɒk.jə.mənt/ | Tài liệu |
| Document type | /ˈdɒk.jə.mənt taɪp/ | Loại tài liệu |
| Metadata | /ˈmet.əˌdeɪ.tə/ | Siêu dữ liệu |
| Character encoding | /ˈkær.ək.tə ɪnˈkəʊ.dɪŋ/ | Mã hóa ký tự |
| Charset | /ˈkær.set/ | Bộ ký tự / chỉ định cách mã hóa ký tự |
| Nested | /ˈnes.tɪd/ | Được lồng bên trong |
| Section | /ˈsek.ʃən/ | Phần / mục nội dung |
| Main content | /meɪn ˈkɒn.tent/ | Nội dung chính |
| Footer | /ˈfʊt.ə/ | Phần chân trang |
| Unordered list | /ʌnˈɔː.dəd lɪst/ | Danh sách không thứ tự |
| Ordered list | /ˈɔː.dəd lɪst/ | Danh sách có thứ tự |
| List item | /lɪst ˈaɪ.təm/ | Mục danh sách |
| Figure | /ˈfɪɡ.ə/ | Hình minh họa / đơn vị nội dung độc lập |
| Caption | /ˈkæp.ʃən/ | Chú thích |
| Emphasis | /ˈem.fə.sɪs/ | Sự nhấn mạnh |
| Strong importance | /strɒŋ ɪmˈpɔː.təns/ | Mức độ quan trọng mạnh |
| Anchor | /ˈæŋ.kə/ | Liên kết neo |
| Target | /ˈtɑː.ɡɪt/ | Đích / mục tiêu |
| Alternative text | /ɒlˈtɜː.nə.tɪv tekst/ | Văn bản thay thế |
| Semantic | /sɪˈmæn.tɪk/ | Mang ngữ nghĩa |

## 8. Self-assessment — six Bloom levels (no answers)

### Remember / Ghi nhớ
1. What are the different purposes of `head`, `body`, `main` and `footer`?
2. Which two HTML elements create unordered and ordered lists? What element represents each item?
3. Which attribute declares the document's character encoding, and which element contains it?

### Understand / Thông hiểu
4. Why can `figure` and `figcaption` be preferable to an unrelated `img` followed by a `p`?
5. Why does an image placed inside an `a` element become clickable?
6. Explain the semantic difference between `em` and `strong`; do not answer merely “italic vs bold”.

### Apply / Vận dụng
7. Write a list of three coastal-observation stations where the order is **not** important.
8. Create a ranked top-three list of the most urgent coastal hazards. Which list element fits that meaning?
9. Write markup for an informative map image that links to a larger map, including a meaningful text alternative.

### Analyze / Phân tích
10. Identify the mistakes in `<a src="/gallery"><img href="cat.jpg" att="Cat"></img></a>`.
11. Draw the DOM hierarchy between `main`, `section`, `figure`, `img`, and `figcaption` in the completed page.
12. An image is visible, but the `alt` text is empty. Is the code necessarily incorrect? What context would you need?

### Evaluate / Đánh giá — Extension
13. Should all lists be ordered lists because numbers look professional? Explain.
14. When is `target="_blank"` appropriate, and what user-experience or security issues would you consider?
15. Does a screenshot of a passing freeCodeCamp test prove accessibility or cross-browser quality? Explain the evidence gap.

### Create / Sáng tạo — Extension
16. Design an HTML-only mini-site for coastal fieldwork with two named sections, one unordered equipment list, and one ordered survey procedure.
17. Add a figure with a photo of a sediment sample, a caption using `em` or `strong` for an appropriate reason, and descriptive `alt` text.
18. Sketch the complete DOM hierarchy and identify which parts belong in `head`, `main`, and `footer`.

## 9. Personal checklist (self-assessment, not formally graded)

- [ ] I can explain the purpose of `head`, `body`, `main`, `section` and `footer`.
- [ ] I can choose `ul` or `ol` based on meaning rather than appearance.
- [ ] I can build a linked image with a useful `alt` attribute.
- [ ] I can explain `figure`, `figcaption`, `em` and `strong`.
- [ ] I know what `meta charset="UTF-8"` does, and what it does not do.
- [ ] I can distinguish the workshop's 100% result from broader website verification.

See [README.md](./README.md) for source navigation and the completed page; see [../../RWD_REVIEW.md](../../RWD_REVIEW.md) for the cumulative multi-lesson model.
