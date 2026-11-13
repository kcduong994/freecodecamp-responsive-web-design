# Lab 02 — HTML Image and Link Attributes / Ôn tập kiến thức

**Activity:** Debug a Pet Adoption Page  
**Core topics:** HTML attributes, `img`, `a`, `src`, `alt`, `href`, void elements and URLs.

## 1. Attribute syntax and meaning

An HTML **attribute** provides additional information in an element's opening tag. Attribute names have defined roles and cannot be exchanged arbitrarily.

```html
<img src="cats.jpg" alt="Two kittens sleeping">
<a href="/cats">Visit cats page</a>
```

- `img`: image element (phần tử hình ảnh).
- `src`: *source* — identifies the resource to embed.
- `alt`: *alternative text* — supplies a textual alternative to an image.
- `a`: *anchor* — can create a hyperlink.
- `href`: *hypertext reference* — identifies the hyperlink's destination.

The original lab mistakenly used `href` on `img`, `att` in place of `alt`, and `src` on the anchors. The corrected page uses the appropriate attributes.

## 2. Void elements versus normal paired elements

`img` is a **void element**. It cannot have content children and has no closing `</img>` tag in HTML.

By contrast, the anchor contains text and has a proper closing tag:

```html
<a href="/dogs">Visit dogs page</a>
```

**Extension:** writing a trailing slash on a void element such as `<img ... />` is often tolerated in HTML syntax, but it is not an actual closing tag. The workshop's required solution simply uses `<img ...>`.

## 3. Browser behavior and accessibility

### Image loading

The browser examines `img[src]`, resolves the URL and requests the resource. An `href` attribute on `img` does not replace the recognized image-source mechanism.

### Text alternative

`alt` communicates the image's relevant meaning. It is not just an optional caption or a tooltip. When an image is informative, the alternative should express the information needed in context. A screen reader can expose this text to users who cannot see the image.

**Extension:** images that are purely decorative may use an empty alternative (`alt=""`), but that choice depends on the image's role in the surrounding content.

### Hyperlink behavior

An anchor with `href` gives the browser a destination to navigate to. An `a` element containing `src="/cats"` does not automatically become a hyperlink to `/cats`.

## 4. Absolute URLs and root-relative URLs

| URL | Type | Interpretation |
| --- | --- | --- |
| `https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg` | Absolute HTTPS URL | Names the host and resource path explicitly |
| `/cats` | Root-relative path | Resolved from the current site's origin (or file context) |
| `/dogs` | Root-relative path | Same behavior as `/cats` |

A syntactically correct anchor may still lead to a missing destination if the server does not implement the corresponding route. In this lab, the root-relative links are part of the required solution; do not invent local routes merely to demonstrate clicking them.

## 5. Five debugging lessons

| Symptom | Root cause | What to inspect |
| --- | --- | --- |
| Cat photograph missing | Used `href` instead of `src` on `img` | Image source attribute |
| Alternative description not recognized | Used `att` instead of `alt` | Correct name and text value |
| Unnecessary closing markup | Used `</img>` | Void-element rules |
| Cat link not navigable | Used `src` instead of `href` | Anchor's `href` |
| Dog link not navigable | Same attribute mix-up | Anchor's `href` |

These are **HTML markup defects**. Resource connectivity, browser compatibility and complete accessibility require separate consideration.

## 6. Technical English — British English IPA

| Term | IPA | Vietnamese |
| --- | --- | --- |
| Attribute | /ˈæt.rɪ.bjuːt/ | Thuộc tính |
| Source | /sɔːs/ | Nguồn tài nguyên |
| Reference | /ˈref.ər.əns/ | Tham chiếu |
| Alternative | /ɒlˈtɜː.nə.tɪv/ | Thay thế |
| Image | /ˈɪm.ɪdʒ/ | Hình ảnh |
| Anchor | /ˈæŋ.kə/ | Thẻ neo/liên kết |
| Hyperlink | /ˈhaɪ.pə.lɪŋk/ | Siêu liên kết |
| Void element | /vɔɪd ˈel.ɪ.mənt/ | Phần tử rỗng |
| Adoption | /əˈdɒp.ʃən/ | Việc nhận nuôi |
| Accessibility | /əkˌses.əˈbɪl.ə.ti/ | Khả năng tiếp cận |
| Relative URL | /ˈrel.ə.tɪv ˌjuː ɑːr ˈel/ | URL tương đối |
| Debugging | /ˌdiːˈbʌɡ.ɪŋ/ | Gỡ lỗi |

## 7. Self-assessment — answer before consulting the source

**Remember**
1. Which attribute specifies the address of an embedded image, its text alternative and an anchor's target?
2. Which of the two elements, `img` and `a`, is void?

**Understand**
3. Why will `<img href="cats.jpg">` not load the image as intended?
4. Why does `alt` provide better semantics than an invented `att` attribute?

**Apply**
5. In a temporary file, correct `<img href="dog.jpg" att="Brown dog"></img>`.
6. Make `<a src="/adopt">Adopt now</a>` a proper hyperlink.

**Analyze**
7. The words “Visit cats page” appear but are not clickable. Which markup and DOM details would you inspect?
8. What is the difference between an anchor without `href` and a valid anchor whose destination returns HTTP 404? *(Extension)*

**Evaluate — extension**
9. Is passing every freeCodeCamp check sufficient to establish that the page is fully accessible? Explain what evidence would still be needed.

**Create — extension**
10. Design an HTML-only display for two coastal-engineering field stations. Include one image with meaningful `alt` and two navigation links; justify their attributes.

## 8. Personal checklist

- [ ] I choose `src`, `alt` and `href` according to the element's purpose.
- [ ] I know why `img` does not have `</img>`.
- [ ] I understand when an image needs useful alternative text.
- [ ] I can distinguish URL validity from resource or route availability.
- [ ] I can explain what the exercise checks do and do not establish.

Source: [index.html](./index.html). Cross-lesson synthesis: [RWD_REVIEW.md](../../RWD_REVIEW.md).
