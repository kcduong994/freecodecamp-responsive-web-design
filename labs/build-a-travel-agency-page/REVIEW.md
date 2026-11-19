# Lab 04 — Travel Agency Page: Conceptual Review / Ôn tập HTML

**Evidence:** The learner's **original** freeCodeCamp submission passed its built-in checks at **100%**, although the Preview showed three missing images. This repository preserves a **polished HTML edition**, which has not been re-submitted to the official site. The following review explains what was practiced, what was corrected and what remains unverified.

## 1. The user-story contract: exactness and meaningful content

This lab combines multiple dimensions of a webpage:

- **Document contract:** `<!DOCTYPE html>`, `<html lang="en">`, `head`, `body`, a meaningful `title`, and two distinct `meta` tags.
- **Content hierarchy:** one `h1`, two named `h2` headings, and paragraphs explaining the destination and packages.
- **List structure:** one `ul` with exactly two `li` children, each with an `a` containing the required label.
- **Media structure:** at least three `figure` elements, each containing `a > img` followed by a sibling `figcaption`.
- **Attribute contract:** exactly five links with the prescribed `href` and `target`; each image with `src` and descriptive `alt`.

Think in **DOM relationships**, not merely visual alignment. The tags' nesting and the text content must satisfy the checker simultaneously. The original screenshot showed the built-in checker reaching 100%; it did not show images successfully downloading.

## 2. Metadata: text encoding, page title, search description

```html
<head>
  <meta charset="UTF-8">
  <meta name="description" content="Discover guided journeys and private tours.">
  <title>Travel Agency Page</title>
</head>
```

**Distinguish the three responsibilities:**

| Construct | Role | Does it normally render as body text? |
| --- | --- | --- |
| `meta charset="UTF-8"` | Declares character encoding | No |
| `meta name="description" content="..."` | Describes page content for consumers such as search engines | No |
| `title` | Supplies the document title for browser UI and other consumers | Not as body content |

The original learner used `Trave Origin` as the document title; the archive uses the exact lesson title. A description is not a substitute for an actual paragraph on the page. Search engines **may** use the description as a search snippet, but this tag does not guarantee indexing, a particular snippet or rankings. This is background explanation, not an SEO performance result.

## 3. Package links: `ul > li > a`

The learner previously tried malformed markup resembling `<a <li>items1</li>` and `<a/>`, which made the checker report wrong list structure. The correct relationship is:

```html
<ul>
  <li><a href="https://www.freecodecamp.org/learn" target="_blank">Group Travels</a></li>
  <li><a href="https://www.freecodecamp.org/learn" target="_blank">Private Tours</a></li>
</ul>
```

- The **direct children** of `ul` are the two `li` elements.
- Each `li` holds one `a` with visible link text.
- The complete anchor has an opening and closing tag. `<a/>` does not substitute for `</a>` in HTML.
- The class of an element or visual bullet style is not a replacement for correct nesting.
- For this lab, the two labels, destination and new-tab behavior are explicit acceptance requirements.

The `ul` is a **list of choices**, not a numerical procedure. A real travel site might link each offer to a separate booking route, but the exercise deliberately requires a shared educational URL.

## 4. The image relationship: `figure > a > img` and `figcaption`

```html
<figure>
  <a href="https://www.freecodecamp.org/learn" target="_blank">
    <img src="https://cdn.freecodecamp.org/curriculum/labs/alps.jpg"
         alt="Rocky Alpine peaks illuminated by evening sunlight">
  </a>
  <figcaption>Discover dramatic mountain scenery in the Alps.</figcaption>
</figure>
```

The direct children of `figure` are **first `a`, then `figcaption`**. The image is a child of the anchor, not a direct sibling of the anchor. The caption is outside the anchor, not nested within it. This is stricter than merely requiring a picture and text somewhere on the page.

**Do not confuse these things:**

| Construct | What it answers | Characteristic |
| --- | --- | --- |
| `src` on `img` | Which resource should be loaded? | URL for embedded image |
| `alt` on `img` | What information does this image convey if it cannot be perceived? | Accessible textual alternative |
| `href` on `a` | Where does activating this link go? | Link destination |
| `target="_blank"` | Where should the link open? | New browsing context, commonly a tab |
| `figcaption` | What visible caption belongs to this figure? | Normally visible text |

The original attempt used `<figcaption text="1">` with no textual content. `text` is not a special `figcaption` content attribute; put the caption **between the tags**. The revised archive replaces bare numerals with short meaningful phrases.

### Accessibility nuances (technical extension)

- `alt="img1"` is syntactically nonempty but communicates very little about the actual picture.
- A linked image should have an accessible name that communicates the linked content or purpose, rather than meaningless placeholder text.
- `alt` and `figcaption` can complement each other; they need not contain the same sentence word-for-word.
- Images must load in a live browser to be visible. Valid HTML source does not guarantee a successful network request.
- In modern browsers, `target="_blank"` on an anchor implies `rel="noopener"`; adding an explicit `rel="noopener"` is a common defence-in-depth convention. The challenge requires `target`, not an explicit `rel`.

## 5. Why 100% passed despite broken images

The freeCodeCamp completion screenshot simultaneously showed **100% code-check completion** and three broken-image icons in Preview. The original author had used empty `src` values. A checker can validate that an attribute exists and that a syntactic value is present without establishing that an HTTP image resource can be fetched and decoded.

The polished edition uses the provided freeCodeCamp image URLs for the Colosseum, Alps and sea. These were opened successfully when preparing this archive. Their future network availability and actual rendering in the learner's own browser are separate checks.

**Suggested manual verification sequence:**

1. Open `index.html` in a real browser with internet access.
2. Confirm that three images render and the captions correspond to them.
3. Inspect each `img` in Developer Tools → Elements and compare `src` and `alt`.
4. Inspect Developer Tools → Network for failed requests, HTTP statuses and caching.
5. Confirm the two package links and three image links all navigate to the required educational destination and open in a new tab.
6. Inspect keyboard focus order and whether linked images convey meaningful information without seeing the photo.

Browser inspection is an exercise for the learner; no independent cross-browser or screen-reader audit is claimed here.

## 6. Common errors and diagnostic methods

| Symptom | Likely cause | Corrective action |
| --- | --- | --- |
| `ul` does not have two `li` items | Malformed `<a <li>` markup, anchors wrapped outside the list items | Make two valid `li` direct children, with each `a` inside an `li` |
| Exact link-label test fails | Placeholder `items1`, wrong capitalization or spacing | Use `Group Travels` and `Private Tours` exactly |
| Caption is empty | `text="1"` attribute used instead of element content | Use `<figcaption>Explore Rome</figcaption>` |
| `figure` child-order test fails | `figcaption` nested inside `a`, or `img` not inside `a` | Use `figure > a > img` and sibling `figcaption` |
| Image missing but source test passes | Empty, invalid, blocked or unavailable `src` | Verify the full URL and the Network request |
| Title test fails | Misspelled or different `title` text | Check explicit user-story wording |
| New-tab link test fails | `target` is absent or has another value | Use `target="_blank"` for all five anchors |
| SEO description test fails | `content` is empty or the second `meta` is missing | Place `meta name="description"` in `head` with nonempty `content` |

Debug from the **first failed invariant**, not the last visible symptom. HTML error recovery can reshape the DOM after malformed nesting; inspect the DOM after correcting syntax.

## 7. Technical vocabulary / Từ vựng chuyên ngành (British English IPA)

| English | IPA | Vietnamese explanation |
| --- | --- | --- |
| Travel agency | /ˈtræv.əl ˈeɪ.dʒən.si/ | Công ty du lịch |
| Destination | /ˌdes.tɪˈneɪ.ʃən/ | Điểm đến |
| Itinerary | /aɪˈtɪn.ə.rər.i/ | Lịch trình hành trình |
| Package | /ˈpæk.ɪdʒ/ | Gói du lịch |
| Group travel | /ɡruːp ˈtræv.əl/ | Du lịch theo nhóm |
| Private tour | /ˈpraɪ.vət tʊə/ | Chuyến du lịch riêng |
| Description | /dɪˈskrɪp.ʃən/ | Phần mô tả |
| Metadata | /ˈmet.əˌdeɪ.tə/ | Siêu dữ liệu |
| Search engine | /sɜːtʃ ˈen.dʒɪn/ | Công cụ tìm kiếm |
| Link | /lɪŋk/ | Liên kết |
| Anchor | /ˈæŋ.kə/ | Thẻ neo tạo liên kết `a` |
| Figure | /ˈfɪɡ.ə/ | Hình minh họa có ngữ cảnh |
| Caption | /ˈkæp.ʃən/ | Chú thích hiển thị |
| Alternative text | /ɒlˈtɜː.nə.tɪv tekst/ | Văn bản thay thế cho ảnh |
| Nested | /ˈnes.tɪd/ | Được lồng bên trong |
| Attribute | /ˈæt.rɪ.bjuːt/ | Thuộc tính của phần tử |
| Browser | /ˈbraʊ.zə/ | Trình duyệt |
| Accessibility | /əkˌses.əˈbɪl.ə.ti/ | Khả năng tiếp cận |

## 8. Self-assessment questions — answer without looking at the source

### A. Recall and explain

1. What is the difference between an `img` element and the resource referenced by its `src`?
2. What does `meta charset="UTF-8"` establish, and how is it different from `html lang="en"`?
3. What is the difference between a `<title>` and the page's `<h1>`?
4. What is the role of `meta name="description"`, and why does it not guarantee search ranking?
5. What are the two required package labels and which elements own their visible text?
6. Explain the difference between `ul`, `li` and `a` in the package section.
7. What is the semantic purpose of `figure` and `figcaption`?
8. What is the difference between `href` and `src`?

### B. Apply and debug

9. Correct `<ul><a <li>Group Travels</li><li>Private Tours</li><a/></ul>`.
10. Why does `<figcaption text="1"></figcaption>` fail the visible-caption requirement?
11. Draw the DOM tree for one `figure` and name its two direct children in order.
12. A `figure` contains `<a><img ...><figcaption>Rome</figcaption></a>`. Why does it not satisfy the lab's specific child order?
13. A page includes `alt="img1"`. What information is missing for a nonvisual user?
14. A link looks like ordinary text rather than underlined text. Does that alone prove its HTML structure is invalid?
15. The Network panel reports 404 for an image; what does this say about `src`, and what does it **not** prove about the rest of the DOM?
16. Write a valid second `meta` element with a meaningful nonempty travel description.
17. How could you use the Elements panel to verify that there are exactly five anchors?
18. Would adding an `<ol>` of tour steps satisfy the requirement for exactly two `ul > li` package items? Explain.

### C. Evaluate and design

19. Why is an official 100% badge insufficient to conclude that the visual page is production-ready?
20. Should every linked image always open a new tab? Distinguish challenge requirements from usability design.
21. Explain why three identical `alt` values would be unhelpful even though all three images depict travel scenes.
22. Compare the strengths of `figure` and a generic `div` for an itinerary photograph and caption.
23. **Extension:** For a real destination website, what additional information and actions are necessary before it could support an actual booking?
24. **Extension:** How would you test the page with images disabled, a keyboard, a screen reader and a narrow viewport?

The questions deliberately have **no answer key**. Use the completed HTML and browser tools to verify your explanations, then extend the answers with evidence. 

## 9. Connections to previous work and future topics

- **Workshop 01:** `h1`, `h2` and `p` express hierarchy and text meaning.
- **Lab 01:** malformed element syntax can distort DOM structure.
- **Lab 02:** `img src/alt` and `a href` solve different problems.
- **Workshop 02:** `figure`, `figcaption` and `target="_blank"` were introduced in a guided exercise.
- **Lab 03:** a source checker can pass while an image resource fails to load.
- **Workshop 03:** neutral `div` containers and class/ID attributes organize content without creating domain semantics.
- **This lab:** combines metadata, exact list/link requirements and a three-image itinerary gallery under independent user stories.
- **Future CSS/JavaScript:** styling and interactive reservation functionality are separate learning objectives, not present here.

**Maintenance rule:** preserve the difference between practiced constructs, technical explanation and unverified extensions. Keep learning documents free of completion dates, Python tests and repository-update scripts.
