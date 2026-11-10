"""Dependency-free source checks for freeCodeCamp RWD Workshop 01.

Run from the repository root:
    python -m unittest discover -s workshops/build-a-curriculum-outline/tests -p 'test_*.py' -v
"""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

HTML_FILE = Path(__file__).resolve().parents[1] / "index.html"
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
CONTENT_TAGS = {"h1", "h2", "h3", "p"}
EXPECTED_CONTENT = [
    ("h1", "Welcome to freeCodeCamp"),
    ("h2", "Full-Stack Curriculum"),
    ("p", "Learn the skills to become a full-stack developer"),
    ("h3", "Introduction to HTML"),
    ("p", "HTML represents the content and structure of a webpage"),
    ("h3", "Introduction to CSS"),
    ("p", "CSS is used to style a webpage"),
    ("h3", "Introduction to Javascript"),
    ("p", "javaScript adds interactivity to a webpage"),
]

class StrictStructureParser(HTMLParser):
    """Parse the exact simple subset used here; reject mismatched/unfinished tags."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.elements: list[tuple[str, str]] = []
        self._active: list[list[str]] = []
        self.tags: list[str] = []
        self.lang = ""
        self.charset = ""
        self.viewport = ""
        self.doctype = False
        self.title = ""
        self.in_title = False
        self.errors: list[str] = []

    def handle_decl(self, decl: str) -> None:
        if decl.casefold() == "doctype html":
            self.doctype = True

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        props = dict(attrs)
        self.tags.append(tag)
        if tag == "html":
            self.lang = props.get("lang", "") or ""
        if tag == "meta":
            self.charset = props.get("charset", self.charset) or self.charset
            if props.get("name") == "viewport":
                self.viewport = props.get("content", "") or ""
        if tag == "title":
            self.in_title = True
        if tag in CONTENT_TAGS:
            if self._active:
                self.errors.append("Unexpected nested content element")
            self._active.append([tag])
        if tag not in VOID:
            self.stack.append(tag)

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data
        if self._active:
            self._active[-1].append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag in VOID:
            self.errors.append(f"Void HTML element must not have a closing tag: {tag}")
            return
        if not self.stack or self.stack[-1] != tag:
            self.errors.append(f"Unexpected closing tag: </{tag}>, stack={self.stack}")
            return
        self.stack.pop()
        if tag in CONTENT_TAGS:
            if not self._active or self._active[-1][0] != tag:
                self.errors.append(f"Mis-nested content tag: {tag}")
            else:
                parts = self._active.pop()
                content = " ".join("".join(parts[1:]).split())
                self.elements.append((tag, content))
        if tag == "title":
            self.in_title = False

class WorkshopTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source = HTML_FILE.read_text(encoding="utf-8")
        cls.parser = StrictStructureParser()
        cls.parser.feed(cls.source)
        cls.parser.close()

    def test_01_standalone_html5_document(self) -> None:
        self.assertTrue(self.parser.doctype)
        self.assertEqual(self.parser.lang, "en")
        self.assertEqual(self.parser.tags.count("html"), 1)
        self.assertEqual(self.parser.tags.count("head"), 1)
        self.assertEqual(self.parser.tags.count("body"), 1)

    def test_02_document_metadata(self) -> None:
        self.assertEqual(self.parser.charset.casefold(), "utf-8")
        self.assertIn("width=device-width", self.parser.viewport)
        self.assertTrue(self.parser.title.strip())

    def test_03_tags_are_balanced_and_nested(self) -> None:
        self.assertEqual(self.parser.errors, [])
        self.assertEqual(self.parser.stack, [])
        self.assertEqual(self.parser._active, [])

    def test_04_exact_workshop_text_and_order(self) -> None:
        self.assertEqual(self.parser.elements, EXPECTED_CONTENT)

    def test_05_heading_hierarchy(self) -> None:
        headings = [tag for tag, _ in self.parser.elements if tag.startswith("h")]
        self.assertEqual(headings, ["h1", "h2", "h3", "h3", "h3"])

    def test_06_four_paragraphs(self) -> None:
        self.assertEqual(sum(tag == "p" for tag, _ in self.parser.elements), 4)

    def test_07_only_workshop_content_tags(self) -> None:
        actual_content = [tag for tag in self.parser.tags if tag in CONTENT_TAGS]
        self.assertEqual(actual_content, [tag for tag, _ in EXPECTED_CONTENT])

    def test_08_no_added_css_or_javascript(self) -> None:
        self.assertNotIn("script", self.parser.tags)
        self.assertNotIn("style", self.parser.tags)
        self.assertNotIn("link", self.parser.tags)
        self.assertIsNone(re.search(r"\son[a-z]+\s*=", self.source, re.IGNORECASE))

if __name__ == "__main__":
    unittest.main(verbosity=2)
