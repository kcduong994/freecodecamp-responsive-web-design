"""Dependency-free source checks for freeCodeCamp Responsive Web Design Lab 02.

From the repository root:
    py -m unittest discover -s labs/debug-pet-adoption-page/tests -p "test_*.py" -v
"""
from __future__ import annotations

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

FILE = Path(__file__).resolve().parents[1] / "index.html"
CAT_IMAGE_URL = "https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg"
ALT_TEXT = "Two tabby kittens sleeping together on a couch."
EXPECTED = [
    ("h1", "Welcome to XYZ Pet Adoption!"),
    ("p", "Consider adopting a pet today. We have cats, dogs, rabbits and more."),
    ("h2", "See our cats!"),
    ("img", ""),
    ("h2", "Adopt a cat!"),
    ("a", "Visit cats page"),
    ("h2", "Adopt a dog!"),
    ("a", "Visit dogs page"),
]
VOID = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}
CONTENT = {"h1", "h2", "p", "a", "img"}


class DocumentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.open_tags: list[str] = []
        self.errors: list[str] = []
        self.tags: list[str] = []
        self.elements: list[tuple[str, str]] = []
        self.content_stack: list[list[str]] = []
        self.images: list[dict[str, str | None]] = []
        self.anchors: list[dict[str, str | None]] = []
        self.has_doctype = False
        self.lang = ""
        self.title = ""
        self.in_title = False
        self.charset = ""
        self.viewport = ""

    def handle_decl(self, decl: str) -> None:
        self.has_doctype |= decl.lower() == "doctype html"

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        self.tags.append(tag)
        if tag == "html":
            self.lang = attributes.get("lang") or ""
        if tag == "meta":
            self.charset = attributes.get("charset") or self.charset
            if attributes.get("name") == "viewport":
                self.viewport = attributes.get("content") or ""
        if tag == "title":
            self.in_title = True
        if tag == "img":
            self.images.append(attributes)
            self.elements.append(("img", ""))
        elif tag in CONTENT:
            if self.content_stack:
                self.errors.append("Unexpected nested text elements")
            self.content_stack.append([tag])
        if tag == "a":
            self.anchors.append(attributes)
        if tag not in VOID:
            self.open_tags.append(tag)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        # Handles input like <img /> without misinterpreting it as a closing tag.
        if tag not in VOID:
            self.errors.append(f"Unexpected self-closing non-void element: {tag}")
            return
        self.handle_starttag(tag, attrs)

    def handle_data(self, text: str) -> None:
        if self.in_title:
            self.title += text
        if self.content_stack:
            self.content_stack[-1].append(text)

    def handle_endtag(self, tag: str) -> None:
        if tag in VOID:
            self.errors.append(f"Void element cannot have a closing tag: {tag}")
            return
        if not self.open_tags or self.open_tags[-1] != tag:
            self.errors.append(f"Unbalanced end tag: {tag}; open={self.open_tags}")
            return
        self.open_tags.pop()
        if tag in CONTENT:
            if not self.content_stack or self.content_stack[-1][0] != tag:
                self.errors.append(f"Mismatched content tag: {tag}")
            else:
                fragments = self.content_stack.pop()
                self.elements.append((tag, " ".join("".join(fragments[1:]).split())))
        if tag == "title":
            self.in_title = False


class PetAdoptionLabTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source = FILE.read_text(encoding="utf-8")
        cls.page = DocumentParser()
        cls.page.feed(cls.source)
        cls.page.close()

    def test_01_html5_document_and_language(self) -> None:
        self.assertTrue(self.page.has_doctype)
        self.assertEqual(self.page.lang, "en")
        for tag in ("html", "head", "body"):
            self.assertEqual(self.page.tags.count(tag), 1)

    def test_02_metadata(self) -> None:
        self.assertEqual(self.page.charset.lower(), "utf-8")
        self.assertIn("width=device-width", self.page.viewport)
        self.assertTrue(self.page.title.strip())

    def test_03_well_balanced_markup(self) -> None:
        self.assertEqual(self.page.errors, [])
        self.assertEqual(self.page.open_tags, [])
        self.assertEqual(self.page.content_stack, [])

    def test_04_exact_final_content_and_order(self) -> None:
        self.assertEqual(self.page.elements, EXPECTED)

    def test_05_heading_hierarchy(self) -> None:
        self.assertEqual(Counter(tag for tag, _ in self.page.elements if tag.startswith("h")),
                         Counter({"h1": 1, "h2": 3}))

    def test_06_image_uses_src(self) -> None:
        self.assertEqual(len(self.page.images), 1)
        self.assertEqual(self.page.images[0].get("src"), CAT_IMAGE_URL)
        self.assertNotIn("href", self.page.images[0])

    def test_07_image_uses_alt_not_att(self) -> None:
        self.assertEqual(self.page.images[0].get("alt"), ALT_TEXT)
        self.assertNotIn("att", self.page.images[0])

    def test_08_image_is_void_without_closing_tag(self) -> None:
        self.assertNotRegex(self.source, r"</\s*img\s*>")
        self.assertEqual(self.page.tags.count("img"), 1)

    def test_09_both_links_use_href(self) -> None:
        self.assertEqual(len(self.page.anchors), 2)
        self.assertEqual([link.get("href") for link in self.page.anchors], ["/cats", "/dogs"])
        self.assertTrue(all("src" not in link for link in self.page.anchors))

    def test_10_only_intended_content_tags(self) -> None:
        self.assertEqual([t for t in self.page.tags if t in CONTENT],
                         [tag for tag, _ in EXPECTED])

    def test_11_no_custom_css_or_javascript(self) -> None:
        self.assertFalse({"style", "script", "link"} & set(self.page.tags))
        self.assertIsNone(re.search(r"\son[a-z]+\s*=", self.source, re.I))


if __name__ == "__main__":
    unittest.main(verbosity=2)
