import unittest
from leafnode import LeafNode
from textnode import TextNode, text_node_to_html_node

class TestTextNodetoHTMLNode(unittest.TestCase):
    def test_bold(self):
        self.assertEqual(text1_node, leaf1_node)
    def test_normal(self):
        self.assertEqual(text2_node, leaf2_node)
    def test_italic(self):
        self.assertEqual(text3_node, leaf3_node)
    def test_code(self):
        self.assertEqual(text4_node, leaf4_node)
    def test_link(self):
        self.assertEqual(text5_node, text6_node)
    def test_link(self):
        self.assertEqual(text6_node, leaf6_node)
    def test_raises(self):
        with self.assertRaises(Exception):
            text_node_to_html_node(TextNode("This is a link", "links", url="google.images.com"))
    
    


text1_node = text_node_to_html_node(TextNode("This is bold text", "bold"))
leaf1_node = LeafNode("b", "This is bold text")
text2_node = text_node_to_html_node(TextNode("This is just text", "text"))
leaf2_node = LeafNode(None, value="This is just text")
text3_node = text_node_to_html_node(TextNode("This is italicised text", "italic"))
leaf3_node = LeafNode("i", "This is italicised text")
text4_node = text_node_to_html_node(TextNode("This is a code block", "code"))
leaf4_node = LeafNode("code", "This is a code block")
text5_node = text_node_to_html_node(TextNode("This is a link", "link", url="google.images.com"))
leaf5_node = LeafNode("a", "This is a link", {"href": "google.images.com"})
text6_node = text_node_to_html_node(TextNode("This is an image", "image", url="google.images.com"))
leaf6_node = LeafNode("img", "", {"src": "google.images.com", "alt": "This is an image"})                            






if __name__ == "__main__":
    unittest.main()