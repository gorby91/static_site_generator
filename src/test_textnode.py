import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node3 = TextNode("This is also a text node", TextType.LINK, "www.google.com")
        node4 = TextNode("This is also a text node", TextType.LINK, "www.google.com")
        self.assertEqual(node3, node4)
        node5 = TextNode("", TextType.NORMAL, None)
        node6 = TextNode("", TextType.NORMAL)
        self.assertEqual(node5, node6)
    def test_empty_url(self):
        node7 = TextNode("This is a not equal test", TextType.CODE, "")
        node8 = TextNode("This is a not equal test", TextType.CODE)
        self.assertNotEqual(node7, node8)
    def test_different_types(self):
        node9 = TextNode("Testing different texttypes", TextType.BOLD)
        node10 = TextNode("Testing different texttypes", TextType.IMAGE)
        self.assertNotEqual(node9, node10)
    def test_different_urls(self):
        node11 = TextNode("Testing different urls", TextType.NORMAL, "https://www.google.com.au/")
        node12 = TextNode("Testing different urls", TextType.NORMAL, "http://www.google.com.au/")

if __name__ == "__main__":
    unittest.main()