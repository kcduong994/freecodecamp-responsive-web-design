# Workshop 01 — Conceptual Review / Ôn tập kiến thức

**Workshop:** Build a Curriculum Outline  
**Scope:** freeCodeCamp Responsive Web Design V9 — 11 completed steps only  
**Review status:** Workshop-level notes complete; **the repository-wide `RWD_REVIEW.md` remains planned** until the full practical curriculum is finished.

## 1. Concepts from this workshop

### 1.1 HTML is not a programming language in the same sense as JavaScript

**HTML (HyperText Markup Language)** is a **markup language**. It describes the content and structure of a webpage. The browser parses HTML to create a **DOM (Document Object Model)** tree; the visual preview uses that document structure to render the page.

**VI:** HTML là ngôn ngữ đánh dấu, chủ yếu mô tả nội dung và cấu trúc, không tự cung cấp logic điều khiển chương trình như JavaScript.

### 1.2 Opening tag, closing tag, content, and element

Example: `<h1>Welcome to freeCodeCamp</h1>`.

- **Opening tag**: `<h1>` — starts an element.
- **Content**: `Welcome to freeCodeCamp` — text in the element.
- **Closing tag**: `</h1>` — closes the element.
- **Element**: the complete structural unit represented by this markup.

Not all elements require closing tags (for example, `meta` is a void element). That detail belongs to later HTML material; the elements practiced here (`h1`, `h2`, `h3`, `p`) do have explicit closing tags.

### 1.3 Heading hierarchy is semantic, not a font-size shortcut

| Element | Role in this completed page |
| --- | --- |
| `<h1>` | Page-level welcome heading |
| `<h2>` | Curriculum section heading |
| `<h3>` | HTML, CSS and JavaScript topic headings |
| `<p>` | Explanatory paragraph |

Heading levels communicate hierarchy to readers and assistive technology. In this lesson the `<h3>` headings logically sit beneath the `<h2>` curriculum heading. The browser's default styles happen to make headings larger and bolder, but the element's **meaning** is not defined by font size.

**Nuance:** “Only one `<h1>` per page” is a common beginner guideline and matches this project. HTML does **not** generally fail validation merely because a document contains more than one `<h1>`; the key objective is a clear, meaningful heading structure.

### 1.4 The roles of HTML, CSS, and JavaScript

- **HTML** — structured content and semantics.
- **CSS** — presentation: color, font, spacing, layout, and responsive behavior.
- **JavaScript** — program logic and interaction, such as reacting to button clicks or form events.

**VI:** HTML trả lời *cái gì và tổ chức thế nào*; CSS trả lời *trông như thế nào*; JavaScript xử lý *hành vi tương tác và logic*.

### 1.5 Why the preview changes after using `<h1>`

The browser applies a **user-agent stylesheet** (CSS mặc định của trình duyệt) to headings and paragraphs. That explains why the plain text shown in Step 1 becomes larger and bold after being wrapped with `<h1>` in Step 2, even though the workshop introduces no CSS rules.

### 1.6 What freeCodeCamp tested, and what our local check tests

The supplied screenshots show all 11 challenges marked complete and freeCodeCamp reporting that code passes. Our local Python tests independently inspect the packaged source's **syntax-oriented structure** and exact archived content. Neither form of evidence proves cross-browser compatibility, accessibility conformance, or production readiness.

## 2. Technical English glossary (IPA, UK approximate)

| Term | IPA | Vietnamese meaning |
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
| Content | /ˈkɒn.tent/ | Nội dung |
| Curriculum | /kəˈrɪk.jə.ləm/ | Chương trình học |
| Outline | /ˈaʊt.laɪn/ | Dàn ý |
| Interactive | /ˌɪn.tərˈæk.tɪv/ | Có tính tương tác |
| Preview | /ˈpriː.vjuː/ | Xem trước |

## 3. Typical beginner mistakes / Lỗi cần tránh

1. **Missing closing tags** — viết `<h3>Introduction to HTML` nhưng quên `</h3>`.
2. **Using heading tags only for visual size** — chọn `<h3>` vì thấy nhỏ hơn, thay vì xét cấu trúc nội dung.
3. **Using plain text instead of a paragraph** — trình duyệt có thể hiển thị, nhưng thiếu ngữ nghĩa của `<p>`.
4. **Claiming CSS was written in this exercise** — lesson *mentions* CSS but uses no explicit CSS rules.
5. **Treating freeCodeCamp pass as complete accessibility validation** — automated curriculum checks have a narrower purpose.
6. **Inconsistent capitalization:** the completed screenshot contains `Javascript` and `javaScript`; professional writing normally spells the language **JavaScript**. The archive keeps the lesson output unchanged for reproducibility.

## 4. Six levels of self-assessment (không kèm đáp án)

Write answers yourself before asking for feedback. These questions intentionally include extensions beyond the workshop; such questions are labeled **Mở rộng**.

**Level 1 — Remember (Ghi nhớ)**  
Q1. What do the letters HTML stand for? Write a complete Vietnamese definition.  
Q2. Identify the opening tag, content, and closing tag in `<p>Hello</p>`.

**Level 2 — Understand (Thông hiểu)**  
Q3. Why does `<h1>` usually look larger than unwrapped text, even without a custom CSS file?  
Q4. Why is an `<h3>` heading more appropriate than `<p>` for “Introduction to CSS” in this page?

**Level 3 — Apply (Vận dụng)**  
Q5. Add a new topic “Introduction to Git” using the same structure as the existing topics. Which two element types should you use? *(Do this in a temporary copy, not the archived source.)*

**Level 4 — Analyze (Phân tích)**  
Q6. Find the structural mistake: `<h3>Introduction to HTML</h2>`. Explain its likely effect.  
Q7. Draw the heading hierarchy of this workshop and state how many elements exist at each heading level.

**Level 5 — Evaluate (Đánh giá) — Mở rộng**  
Q8. A developer uses `<h1>` for every section because it looks large. Assess the semantic risks.  
Q9. Does passing a freeCodeCamp structural test prove keyboard accessibility? Why or why not?

**Level 6 — Create (Sáng tạo) — Mở rộng**  
Q10. Propose an HTML-only outline for a coastal-engineering course, preserving meaningful heading levels and paragraphs. Describe how to verify the hierarchy.

## 5. Ready for the next lesson?

- [ ] I can distinguish **tag** from **element**.
- [ ] I know when to use `h1`, `h2`, `h3` and `p`.
- [ ] I can explain why raw text still displays in a browser.
- [ ] I can distinguish HTML, CSS, and JavaScript responsibilities.
- [ ] I have opened `index.html` locally and run the source tests.
- [ ] I can explain what the automated tests prove and what they cannot prove.

> The checklist is a self-assessment aid, **not a claim that these items were individually verified by the instructor**.
