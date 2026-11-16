# Lab 03 — Build a Recipe Page: Conceptual Review / Ôn tập HTML

**Evidence:** The learner's original freeCodeCamp source passed the challenge at **100%**. This repository stores a **lightly edited edition**, whose individual edits must not be conflated with the original official result.

## 1. From user stories to semantic HTML

A **user story** (yêu cầu từ góc nhìn người dùng) describes a desired observable result, such as: “There should be an ordered list of at least four instruction steps.” Converting that into HTML requires identifying the exact element and the position in the document:

- Overall document contract → `<!DOCTYPE html>`, `html`, `head`, `body`.
- Recipe metadata → `title`, `meta charset="UTF-8"` inside `head`.
- Main page title → exactly one `h1` in `body`.
- Introductory explanation → `p` below `h1`.
- Ingredients section → `h2` followed by `ul` with `li` children.
- Instructions section → a second `h2` followed by `ol` with `li` children.
- Recipe illustration → `img` with `src` and `alt`.

A page can render even when a validator considers an item wrong. The important questions are: **what does the code say, what does the browser parse, and what does the test require?**

## 2. The document tree: `head` is not inside `body`

The learner initially placed `head` inside `body` and saw seemingly contradictory freeCodeCamp errors for `title`, `meta` and `body` placement. The corrected hierarchy is:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Fish Recipe</title>
  </head>
  <body>
    <h1>Fish Recipe</h1>
  </body>
</html>
```

**Key lesson:** `head` and `body` are siblings within `html`; the browser does not treat a nested `<head>` written inside `<body>` as the author's intended document head. Error recovery can make the resulting DOM differ from the source.

- `lang="en"` declares the **language** of the page.
- `charset="UTF-8"` declares its **character encoding**.
- `title` identifies the document in the browser tab and other contexts; `h1` names its visible content.
- `meta` is a **void element**; it does not have a closing `</meta>` tag.

## 3. Why `ul` and `ol` are not interchangeable

The ingredients are a set of items to obtain or prepare, with no required sequence. The **unordered list** (`ul`) expresses that relationship. The cooking method is a **sequence of actions**, so an **ordered list** (`ol`) is appropriate.

```html
<h2>Ingredients</h2>
<ul>
  <li>2 fish fillets</li>
  <li>Cooking oil</li>
</ul>

<h2>Instructions</h2>
<ol>
  <li>Pat the fish dry.</li>
  <li>Season the fish.</li>
</ol>
```

The marker presentation (bullets or numbers) comes from default browser styling, but the underlying choice is **semantic**. An `li` belongs in a list container rather than being an arbitrary standalone line of text.

## 4. Image source correctness versus test success

The initial user submission used:

```html
<img src="abcd.com/fish.jpg" alt="that is fish">
```

The freeCodeCamp checker passed, but the browser showed a broken-image indicator. Without a URL scheme and a working relative file, `abcd.com/fish.jpg` is interpreted as a **relative path**, not as a guaranteed valid image on the public domain `abcd.com`. Passing a syntactic `src` check does **not** establish that the resource exists or can be retrieved.

The archived edition uses an HTTPS Wikimedia Commons thumbnail of fried fish fillets (CC0 1.0). Its `alt` describes the relevant visual content. It also specifies `width` and `height` to reserve layout space. The archive **does not bundle image bytes**; resource loading still depends on network access and the image host.

**Independent troubleshooting:** Developer Tools → Network → check the image request URL, status, content type and any blocking errors. Developer Tools → Elements → confirm the `src` actually points to that resource. Neither a correct DOM nor an official exercise check alone proves network success.

## 5. Meaningful content is different from merely meeting counts

The original `cook1`, `cook2`, `cook3`, `cook4` satisfied the requirement for four `li` items but did not explain how to prepare fish. A learner should distinguish two kinds of quality:

1. **Structural correctness:** the required HTML elements exist and are arranged properly.
2. **Content usefulness:** the instructions are accurate, understandable, ordered and appropriate to the topic.

The archived edition improves wording and includes a commonly recommended cooked-fish internal temperature, **63°C (145°F)**. That is an example of meaningful content; no food-safety certification or kitchen measurement was performed as part of this programming lab.

## 6. Common errors and how to diagnose them

| Mistake | Why it matters | Better approach |
| --- | --- | --- |
| Putting `head` inside `body` | Browser may reconstruct an unintended DOM | Keep `head` and `body` as siblings |
| Confusing `title` and `h1` | Metadata and visible content serve different roles | Supply both |
| Omitting `lang` or `charset` | Fails stated document requirements | Set `lang="en"`, `charset="UTF-8"` |
| Writing list items without their list | Loses meaningful grouping | Use `ul > li` or `ol > li` |
| Using `ul` for sequential procedure | Removes order semantics | Use `ol` for cooking steps |
| Providing an inaccessible `src` | Broken image despite source test success | Use and verify a retrievable image URL |
| Vague `alt` text | Gives a poor textual alternative | Describe the actual image concisely |
| Treating 100% as deployment proof | Official tests cover a defined scope | Inspect resource loads and actual browser behavior |

## 7. English vocabulary — British English IPA

| Term | UK IPA | Tiếng Việt |
| --- | --- | --- |
| Recipe | /ˈres.ɪ.pi/ | Công thức nấu ăn |
| Ingredient | /ɪnˈɡriː.di.ənt/ | Nguyên liệu |
| Instruction | /ɪnˈstrʌk.ʃən/ | Hướng dẫn |
| Declaration | /ˌdek.ləˈreɪ.ʃən/ | Khai báo |
| Hierarchy | /ˈhaɪə.rɑː.ki/ | Hệ phân cấp |
| Sequence | /ˈsiː.kwəns/ | Trình tự |
| Unordered | /ʌnˈɔː.dəd/ | Không theo thứ tự |
| Ordered | /ˈɔː.dəd/ | Có thứ tự |
| Alternative text | /ɒlˈtɜː.nə.tɪv tekst/ | Văn bản thay thế |
| Fillet | /ˈfɪl.ɪt/ | Miếng phi lê |
| Frying pan | /ˈfraɪ.ɪŋ pæn/ | Chảo rán |
| Season (verb) | /ˈsiː.zən/ | Nêm gia vị |
| Metadata | /ˈmet.əˌdeɪ.tə/ | Siêu dữ liệu |
| Validation | /ˌvæl.ɪˈdeɪ.ʃən/ | Xác thực tính hợp lệ |

## 8. Self-assessment — tự trả lời trước khi xem lại mã nguồn

**Remember / Nhớ**

1. What are the roles of `head`, `title`, `meta`, `body` and `h1`?
2. Which tags create an ordered and an unordered list? What tag creates a list item?

**Understand / Hiểu**

3. Why are `head` and `body` siblings rather than parent and child?
4. Why does a recipe normally use `ul` for ingredients and `ol` for instructions?
5. How are `lang="en"` and `charset="UTF-8"` different?

**Apply / Vận dụng**

6. Write a document with a title, one `h1`, two `h2` headings, an ingredients list and four preparation steps.
7. Correct the snippet `<body><head><title>Soup</title></head></body>`.
8. Explain the problem with `src="abcd.com/fish.jpg"` when no matching local file is provided.

**Analyze / Phân tích**

9. How could freeCodeCamp report **100%** while the page still displays a broken image?
10. How would you distinguish an invalid `src` path from a temporary network error?

**Evaluate and create / Đánh giá và sáng tạo — extension**

11. Which checks establish HTML semantics, and which checks establish that a real image loads?
12. Design a recipe with five meaningful ingredient items and five clear steps. Explain why its final list choices, `alt` description and heading structure are appropriate.

## 9. Completion checklist

- [ ] I can reproduce the `html > head + body` hierarchy from memory.
- [ ] I can distinguish `title` metadata from a visible `h1`.
- [ ] I can use `ul` and `ol` for their intended semantics.
- [ ] I can explain why an image test can pass while its resource fails to load.
- [ ] I can inspect the actual network request when an image appears broken.
- [ ] I know the difference between the original passing exercise and the edited local archive.

Review [README.md](./README.md) for source and image provenance, and [RWD_REVIEW.md](../../RWD_REVIEW.md) for cumulative connections across the five activities.
