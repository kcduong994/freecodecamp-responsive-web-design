"""Standard-library HTML source tests for freeCodeCamp RWD Lab 01.

Run from repo root:
    py -m unittest discover -s labs/debug-camperbots-profile-page/tests -p 'test_*.py' -v
"""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

HTML_FILE = Path(__file__).resolve().parents[1] / "index.html"
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
CONTENT = {"h1", "h2", "h3", "p"}
EXPECTED = [
    ("h1", "Hello from Camperbot!"),
    ("h2", "About"),
    ("p", "My name is Camperbot and I love learning new things."),
    ("h3", "Background and Interests"),
    ("p", "I enjoy solving puzzles."),
]


class StrictProfileParser(HTMLParser):
    """Check the simple HTML subset used by this lab, including balanced tags."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.tags = []
        self.active = None
        self.elements = []
        self.lang = ""
        self.charset = ""
        self.viewport = ""
        self.title = ""
        self.title_open = False
        self.doctype = False

    def handle_decl(self, declaration):
        if declaration.casefold() == "doctype html":
            self.doctype = True

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        attrs = dict(attrs)
        if tag == "html":
            self.lang = attrs.get("lang", "")
        if tag == "meta":
            self.charset = attrs.get("charset", self.charset)
            if attrs.get("name") == "viewport":
                self.viewport = attrs.get("content", "")
        if tag == "title":
            self.title_open = True
        if tag in CONTENT:
            if self.active is not None:
                self.errors.append("Nested text element found")
            self.active = [tag, ""]
        if tag not in VOID:
            self.stack.append(tag)

    def handle_data(self, data):
        if self.title_open:
            self.title += data
        if self.active is not None:
            self.active[1] += data

    def handle_endtag(self, tag):
        if tag in VOID:
            self.errors.append(f"Unexpected closing void tag: {tag}")
            return
        if not self.stack or self.stack[-1] != tag:
            self.errors.append(f"Incorrect closing tag </{tag}>, stack={self.stack}")
            return
        self.stack.pop()
        if tag in CONTENT:
            if self.active is None or self.active[0] != tag:
                self.errors.append(f"Mismatched content tag: {tag}")
            else:
                self.elements.append((tag, " ".join(self.active[1].split())))
                self.active = None
        if tag == "title":
            self.title_open = False


class CamperbotProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = HTML_FILE.read_text(encoding="utf-8")
        cls.parser = StrictProfileParser()
        cls.parser.feed(cls.source)
        cls.parser.close()

    def test_01_html5_structure(self):
        self.assertTrue(self.parser.doctype)
        self.assertEqual(self.parser.lang, "en")
        for tag in ("html", "head", "body"):
            self.assertEqual(self.parser.tags.count(tag), 1)

    def test_02_document_metadata(self):
        self.assertEqual(self.parser.charset.lower(), "utf-8")
        self.assertIn("width=device-width", self.parser.viewport)
        self.assertTrue(self.parser.title.strip())

    def test_03_balanced_tags(self):
        self.assertEqual(self.parser.errors, [])
        self.assertEqual(self.parser.stack, [])
        self.assertIsNone(self.parser.active)

    def test_04_exact_text_and_order(self):
        self.assertEqual(self.parser.elements, EXPECTED)

    def test_05_heading_hierarchy(self):
        self.assertEqual([tag for tag, _ in self.parser.elements if tag.startswith("h")], ["h1", "h2", "h3"])

    def test_06_exactly_two_paragraphs(self):
        self.assertEqual(sum(tag == "p" for tag, _ in self.parser.elements), 2)

    def test_07_original_invalid_tags_absent(self):
        self.assertFalse({"heading2", "pp"} & set(self.parser.tags))
        self.assertEqual([tag for tag in self.parser.tags if tag in CONTENT], [tag for tag, _ in EXPECTED])

    def test_08_no_custom_css_javascript(self):
        self.assertFalse({"style", "script", "link"} & set(self.parser.tags))
        self.assertIsNone(re.search(r"\son[a-z]+\s*=", self.source, re.IGNORECASE))


if __name__ == "__main__":
    unittest.main(verbosity=2)
