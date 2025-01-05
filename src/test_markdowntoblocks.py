import unittest
from markdowntoblocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_lesson_example(self):
        self.assertEqual(markdown_to_blocks(test1), result1)
    def test_extra_lines(self):
        self.assertEqual(markdown_to_blocks(test1_1), result1)
    def test_extra_whitespace(self):
        self.assertEqual(markdown_to_blocks(test1_2), result1)




test1 = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

result1 = [
    "# This is a heading",
    "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
    """* This is the first list item in a list block
* This is a list item
* This is another list item""",
]

test1_1 = """# This is a heading






This is a paragraph of text. It has some **bold** and *italic* words inside of it.




* This is the first list item in a list block
* This is a list item
* This is another list item"""

test1_2 = """        # This is a heading






     This is a paragraph of text. It has some **bold** and *italic* words inside of it.          




   * This is the first list item in a list block
* This is a list item
* This is another list item                """