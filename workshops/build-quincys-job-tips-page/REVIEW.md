# Workshop 09 — Conceptual Review / Ôn tập chuyên sâu

**Activity:** Build Quincy's Job Tips Page — freeCodeCamp Responsive Web Design V9.
**Learner evidence:** complete HTML provided; the learner reported completion, but no final checker screenshot or step count was supplied in this message.
**Source authority:** [`index.html`](./index.html) is the submitted HTML. The wording of quotes is preserved; exact matching with the published article has **not** been verified.

## 1. Semantic HTML — HTML có ngữ nghĩa

**Semantic** /sɪˈmæn.tɪk/ (sờ-MAN-tik) means *concerned with meaning* — thuộc về ngữ nghĩa. Semantic HTML indicates what a part of a document **is**, not only what it looks like.

Here, an `h1` identifies the page topic; three `h2` headings identify distinct advice themes. `main` represents the principal content region; `section` identifies thematic content groups; `q` and `blockquote` identify quotations. Without custom CSS, browsers still apply default visual formatting, but semantic meaning and default appearance are separate concerns.

**Observation on this exact source:** the page's `h1` and introductory paragraph are outside the `main` element. That is what the learner submitted. Placing core introductory content inside `main` would often be a useful future design revision, but the archive does not silently change the accepted exercise code.

## 2. Short quotations: `<q>` versus `<blockquote>`

```html
<p>
  Learning to code is hard, but as Quincy Larson says,
  <q cite="https://www.freecodecamp.org/news/learn-to-code-book/">You can become a developer.</q>
</p>
```

`q` is for a short quotation **within** a sentence or paragraph. User agents commonly add quotation punctuation around its text; do not type a second pair of quote marks without checking the intended result. The quoted content remains part of the surrounding paragraph.

A `blockquote` is appropriate for a longer passage treated as a quotation block:

```html
<blockquote cite="https://www.freecodecamp.org/news/learn-to-code-book/">
  <p>Share short video demos of your projects.</p>
  <p>Keep applying to speak at bigger and bigger conferences.</p>
</blockquote>
```

The workshop uses three `blockquote` elements. The first directly contains prose; the second contains four paragraphs; the third contains three. Block quotations can contain flow content including paragraphs. Their display indentation normally comes from the browser's built-in CSS, not a requirement to insert spaces in the HTML.

## 3. The two meanings of `cite`

The **`cite` attribute** and the **`cite` element** have distinct uses:

```html
<blockquote cite="https://www.freecodecamp.org/news/learn-to-code-book/">
  A quotation from the referenced work.
</blockquote>
<p>—Quincy Larson, <cite>How to Learn to Code and Get a Developer Job [Full Book]</cite></p>
```

- The attribute `cite="..."` associates a quotation with a source URL. It is metadata; most browsers do **not** automatically render that URL visibly or make it clickable.
- The `<cite>` element marks the *title of a creative work*, such as a book or article. It is not intended simply as a wrapper for a person's name.
- The source uses `&mdash;` before the author's name. The entity renders the em dash (—) and has no automatic citation behavior.
- An explicit hyperlink would use `<a href="...">` where appropriate; a `cite` attribute alone is not equivalent to an `a` element.

**Provenance:** A URL in `cite` is only an author-supplied source pointer. It does not independently prove that the quotation is verbatim, the source is available, or permission to reuse material has been checked.

## 4. Section hierarchy and DOM relationships

```text
body
├── h1
├── p > q[cite]
└── main
    ├── section > h2 + blockquote + p[citation text and cite element]
    ├── section > h2 + blockquote > p + p + p + p
    └── section > h2 + blockquote > p + p + p
```

The three `section` elements are direct children of `main` and each starts with an `h2` heading. The first adds a separate author-and-title attribution paragraph after its quote. The other two contain multiple paragraphs *inside* their block quotations. An `h2` is a heading child of `section`; it is **not** nested in the blockquote.

### Why `section` rather than `div`?

`div` is a generic grouping container. `section` carries thematic document semantics and is usually best introduced by a heading. This source has three named themes: success, networking, and reputation. Choosing `section` makes the structure more meaningful than using visually identical but unnamed generic containers.

## 5. Metadata, character encoding and browser behavior

The document starts with `<!DOCTYPE html>`, declares English via `lang="en"`, includes the UTF-8 charset and viewport metadata, and sets a title used for document metadata. Those are separate from the visible `h1`.

The browser converts the text and tags into a DOM. `q` may acquire quotation punctuation through browser styling; `blockquote` may be indented; `cite` is typically italicized by user-agent styling. None of these default visual changes establishes that the external source URL was retrieved or verified.

No JavaScript or external CSS is present. The `cite` attributes do not trigger audio/video downloads or a special API call.

## 6. Debugging / Những lỗi cần tránh

| Problem | Cause | How to check or correct |
| --- | --- | --- |
| An inline quotation breaks a paragraph's flow | `blockquote` used where a short `q` fits | Choose quote markup according to the content |
| Quote marks appear twice | Literal quote punctuation plus browser-provided `q` punctuation | Inspect rendered text and source |
| Source URL is invisible | `cite` attribute is metadata, not a hyperlink | Add an explicit `a` element in a separately documented revision if needed |
| Book author appears italicized as a title | `<cite>` wraps a person rather than a work title | Use `<cite>` for the title of the work |
| Section headings do not form a hierarchy | `h2` missing or placed inside a quote | Inspect `section` children in the DOM |
| Long quote appears unindented after CSS changes | Styles changed; markup may still be semantic | Verify DOM semantics separately from CSS |
| Code passes but a quotation is inaccurate | HTML validation does not check source wording | Independently compare against the published source before asserting accuracy |
| A quoted paragraph loses its intended grouping | Incorrect closing `</blockquote>` or `</p>` | Inspect start/end tags and computed DOM |

## 7. English vocabulary, pronunciation and Vietnamese meaning

British English IPA is approximate where accent variation occurs. CAPITAL letters in the Vietnamese-style reading hint indicate the stressed syllable; read IPA as the authority.

| Term | IPA (UK) | Cách đọc gợi ý | Nghĩa |
| --- | --- | --- | --- |
| Developer | /dɪˈvel.ə.pə/ | đi-VÉ-lờ-pờ | Nhà phát triển phần mềm |
| Semantic | /sɪˈmæn.tɪk/ | si-MAN-tik | Có ngữ nghĩa |
| Quotation | /kwəʊˈteɪ.ʃən/ | quâu-TÂY-shần | Trích dẫn |
| Inline quotation | /ˈɪn.laɪn kwəʊˈteɪ.ʃən/ | IN-lain quâu-TÂY-shần | Trích dẫn trong dòng |
| Block quotation | /blɒk kwəʊˈteɪ.ʃən/ | blok quâu-TÂY-shần | Trích dẫn dạng khối |
| Citation | /saɪˈteɪ.ʃən/ | sai-TÂY-shần | Thông tin trích dẫn |
| Source | /sɔːs/ | so(r)s | Nguồn |
| Attribute | /ˈæt.rɪ.bjuːt/ | ÁT-ri-biu(t) | Thuộc tính |
| Element | /ˈel.ɪ.mənt/ | ÉL-i-mờnt | Phần tử |
| Networking | /ˈnet.wɜː.kɪŋ/ | NÉT-wơ-king | Xây dựng quan hệ nghề nghiệp |
| Reputation | /ˌrep.jʊˈteɪ.ʃən/ | rep-yu-TÂY-shần | Danh tiếng, uy tín |
| Envision | /ɪnˈvɪʒ.ən/ | in-VI-zhần | Hình dung, tưởng tượng |
| Success | /səkˈses/ | sờk-SES | Thành công |
| Introvert | /ˈɪn.trə.vɜːt/ | ÍN-trờ-vơ(t) | Người hướng nội |
| Paragraph | /ˈpær.ə.ɡrɑːf/ | PÁ-rờ-graf | Đoạn văn |
| Structure | /ˈstrʌk.tʃə/ | STRẮK-chờ | Cấu trúc |
| Accessibility | /əkˌses.əˈbɪl.ə.ti/ | ặc-SE-si-BI-lờ-ti | Khả năng tiếp cận |

## 8. Self-assessment / Câu hỏi tự ôn tập (chưa kèm đáp án)

1. **Remember:** What does semantic HTML describe beyond visual appearance?
2. **Understand:** When is `q` more appropriate than `blockquote`?
3. **Analyze:** Why might the browser add visible quotation marks around `q` automatically?
4. **Apply:** Write one `q` with a valid URL in its `cite` attribute.
5. **Understand:** Does a `cite` attribute automatically create a link in the rendered page?
6. **Compare:** How is `cite="..."` different from the `<cite>` element?
7. **Apply:** Mark up a book title correctly in an attribution sentence.
8. **Debug:** Why might a long quote show four paragraphs in a single `blockquote`?
9. **Understand:** What is the relationship between an `h2` and its enclosing `section`?
10. **Analyze:** How do default indentation and actual HTML nesting differ?
11. **Evaluate:** Why does source markup alone not prove a quoted passage is word-for-word accurate?
12. **Apply:** Identify the purpose of `&mdash;` in an attribution.
13. **Compare:** When should you use `section` rather than a generic `div`?
14. **Analyze:** In this final source, where are the `h1` and introduction placed relative to `main`?
15. **Create — extension:** Design a version where `main` includes the heading, introduction and three sections; explain why this is a revision, not the submitted source.
16. **Debug:** What DOM structure would you inspect if a closing `</blockquote>` tag were missing?
17. **Evaluate:** Which keyboard and screen-reader checks would be necessary before claiming the page is accessible?
18. **Create:** Write a short, source-attributed engineering quotation and a separate citation of the work title, without inventing a real source.
19. **Compare:** What is the difference between the browser-tab `title` and the visible `h1`?
20. **Evaluate:** What does the learner's supplied HTML demonstrate, and which claims remain unverified without the official checker or browser testing?

## 9. Connections to earlier lessons

Workshop 01 introduced headings and paragraphs. Workshop 02 and the media labs developed document structure, semantic grouping and source attributes. Workshop 08 used `dl` to associate named items with descriptions; Workshop 09 now distinguishes **inline quotes**, **extended quotations**, **work titles** and **source URLs**, building richer document semantics without adding scripts or visual components.

**Next step:** revisit quotations and citations in a technical report, where a source link, verbatim accuracy, licensing and context must be checked separately from HTML validity.
