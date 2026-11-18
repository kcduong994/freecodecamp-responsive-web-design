# Workshop 03 — Conceptual Review / Ôn tập kiến thức

**Activity:** Build a Bookstore Page · freeCodeCamp Responsive Web Design V9
**Evidence:** Learner's original HTML accepted in Step 19, **19/19 (100%)**
**Scope:** HTML document, `div`, `class`, `id`, nested book cards, headings, paragraphs, buttons and browser behavior.
**Method:** Source-grounded explanation → technical distinctions → error analysis → independent questions. The advanced examples are marked *Extension*.

## 1. What the actual source constructs

The completed page is a static book-catalog layout with **two books** and **four buttons**.

```html
<div class="card-container">
  <div class="card" id="sally-adventure-book">
    <h2>Sally's SciFi Adventure</h2>
    <p>This is an epic story of Sally and her dog Rex as they navigate through other worlds.</p>
    <button class="btn">Buy Now</button>
  </div>
  <div class="card" id="dave-cooking-book">
    <h2>Dave's Cooking Adventure</h2>
    <p>This is the story of Dave as he learns to cook everything from pancakes to pasta, one recipe at a time.</p>
    <button class="btn">Buy Now</button>
  </div>
</div>
```

Below the cards is a paragraph inviting the reader to review selections, followed by a `div` with `class="btn-container"` containing two buttons with `id="view-cart-btn"` and `id="checkout-btn"`. The full HTML is in [index.html](./index.html).

**Separate three layers:** content/structure = HTML; presentation (future) = CSS; dynamic behavior (future) = JavaScript and, for real purchases, a secure commerce system. A browser's default rendering shows the content even without authored CSS.

## 2. Elements, tags and attributes — three different things

Consider:

```html
<div class="card" id="sally-adventure-book">
  <h2>Sally's SciFi Adventure</h2>
</div>
```

- **Element:** the complete `div` node, including its content and child heading.
- **Opening tag:** `<div class="card" id="sally-adventure-book">`.
- **Attributes:** `class` and `id` within that opening tag.
- **Closing tag:** `</div>`.
- **Nested child:** the `h2` element is a child of the outer `div`.

`class` and `id` are **attributes**; `card` and `sally-adventure-book` are **attribute values**, not tag names. No `<card>` element was created in this lesson.

### 2.1 Why is `div` used?

`div` is a **generic grouping element**. It creates a container in the DOM but does **not** intrinsically announce "book", "article", "product", "cart" or "navigation". This is useful when the structure is a neutral wrapper or will be styled via CSS. Do not assume a `div` itself adds a card border, a shopping-card meaning, a grid or spacing.

The workshop has one outer `.card-container`, two `.card` descendants, and one lower `.btn-container`. The code alone does not give these containers special display properties.

### 2.2 HTML nesting and DOM hierarchy

Correctly closing each inner card before closing the outer card container matters. Otherwise the DOM may unexpectedly place later book content within an earlier card, changing relationships and future CSS behavior. Developers can inspect the actual nested tree in **Developer Tools → Elements**, not only the raw source text.

## 3. `class` versus `id`: group identity and individual identity

| Question | `class` | `id` |
| --- | --- | --- |
| Role | Assign one or more class tokens to an element | Give an element one document-unique identifier |
| Reuse | Common and intentional | Should not repeat within the same document |
| Number per element | `class="card featured"` can contain multiple tokens | One `id` attribute per element; its value must be unique |
| Source examples | `card`, `card-container`, `btn`, `btn-container` | `sally-adventure-book`, `dave-cooking-book`, `view-cart-btn`, `checkout-btn` |
| Future CSS (extension) | `.btn { ... }` | `#checkout-btn { ... }` |
| Future JS (extension) | `document.querySelectorAll('.btn')` | `document.getElementById('checkout-btn')` |

**Why both on the same button?** The `Checkout` button is part of the shared group `.btn`, while `id="checkout-btn"` singles it out. They have different purposes. The actual page includes one class on each `button`; the `btn` class does not, by itself, style or activate the button.

**Important distinction:** class and ID values are case-sensitive in common CSS/DOM matching contexts; careless capitalization changes can break selectors. IDs may be technically valid with many characters, but consistent, human-readable tokens without spaces make maintenance and CSS/JS targeting easier.

## 4. Headings, paragraphs and book-card meaning

There is one `h1` — **XYZ Bookstore** — and two `h2` elements, one for each title. These headings establish a logical content hierarchy. The initial and checkout-guidance paragraphs are siblings of the card container; the book-description paragraphs are children of the individual book-card containers.

This hierarchy matters for reading order, navigation with assistive technology and future styling. Do not choose heading levels only for font size. A `h2` does not need to be styled to serve its heading role; conversely, a `div` styled as big bold text does not automatically become a semantic heading.

**Extension — not required by Workshop 03:** a richer production catalog might use `main` for the primary page region, `article` or another appropriate semantic grouping for each independently meaningful book item, images with meaningful alternatives, prices and explicit links. Those are improvements to evaluate later, not extra elements in the completed freeCodeCamp exercise.

## 5. Buttons are controls, not a working shopping cart

The workshop uses four real HTML `button` elements:

1. "Buy Now" inside Sally's card.
2. "Buy Now" inside Dave's card.
3. "View Cart" (`id="view-cart-btn"`).
4. "Checkout" (`id="checkout-btn"`).

A native `button` is normally keyboard-focusable and exposes its label to assistive technology. But the source contains **no JavaScript event handler**, cart state, product ID binding, payment integration or form submission endpoint. Clicking a "Buy Now" button therefore does **not** add anything to a cart on this page.

**Extension:** when a button is used inside a future `form`, the default button type can act as `submit`; use `type="button"` for an action that must not submit a form. No form is present in this workshop, so its existing buttons are not submitting purchases.

**Security connection — extension:** a real checkout would require authoritative backend validation, price calculation, inventory rules, authentication/payment handling and protection against tampered browser input. A front-end button label alone is not a commerce implementation.

## 6. Source order, visual layout and responsive design

The source order is: main heading → introduction → card container (Sally then Dave) → guidance paragraph → two final buttons. Without CSS, the browser displays this as ordinary document flow; the user-provided Preview shows text and buttons rather than styled book tiles. **`class="card"` does not generate a visual card automatically.**

Later CSS can lay cards out as a responsive grid or flex row without changing the document order. Visual position should not contradict keyboard/tab or screen-reader order. This makes HTML structure important even before the first CSS declaration.

**Compare with Lab 03:** `ul` and `ol` are semantically meaningful lists; `div` is only generic grouping. One should not replace lists with `div` merely to imitate bullet formatting. Likewise, adding many `div` elements without a clear containment purpose can make maintenance harder.

## 7. How to debug and verify

| Situation | Likely explanation | Diagnostic action |
| --- | --- | --- |
| `card` seems not to have borders | No CSS styles have been authored | Inspect computed styles; confirm lesson is HTML-only |
| `Buy Now` does nothing | No click handler or cart implementation | Inspect source for behavior; do not infer commerce from labels |
| `#view-cart-btn` does not select the right element | ID spelling mismatch or duplicate ID | Compare the actual `id` attribute and inspect DOM |
| Second book is nested inside first | Closing `</div>` missing or moved | Inspect DOM hierarchy in Elements |
| Both buttons styled alike later | Both share `.btn` class | Inspect matching CSS selectors when studying CSS |
| Four buttons are not reached in expected sequence | Incorrect source order, hidden/disabled controls or future CSS/JS changes | Test Tab and Shift+Tab in a browser |
| FreeCodeCamp shows 100% | The lesson's tests accepted the submitted source | Do not extrapolate to visual/a11y/commerce certification |

**Verified by evidence:** the user-provided final-step screenshot reports **100%** for Workshop 03.
**Not claimed:** independent freeCodeCamp rerun of archived file; automated accessibility audit; responsive visual test suite; functioning checkout; GitHub commit/push of this new package.

## 8. English vocabulary — British English IPA / Từ vựng và phiên âm

| English term | IPA (UK) | Tiếng Việt | Relevant HTML idea |
| --- | --- | --- | --- |
| Bookstore | /ˈbʊk.stɔː/ | Cửa hàng sách | Page topic |
| Container | /kənˈteɪ.nə/ | Vùng chứa | `div.card-container` |
| Card | /kɑːd/ | Thẻ nội dung | `div.card` |
| Class | /klɑːs/ | Lớp, nhóm | `class="btn"` |
| Identifier | /aɪˈden.tɪ.faɪ.ə/ | Định danh | `id` |
| Attribute | /ˈæt.rɪ.bjuːt/ | Thuộc tính | `class`, `id`, `lang` |
| Element | /ˈel.ɪ.mənt/ | Phần tử | `div`, `button`, `h2` |
| Nest | /nest/ | Lồng bên trong | Parent/child HTML |
| Heading | /ˈhed.ɪŋ/ | Tiêu đề | `h1`, `h2` |
| Paragraph | /ˈpær.ə.ɡrɑːf/ | Đoạn văn | `p` |
| Browse | /braʊz/ | Duyệt, xem qua | Welcome description |
| Checkout | /ˈtʃek.aʊt/ | Thanh toán/đến bước thanh toán | Button label |
| Cart | /kɑːt/ | Giỏ hàng | "View Cart" |
| Button | /ˈbʌt.ən/ | Nút bấm | `button` |
| Selector | /sɪˈlek.tə/ | Bộ chọn | CSS extension |
| Semantic | /sɪˈmæn.tɪk/ | Ngữ nghĩa | `h2` vs `div` |
| Accessibility | /əkˌses.əˈbɪl.ə.ti/ | Khả năng tiếp cận | Keyboard and naming |
| Interaction | /ˌɪn.təˈræk.ʃən/ | Tương tác | Future JS |

IPA represents common British English pronunciation; variant accents may differ. Each term here is grounded in the lesson or explicitly marked as a connection to later work.

## 9. Questions for independent review — chưa kèm đáp án

**A. Recall and explain**

1. Define an HTML **element**. Which part of `<div class="card">...</div>` is an attribute?
2. How many book cards and buttons are present in the actual completed file? Identify each button's text.
3. Why are `head` and `body` siblings under `html` rather than nested inside each other?
4. What does `div` mean semantically? Why is `div` suitable as a neutral container?
5. Why can two different elements share `class="card"` but should not share the same `id`?
6. What difference does a `h2` make compared with a styled `div` containing the same text?

**B. Apply and debug**

7. Write the opening tag for a third book card with `class="card"` and a unique `id`.
8. Write HTML for a button that belongs to class `btn` and is uniquely identified as `save-book-btn`.
9. A book appears nested inside another card in Developer Tools. Which opening/closing tags should you examine first?
10. Two buttons use the same `id="checkout-btn"`. What kinds of problems can this cause?
11. If you write `class="btn primary"`, how many class tokens are present? How would you select both in CSS later?
12. Describe the actual parent–child relationship between `div.card-container`, `div.card`, `h2` and `p`.
13. Explain why the screenshot looks like unstyled text even though the source calls its containers `card`.

**C. Analyze, evaluate and extend**

14. Explain why passing all 19 steps does not establish that the "Checkout" button takes payment.
15. What differences would you expect between a `button` and an `a` link when designing a "Read book details" interaction?
16. Why could CSS Grid improve the layout later without requiring the HTML cards to be reordered?
17. What risks arise when CSS visually reorders cards but the DOM/tab order stays unchanged?
18. If you convert the cards into `article` elements, what evidence would justify that semantic choice?
19. Design a simple mental test plan for keyboard navigation, duplicate IDs and content hierarchy.
20. For a real engineering-document catalog, which book-card patterns could be reused, and which commerce-specific features should not be copied?

**Answer policy:** deliberately no answer key. Work through these questions, explain your reasoning and compare with the source. Extensions are for thinking beyond the workshop, not claims that additional curriculum steps were completed.

## 10. Progression to the next lesson

The new tools are `div`, `class` and `id`, used to **organize** elements. Upcoming CSS can use classes/IDs to **style** them; JavaScript may later bind behavior. Preserve the distinction between HTML **structure**, CSS **presentation**, and application **behavior**.

Also see the [repository-wide RWD review](../../RWD_REVIEW.md). This archive contains no completion dates, Python tests or helper scripts.
