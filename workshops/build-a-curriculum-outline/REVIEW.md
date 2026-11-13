# Workshop 01 — Conceptual Review / Ôn tập kiến thức

**Activity:** Build a Curriculum Outline  
**Scope:** HTML text, elements, heading levels, paragraphs, and the introductory distinctions between HTML/CSS/JavaScript.

## 1. Core concepts

### 1.1 HTML provides content and semantics

HTML (*HyperText Markup Language*) uses markup to describe webpage content and its logical structure. It is not primarily a layout engine or a replacement for application programming logic.

**VI:** HTML định nghĩa *nội dung là gì* và *cấu trúc ý nghĩa của nội dung*. CSS chủ yếu định dạng cách trình bày; JavaScript có thể thực hiện logic và tương tác.

### 1.2 Tags, content and elements

```html
<h1>Welcome to freeCodeCamp</h1>
```

- `<h1>` — opening tag (thẻ mở).
- `Welcome to freeCodeCamp` — content (nội dung).
- `</h1>` — closing tag (thẻ đóng).
- The full structure — HTML element (phần tử HTML).

Do not assume all HTML elements need a closing tag. Void elements such as `img` will be introduced in later practice; **the heading and paragraph elements here do require closing tags**.

### 1.3 Headings represent hierarchy

| Markup | Role |
| --- | --- |
| `h1` | Main welcome heading |
| `h2` | Curriculum heading |
| `h3` | Three parallel topic headings |
| `p` | Explanation or introductory paragraph |

The workshop uses one `h1` and one `h2`, followed by three sibling `h3` headings. A lower-number heading is not just a way to make letters bigger. Headings communicate structure to readers and assistive technology.

**Nuance:** one meaningful `h1` is a useful beginner convention, but having multiple `h1` elements does not, by itself, automatically make every HTML document invalid.

### 1.4 Why does the preview change?

The browser converts HTML into a DOM (*Document Object Model*) tree and applies default presentation rules. Adding `<h1>` often produces bigger, bolder text because of the browser's **user-agent stylesheet**. This appearance is a default style, not the meaning of the tag.

```text
Plain text: browser can still display it
      ↓ add meaningful HTML markup
Heading / paragraph elements in DOM
      ↓ browser default presentation
Visually distinct headings and paragraphs
```

### 1.5 Recognize the limited scope

The exercise *mentions* CSS and JavaScript but does not require custom CSS rules or JavaScript code. The added HTML5 document wrapper in the archived `index.html` is a convenience for opening the file locally, not a separate completed theory lesson.

## 2. Common mistakes

1. Forgetting `</h1>`, `</h2>`, `</h3>` or `</p>`.
2. Choosing heading tags solely for their default font sizes.
3. Leaving a real paragraph as raw text without marking its role.
4. Confusing a tag with the element as a whole.
5. Claiming a concept has been mastered merely because its name appears in the page.
6. Assuming the browser preview establishes all aspects of correctness.

## 3. Technical vocabulary — British English IPA

| Term | IPA | Vietnamese |
| --- | --- | --- |
| Hypertext | /ˈhaɪ.pə.tekst/ | Siêu văn bản |
| Markup | /ˈmɑː.kʌp/ | Đánh dấu |
| Element | /ˈel.ɪ.mənt/ | Phần tử |
| Opening tag | /ˈəʊ.pən.ɪŋ tæɡ/ | Thẻ mở |
| Closing tag | /ˈkləʊ.zɪŋ tæɡ/ | Thẻ đóng |
| Heading | /ˈhed.ɪŋ/ | Tiêu đề |
| Subheading | /ˈsʌbˌhed.ɪŋ/ | Tiêu đề phụ |
| Paragraph | /ˈpær.ə.ɡrɑːf/ | Đoạn văn |
| Structure | /ˈstrʌk.tʃə/ | Cấu trúc |
| Hierarchy | /ˈhaɪə.rɑː.ki/ | Hệ phân cấp |
| Curriculum | /kəˈrɪk.jə.ləm/ | Chương trình học |
| Outline | /ˈaʊt.laɪn/ | Dàn ý |
| Preview | /ˈpriː.vjuː/ | Xem trước |
| Semantic | /sɪˈmæn.tɪk/ | Mang ngữ nghĩa |

## 4. Self-assessment questions — no answer key

Answer independently; questions labeled **extension** go beyond the workshop itself.

**Remember**
1. Expand the acronym HTML and explain its primary responsibility.
2. Identify the opening tag, content and closing tag in `<p>Hello</p>`.

**Understand**
3. Why does wrapping text in `h1` change its normal appearance without custom CSS?
4. Why is `h3` more meaningful than a plain `p` for “Introduction to CSS” in this document?

**Apply**
5. In a temporary copy, add a new `Introduction to Git` topic with a heading and a paragraph.
6. Write a paragraph describing why semantic structure matters.

**Analyze**
7. What is wrong with `<h3>Introduction to HTML</h2>`? Explain the underlying problem.
8. Sketch the document outline, counting the headings at each level.

**Evaluate — extension**
9. Someone uses `h1` for every section because it looks large. Is this a sound decision? Defend your answer.

**Create — extension**
10. Sketch an HTML-only outline for a coastal-engineering course with a main title, subsections and explanatory paragraphs. Explain your heading choices.

## 5. Personal mastery checklist

- [ ] I distinguish **tag** and **element**.
- [ ] I can explain the roles of `h1`, `h2`, `h3` and `p`.
- [ ] I understand that plain text can render without explicit semantic markup.
- [ ] I can describe HTML, CSS and JavaScript responsibilities.
- [ ] I can reason about default browser styling versus HTML semantics.

For the exact source, see [index.html](./index.html). For the course-wide synthesis, see [RWD_REVIEW.md](../../RWD_REVIEW.md).
