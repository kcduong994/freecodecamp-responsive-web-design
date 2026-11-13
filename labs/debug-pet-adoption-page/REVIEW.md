# Lab 02 — Debugging HTML Image and Link Attributes / Ôn tập kiến thức

**Exercise:** Debug a Pet Adoption Page  
**Date:** 2026-11-13  
**Completed in freeCodeCamp:** 100%, **5/5 checks passed** (learner screenshot).  
**Scope:** `img`, `a`, `src`, `href`, `alt`, void elements and HTML source debugging.

## 1. Core distinction: element vs attribute

An **HTML element** represents a type of content or behavior. An **attribute** supplies a particular property in its opening tag. Attributes are not interchangeable merely because they both contain URL strings.

```html
<img src="cats.jpg" alt="Two kittens sleeping">
<a href="/cats">Visit cats page</a>
```

- `img` embeds an image. `src` names the image resource; `alt` supplies text as an alternative to that image.
- `a` creates a hyperlink when supplied an `href`, which identifies the navigation destination.
- The lab initially used `href` on `img` and `src` on `a` — both are incorrect for their intended tasks.

## 2. What does the browser actually do?

1. The browser parses the markup into a **DOM** (Document Object Model) tree.
2. For `img`, it uses a recognized **`src`** URL to request and display the image. A mistaken `href` does not substitute for that mechanism.
3. The browser associates image **`alt`** text with the image as a text alternative. The invented `att` attribute does not supply this recognized semantic function.
4. For `a`, a valid **`href`** makes the anchor a hyperlink. `src` on `a` does not make it navigate to that URL.
5. An HTML **void element** such as `img` has no content children and cannot have a corresponding `</img>` closing tag.

**Important extension:** browsers are fault-tolerant, but their ability to render content does not guarantee valid or accessible HTML. The HTML parser may ignore or recover from some errors; verify the resulting DOM and the behavior, not just the existence of text in Preview.

## 3. The image's alternative text

The lab's completed markup uses:

```html
<img
  src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg"
  alt="Two tabby kittens sleeping together on a couch."
>
```

`alt` should communicate the relevant information the image contributes, based on its purpose and context. It is not merely a tooltip and is not only for broken images. A screen reader can announce the alternative text when appropriate; if the image fails to load, a browser may display it as fallback text.

**Extension (not assessed in this lab):** a purely decorative image may use `alt=""`; meaningful images generally need an appropriate text alternative. Do not simply replace every image's `alt` with the filename.

## 4. Relative URL semantics (extension)

- `https://cdn.freecodecamp.org/.../cats.jpg` is an absolute HTTPS URL to a resource on a different host.
- `/cats` and `/dogs` are **root-relative** paths, resolved against the current site's origin (or the current file URL context).
- `href="/cats"` can be syntactically correct **even if no `/cats` route exists** on a given local test server. Markup validity and resource/route availability are separate properties.

## 5. Debugging checklist

| Symptom | Typical mistake | What to check |
| --- | --- | --- |
| Image does not appear | `href` used instead of `src` | Inspect `img` source attribute and network response |
| Image alternative is missing | `att` instead of `alt` | Inspect `alt` on the `img` DOM element |
| Unexpected closing markup | `</img>` | Remove the invalid closing tag for the void element |
| Anchor text is not a link | `src` instead of `href` | Inspect `a` and its destination |
| Clicking link fails locally | Target route does not exist | Separate correct HTML from server routing |
| Tests pass but page still needs review | Tests cover limited cases | Check accessibility and network behavior separately |

## 6. Technical English — UK IPA and Vietnamese

| English term | UK IPA | Tiếng Việt |
| --- | --- | --- |
| Attribute | /ˈæt.rɪ.bjuːt/ | Thuộc tính |
| Source | /sɔːs/ | Nguồn tài nguyên |
| Reference | /ˈref.ər.əns/ | Tham chiếu |
| Alternative | /ɒlˈtɜː.nə.tɪv/ | Thay thế |
| Image | /ˈɪm.ɪdʒ/ | Hình ảnh |
| Anchor | /ˈæŋ.kə/ | Phần tử neo/liên kết |
| Hyperlink | /ˈhaɪ.pə.lɪŋk/ | Siêu liên kết |
| Void element | /vɔɪd ˈel.ɪ.mənt/ | Phần tử rỗng |
| Adoption | /əˈdɒp.ʃən/ | Việc nhận nuôi |
| Accessibility | /əkˌses.əˈbɪl.ə.ti/ | Khả năng tiếp cận |
| Relative URL | /ˈrel.ə.tɪv ˌjuː ɑːr ˈel/ | Địa chỉ URL tương đối |
| Debugging | /ˌdiːˈbʌɡ.ɪŋ/ | Gỡ lỗi |

In code, the exact names `src`, `alt` and `href` are technical identifiers, not arbitrary abbreviations you can rename. `src` commonly abbreviates *source*; `alt` abbreviates *alternative*; `href` is historically called a *hypertext reference*.

## 7. Six levels of self-assessment — no answer key

Complete the questions yourself before requesting grading. Extensions are marked explicitly.

**Remember / Ghi nhớ**
1. Name the attributes that specify an embedded image's URL, its text alternative and a hyperlink's destination.
2. Which element is void: `img` or `a`? Write the proper form of each element.

**Understand / Thông hiểu**
3. Why does `<img href="cats.jpg">` not embed that image as intended?
4. Why is `alt="Two tabby kittens sleeping together on a couch."` more useful than `att="..."`?

**Apply / Vận dụng**
5. In a temporary file, fix `<img href="dog.jpg" att="A brown dog"></img>` with minimal edits.
6. Make `<a src="/adopt">Adopt now</a>` into a navigable hyperlink.

**Analyze / Phân tích**
7. A page renders the words “Visit cats page” but they cannot be clicked. List two concrete checks you would make in DevTools.
8. Explain the difference between a link that is missing its `href` and a valid link whose target path returns HTTP 404. *(Extension)*

**Evaluate / Đánh giá — extension**
9. Does a 5/5 freeCodeCamp result establish that a website is fully accessible? Explain which evidence is still missing.

**Create / Sáng tạo — extension**
10. Sketch an HTML-only page presenting two coastal-engineering observation stations. Include meaningful headings, one informative image with suitable `alt`, and two navigation links; explain your choices.

## 8. Self-assessment checklist

- [ ] I can distinguish `src`, `href` and `alt`.
- [ ] I can explain why `img` is a void element.
- [ ] I know that `</img>` is incorrect in HTML.
- [ ] I can explain why `href="/cats"` does not guarantee an actual local route.
- [ ] I can distinguish freeCodeCamp's five checks from a broader accessibility or network audit.

**This checklist is for self-study and is not itself a verified assessment.**
