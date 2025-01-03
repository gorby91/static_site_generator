import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        self.assertEqual(node.to_html(), test1_string)
        self.assertEqual(node2.to_html(), test2_string)
    def test_no_children(self):
        with self.assertRaises(ValueError):
            node3.to_html()
    def test_no_tag(self):
        with self.assertRaises(ValueError):
            node4.to_html()


node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

test1_string = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"

node2 = ParentNode(
    "html",
    [
         ParentNode("head", [LeafNode("title", "Sample Web Page")]),
         ParentNode(
              "body",
              [
                   LeafNode("h1", "Welcome to HTML"),
                   LeafNode("p", "This is a sample paragraph."),
                   LeafNode("a", "Visit Example", {"href": "https://www.example.com"}),
              ]
         )
    ])

test2_string = '<html><head><title>Sample Web Page</title></head><body><h1>Welcome to HTML</h1><p>This is a sample paragraph.</p><a href="https://www.example.com">Visit Example</a></body></html>'

node3 = ParentNode("p", [])
node4 = ParentNode(None, [LeafNode(None, "This is test 4")])

if __name__ == "__main__":
    unittest.main()