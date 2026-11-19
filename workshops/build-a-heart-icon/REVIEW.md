# Workshop 06 — Conceptual Review / Ôn tập kiến thức

**Activity:** Build a Heart Icon · freeCodeCamp Responsive Web Design V9
**Evidence:** Step 6 screenshot displays **100% complete** and **"Your code passes."**
**Source:** [index.html](./index.html) — the complete code supplied by the learner.
**Scope:** Inline SVG, drawing coordinates, path data and fill colour. Extensions are distinguished from completed practice.

## 1. Conceptual overview / Khái niệm

**SVG — Scalable Vector Graphics** /ˈskeɪ.lə.bəl ˈvek.tə ˈɡræf.ɪks/: đồ họa vector có thể mở rộng. SVG describes geometry using structured markup and mathematical coordinates. In contrast, a raster image such as a typical JPEG or PNG represents image samples on a pixel grid.

The completed HTML creates **one SVG element, one path and one red heart**, with no embedded bitmap, script, CSS framework, hover effect or animation. The HTML document provides the host page; the SVG subtree provides the shape.

### Source contract

```html
<svg width="24" height="24" viewBox="0 0 24 24" fill="red">
  <path d="M12 21s-6-4.35-9.33-8.22C-.5 7.39 3.24 1 8.4 4.28 10.08 5.32 12 7.5 12 7.5s1.92-2.18 3.6-3.22C20.76 1 24.5 7.39 21.33 12.78 18 16.65 12 21 12 21z"></path>
</svg>
```

## 2. `<svg>`: viewport versus coordinate space

| Attribute | Learner's value | Interpretation |
| --- | --- | --- |
| `width` | `24` | The rendered SVG viewport's width (24 CSS px in this example). |
| `height` | `24` | The rendered SVG viewport's height (24 CSS px). |
| `viewBox` | `0 0 24 24` | Four numbers: `min-x min-y width height` in internal user units. |
| `fill` | `red` | The initial fill applied to the shape, inherited through the SVG tree. |

**Viewport** /ˈvjuː.pɔːt/ is the displayed region. **Coordinate system** /kəʊˈɔː.dɪ.nət ˈsɪs.təm/ defines positions in the drawing. Since both width and height are 24 and the viewBox dimensions are also 24×24, one drawing unit maps directly to one CSS pixel at the declared size under the default scale.

The `viewBox` does **not** determine the HTML page's viewport, and it is not another name for `width`/`height`. Its four values should be read in order: `0` (minimum x), `0` (minimum y), `24` (drawing width), `24` (drawing height).

**Extension:** if width and height change to `48` while the viewBox remains `0 0 24 24`, the vector normally scales up to occupy the larger viewport under the default aspect-ratio behaviour. Inspect the browser for exact visual results. Do not confuse SVG scaling with the browser's device-pixel ratio or responsive CSS.

## 3. `<path>` and the `d` attribute

The path's `d` (path data) value is a compact sequence of geometry commands and numeric coordinates. It is not a URL or a literal text label. This activity uses commands including:

| Command | General purpose | Point to remember |
| --- | --- | --- |
| `M` | **moveto** — set the starting point | Uppercase uses absolute coordinates. |
| `s` | **smooth cubic Bézier** curve | Lowercase uses relative coordinate values. |
| `C` | **cubic Bézier** curve | Uppercase uses absolute coordinates. |
| `z` | **closepath** — close the current contour | Returns to the subpath's starting point. |

**Bézier curve** /ˈbeɪ.zi.eɪ kɜːv/: đường cong Bézier. The text `M12 21` moves to a position in the SVG user coordinate system. The remaining numbers control curves forming the rounded heart contour. The source uses compressed notation and negative numeric values; changing arbitrary values without understanding command boundaries can distort the shape.

A `path` is not inherently a heart; it becomes a heart because of its **specific** path data. The `svg` element alone defines the drawing context but not the geometry.

## 4. `fill` and visual output

`fill="red"` on the parent `<svg>` establishes a red SVG fill value that the child `<path>` uses unless overridden. This is different from painting the full 24×24 square red; the fill colours the area enclosed by the path's shape.

- The browser's background remains transparent outside the path by default.
- `fill` is not the same as `stroke`: fill colours the interior while stroke paints outlines.
- **Extension:** CSS can also affect SVG presentation properties, but the completed workshop adds no CSS rules.
- An icon with a red colour is not automatically a button and has no click action here.

## 5. Inline SVG versus `<img>` and icon libraries

| Method | Where is shape data? | Scope of this lesson |
| --- | --- | --- |
| Inline `<svg><path ...></path></svg>` | Inside the HTML/SVG DOM | **Practiced** |
| `<img src="heart.svg" alt="...">` | In a separate SVG file loaded as an image | **Explained comparison only** |
| Font or icon library | Provided by a package or stylesheet | **Not used** |
| PNG/JPEG | Raster image resource | **Not used** |

Inline SVG permits direct inspection of the graphic's markup. External icon sources and libraries may be useful in larger applications, but no such dependency exists in this submission.

## 6. Debugging and evidence / Gỡ lỗi và bằng chứng

| Symptom | Investigation |
| --- | --- |
| Blank page | Verify the `<svg>` is inside `<body>` and `<path>` is nested correctly. |
| Icon absent or distorted | Inspect path `d` and `viewBox`; check for misplaced characters or incomplete quotes. |
| Heart has no red fill | Confirm `fill="red"` is present and not overridden. |
| Unexpected size | Inspect `width`, `height`, CSS scaling and browser zoom separately. |
| Path looks clipped | Verify that the drawing coordinates and viewBox correspond. |
| Checker fails | Compare the exact required attributes, nesting and path data for the current step. |

The screenshot confirms the learner finished the **six-step workshop at 100%**. That is evidence of lesson acceptance, not proof of cross-browser parity, screen-reader semantics, keyboard behavior, or a production-ready icon system. A visual icon with no interactive purpose also does not become keyboard-operable simply by using SVG.

## 7. Accessibility / Khả năng tiếp cận — extension

If the heart conveys meaning, its accessible name or surrounding text should communicate that meaning. If it is purely decorative beside equivalent text, it may instead be hidden from assistive technology. The correct choice depends on context; adding an arbitrary label is not always the right solution. This submission uses the attributes explicitly shown in the exercise; it does **not** claim an accessibility audit.

## 8. Technical vocabulary and pronunciation / Từ vựng và phiên âm

British English IPA is supplied for learning; markup tokens such as `viewBox` and `fill` should be read as code identifiers.

| English | IPA | Tiếng Việt |
| --- | --- | --- |
| Heart icon | /hɑːt ˈaɪ.kɒn/ | Biểu tượng trái tim |
| Vector graphics | /ˈvek.tə ˈɡræf.ɪks/ | Đồ họa vector |
| Scalable | /ˈskeɪ.lə.bəl/ | Có thể mở rộng / thay đổi tỷ lệ |
| Viewport | /ˈvjuː.pɔːt/ | Vùng hiển thị |
| Coordinate | /kəʊˈɔː.dɪ.nət/ | Tọa độ |
| Dimension | /daɪˈmen.ʃən/ | Kích thước |
| Width | /wɪdθ/ | Chiều rộng |
| Height | /haɪt/ | Chiều cao |
| Path | /pɑːθ/ | Đường dẫn hình học |
| Geometry | /dʒiˈɒm.ə.tri/ | Hình học |
| Curve | /kɜːv/ | Đường cong |
| Fill | /fɪl/ | Màu tô phần bên trong |
| Stroke | /strəʊk/ | Nét viền |
| Attribute | /ˈæt.rɪ.bjuːt/ | Thuộc tính |
| Browser | /ˈbraʊ.zə/ | Trình duyệt |
| Raster | /ˈrɑː.stə/ | Đồ họa điểm ảnh |
| Resolution | /ˌrez.əˈluː.ʃən/ | Độ phân giải |
| Accessibility | /əkˌses.əˈbɪl.ə.ti/ | Khả năng tiếp cận |
| Transparent | /trænsˈpær.ənt/ | Trong suốt |

## 9. Self-assessment — answer independently

### Remember and understand / Nhớ và hiểu

1. What does SVG stand for, and how does vector graphics differ from raster graphics?
2. How many SVG and path elements appear in this workshop's final source?
3. What do the four `viewBox` numbers mean, in order?
4. Why do `width="24"` and `height="24"` not replace the `viewBox`?
5. Where does the heart's actual shape come from: `svg`, `fill`, or `path d`?
6. Why does `fill="red"` colour the heart rather than the entire square viewport?
7. What is the difference between `fill` and `stroke`?
8. What is the distinction between uppercase `M` and lowercase `s` in path data?

### Apply and debug / Vận dụng và gỡ lỗi

9. A page contains `<svg></svg>` but no visible heart. What would you inspect first?
10. Change the size from 24×24 to 48×48 while keeping the viewBox. What outcome would you expect? How would you verify it?
11. A copied `d` attribute accidentally loses a quotation mark. How could that affect parsing?
12. A heart renders black rather than red. Which attributes or styles should you inspect?
13. Explain why a red SVG icon does not implement a working favourite/like button.
14. When would you place the path geometry inline rather than load a separate SVG file?
15. What exactly does the freeCodeCamp Step 6 screenshot establish, and what does it leave untested?

### Analyze and extend / Phân tích và mở rộng

16. How can an SVG viewport and internal coordinate system have different physical and numerical dimensions?
17. Compare inline SVG scaling with increasing the dimensions of a small raster image.
18. Explain why a path can have a viewport larger than its actual filled area.
19. How might you test whether the same icon is visible at 100%, 200% and 400% browser zoom?
20. **Extension:** for a heart used as a "Save favourite" control, what additional HTML behavior and accessible naming would be required?
21. **Extension:** for a decorative heart beside an already-labelled control, how would you avoid duplicate spoken content?
22. **Coastal engineering application:** propose an SVG symbol for a monitoring station on a map. What would represent geometry, what would represent data, and what would represent interaction?

Questions are intentionally left unanswered for active recall. Compare each explanation against the [source](./index.html), browser Elements panel and official learning material.

## 10. Maintenance

Keep the learner's originally accepted code distinct from experimental enhancements. No completion dates, Python test scripts, local updater scripts, JavaScript, CSS or downloaded binary graphics belong in this workshop's committed three-file archive.
