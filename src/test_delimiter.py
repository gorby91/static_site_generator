import unittest
from delimiter import split_nodes_delimiter
from textnode import TextType, TextNode

class TestDelimiter(unittest.TestCase):
    def test_raises(self):
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node1], "*", TextType.ITALIC)
    def test_no_split(self):
        self.assertEqual(split_nodes_delimiter(result2, "**", TextType.BOLD), result2)
    def test_code(self):
        self.assertEqual(split_nodes_delimiter([node2], "`", TextType.CODE), result2)
    def test_bold(self):
        self.assertEqual(split_nodes_delimiter([node1], "**", TextType.BOLD), result1)
    def test_italic(self):
        self.assertEqual(split_nodes_delimiter([node3], "*", TextType.ITALIC), result3)
        self.assertEqual(split_nodes_delimiter(result1, "*", TextType.ITALIC), result1_1)
    def test_start(self):
        self.assertEqual(split_nodes_delimiter([node4], "`", TextType.CODE), result4)
    def test_end(self):
        self.assertEqual(split_nodes_delimiter([node5], "**", TextType.BOLD), result5)



node = TextNode("This is an **invalid markup * string", TextType.TEXT)
node1 = TextNode("This is a string with **bold** and *italic*", TextType.TEXT)
result1 = [
    TextNode("This is a string with ", TextType.TEXT),
    TextNode("bold", TextType.BOLD),
    TextNode(" and *italic*", TextType.TEXT),
]
result1_1 = [
    TextNode("This is a string with ", TextType.TEXT),
    TextNode("bold", TextType.BOLD),
    TextNode(" and ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
]
node2 = TextNode("This is text with a `code block` word", TextType.TEXT)
result2 = [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
]
node3 = TextNode("This is a test with *italic* text", TextType.TEXT)
result3 = [
    TextNode("This is a test with ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" text", TextType.TEXT),
]
node4 = TextNode("`Code` appears at the start of this test", TextType.TEXT)
result4 = [
    TextNode("Code", TextType.CODE),
    TextNode(" appears at the start of this test", TextType.TEXT),
]
node5 = TextNode("This text ends with a **bold statement**", TextType.TEXT)
result5 = [
    TextNode("This text ends with a ", TextType.TEXT),
    TextNode("bold statement", TextType.BOLD)

]

if __name__ == "__main__":
    unittest.main()