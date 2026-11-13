# Lab 01 — HTML Debugging / Ôn tập kiến thức

**Activity:** Debug Camperbot's Profile Page  
**Core themes:** standard elements, closing tags, browser error recovery and semantic hierarchy.

## 1. Understand the failure, not just the correction

### Incorrect element names

`<heading2>` and `<pp>` are not the standard HTML elements for second-level headings and paragraphs. Browsers can create unfamiliar elements without guessing what the author intended. Writing `heading2` does **not** create `h2` semantics; writing `pp` does **not** create a standard paragraph.

### Incorrect closing syntax

```html
<h3>Background and Interests</h3>
```

An opening tag looks like `<h3>`, while a closing tag looks like `</h3>`. The original `<h3/>` is not an equivalent closing tag in an HTML document. The parser may recover from this mistake, but its resulting DOM can differ from the intended document.

### Semantic heading hierarchy

The finished page follows `h1 → h2 → p → h3 → p`. The semantic meaning is more important than how large the heading appears by default. `h1` announces the main page title; `h2` and `h3` represent progressively narrower heading levels in the exercise.

## 2. Source, DOM and preview

```text
HTML markup (possibly incorrect)
        ↓
Browser HTML parser and error recovery
        ↓
Document Object Model (DOM)
        ↓
Browser default styles and layout
        ↓
Rendered page / preview
```

The fact that a browser can show the text is not evidence that the intended element names and relationships are correct. Use **Developer Tools → Elements** to inspect what the browser actually constructed.

**Extension:** error recovery is governed by HTML parsing rules. In production, avoid relying on those rules to hide malformed markup; write predictable, meaningful HTML instead.

## 3. A practical debugging process

1. Read user stories and list the element names and text that must remain.
2. Compare the markup against correct HTML syntax.
3. Identify unknown names, incorrect delimiter order and mismatched tags.
4. Fix only the smallest number of necessary characters.
5. Inspect the source, rendered page and DOM.
6. Use the official freeCodeCamp check for the exercise's acceptance criteria.

This process applies equally well to more complex interfaces, although later lessons may introduce additional inspection tools.

## 4. Typical errors

| Issue | Example | Better approach |
| --- | --- | --- |
| Mistyped heading | `<heading2>` | Use `<h2>` |
| Mistyped paragraph | `<pp>` | Use `<p>` |
| Wrong closing delimiter | `<h3/>` | Use `</h3>` |
| Visual-only assessment | “The page looks fine” | Inspect markup and DOM |
| Excessive rewriting | Changing unrelated text | Preserve user-story content |

## 5. Technical English — British English IPA

| Term | IPA | Vietnamese |
| --- | --- | --- |
| Debug | /ˌdiːˈbʌɡ/ | Gỡ lỗi |
| Debugging | /ˌdiːˈbʌɡ.ɪŋ/ | Quá trình gỡ lỗi |
| Syntax | /ˈsɪn.tæks/ | Cú pháp |
| Element | /ˈel.ɪ.mənt/ | Phần tử |
| Heading | /ˈhed.ɪŋ/ | Tiêu đề |
| Paragraph | /ˈpær.ə.ɡrɑːf/ | Đoạn văn |
| Closing tag | /ˈkləʊ.zɪŋ tæɡ/ | Thẻ đóng |
| Profile | /ˈprəʊ.faɪl/ | Hồ sơ |
| Invalid | /ɪnˈvæl.ɪd/ | Không hợp lệ |
| Semantic | /sɪˈmæn.tɪk/ | Mang ngữ nghĩa |
| Error recovery | /ˈer.ə rɪˌkʌv.ər.i/ | Phục hồi lỗi |
| Validation | /ˌvæl.ɪˈdeɪ.ʃən/ | Kiểm tra tính hợp lệ |

## 6. Self-assessment — no answer key

**Remember**
1. Which tags create an `h2` heading and an ordinary paragraph?
2. Write the opening and closing tags for an `h3` heading.

**Understand**
3. Why can a browser still display the words inside `<pp>...</pp>`?
4. Why does `<h3/>` not properly close an existing `h3` element?

**Apply**
5. Correct `<heading2>Contact</heading2>` without changing the text.
6. Correct `<h3>Skills<h3/>` using the fewest edits.

**Analyze**
7. Find the errors in `<pp>About</pp><h3>Skills<h3/>` and describe how you would inspect the DOM.

**Evaluate — extension**
8. Is a good-looking preview enough to prove HTML semantics are correct? Explain.
9. What does freeCodeCamp's passing status demonstrate? What does it **not** demonstrate about accessibility?

**Create — extension**
10. Sketch an HTML-only researcher profile with a main heading, an About section, a subsection on research interests and two paragraphs. Justify the heading levels.

## 7. Personal checklist

- [ ] I recognize standard HTML headings and paragraphs.
- [ ] I use the correct slash placement in closing tags.
- [ ] I know why browser error recovery can hide source problems.
- [ ] I can compare the markup with the actual DOM.
- [ ] I can preserve the intended content while repairing its structure.

Source: [index.html](./index.html). Cross-lesson synthesis: [RWD_REVIEW.md](../../RWD_REVIEW.md).
