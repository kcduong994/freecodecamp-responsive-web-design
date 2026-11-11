# Lab 01 — HTML Debugging / Ôn tập gỡ lỗi HTML

**Lab:** Debug Camperbot's Profile Page  
**Status:** Passed on freeCodeCamp — 100% (2026-11-11 screenshot).  
**Scope:** Correcting invalid element names and a malformed `h3` closing tag.  
**Approach:** First diagnose the error, then explain why the corrected HTML works. Answers to the self-assessment questions are intentionally omitted.

## 1. Key concepts / Kiến thức trọng tâm

### 1.1 Syntax is not the same as appearance

**HTML syntax** (cú pháp HTML) specifies how HTML element tags and content are written. A browser may display text even when markup contains mistakes. Rendering some content **does not prove** the intended semantic HTML elements were created.

The original source used `<heading2>` and `<pp>`. These are not the standard heading or paragraph elements (`h2` and `p`); the parser does not infer the intended semantics from similar-looking names.

### 1.2 Correct opening and closing tags

```html
<h3>Background and Interests</h3>
```

- `<h3>` — **opening tag** (thẻ mở)
- `Background and Interests` — **text content** (nội dung)
- `</h3>` — **closing tag** (thẻ đóng)

**Extension:** `<h3/>` is not a valid substitute for `</h3>` in ordinary HTML markup. For a non-void HTML element such as `h3`, the trailing slash does not serve as an HTML closing tag. The browser's HTML parser can recover from this kind of mistake but may construct an unexpected tree.

### 1.3 Heading hierarchy and paragraphs

The finished page has exactly one `h1`, one `h2`, one `h3` and two `p` elements. Heading levels communicate document structure; they should not be chosen only for font size. Paragraph elements mark ordinary prose.

### 1.4 Source → DOM → rendered preview

```text
HTML source (possibly incorrect)
        ↓
HTML parser + error recovery
        ↓
DOM tree (Document Object Model)
        ↓
Browser default styles and layout
        ↓
Preview (visible result)
```

**Learned:** fixing tags can change both hierarchy and appearance. **Extension:** the detailed HTML error-recovery algorithm and computed browser styles go beyond the particular lab's instructions. Use browser Developer Tools → Elements to see the actual DOM.

### 1.5 Practical debugging workflow

1. Read the user stories and identify the required element types, counts and exact text.
2. Inspect incorrect names, missing delimiters and mismatched opening/closing tags.
3. Apply the smallest changes that satisfy the intended semantics.
4. Compare the HTML source with the browser preview and DOM tree.
5. Run freeCodeCamp tests and separate local source tests; record what each confirms.

## 2. Original issues and corrections

| Mistake | Why it fails the intended requirement | Correction |
| --- | --- | --- |
| `<heading2>` | Not an `h2` heading | Use `<h2>` and `</h2>` |
| `<pp>` | Not a standard paragraph element | Use `<p>` and `</p>` |
| `<h3/>` | Does not properly close an existing `h3` in HTML | Use `</h3>` |

## 3. Technical English (UK pronunciation / IPA)

| Word or expression | IPA | Nghĩa tiếng Việt |
| --- | --- | --- |
| Debug | /ˌdiːˈbʌɡ/ | Gỡ lỗi |
| Debugging | /ˌdiːˈbʌɡ.ɪŋ/ | Quá trình gỡ lỗi |
| Syntax | /ˈsɪn.tæks/ | Cú pháp |
| Element | /ˈel.ɪ.mənt/ | Phần tử |
| Heading | /ˈhed.ɪŋ/ | Tiêu đề |
| Paragraph | /ˈpær.ə.ɡrɑːf/ | Đoạn văn |
| Closing tag | /ˈkləʊ.zɪŋ tæɡ/ | Thẻ đóng |
| Invalid | /ɪnˈvæl.ɪd/ | Không hợp lệ |
| Profile | /ˈprəʊ.faɪl/ | Hồ sơ |
| Validation | /ˌvæl.ɪˈdeɪ.ʃən/ | Kiểm tra tính hợp lệ |
| Semantic | /sɪˈmæn.tɪk/ | Mang ngữ nghĩa |
| Error recovery | /ˈer.ə rɪˌkʌv.ər.i/ | Phục hồi lỗi |

## 4. Review questions (không kèm đáp án)

These questions follow six Bloom-style levels. Questions marked **extension** go beyond the basic lab.

**Remember — Ghi nhớ**

1. Which tag defines a second-level heading? Which tag defines a paragraph?
2. How do you write the opening and closing tags for an `h3` heading?

**Understand — Thông hiểu**

3. Why can a browser still display the words inside an unknown `<pp>` element?
4. Why is `<h3/>` different from `</h3>` in an HTML document?

**Apply — Vận dụng**

5. Correct `<heading2>Contact</heading2>` while preserving the text.
6. Correct `<h3>Research Interests<h3/>` using the fewest changes.

**Analyze — Phân tích**

7. Identify the issues in `<pp>About</pp><h3>Skills<h3/>`. How would you inspect the resulting DOM?

**Evaluate — Đánh giá (extension)**

8. Is “the page looks fine” sufficient evidence for semantic correctness? Explain.
9. What do freeCodeCamp tests verify in this lab, and what does a separate local Python structural test *not* verify?

**Create — Sáng tạo (extension)**

10. Design a minimal HTML-only coastal engineering researcher profile: one main heading, an About section, an Interests subsection and two paragraphs. Explain your choice of heading levels and how you would check them.

## 5. Checklist

- [ ] I recognize valid HTML heading and paragraph elements.
- [ ] I can explain the difference between opening and closing tags.
- [ ] I know why a rendered preview might hide source mistakes.
- [ ] I can check the DOM with browser Developer Tools.
- [ ] I can distinguish official freeCodeCamp results from local structural tests.
- [ ] I can correct the markup without unnecessarily rewriting the requested content.

> This checklist records self-assessment prompts, **not** independent grading results.
