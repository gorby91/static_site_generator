import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(None, "test")
        node1 = LeafNode(tag=None,  value="test")
        self.assertEqual(node, node1)
        node2 = LeafNode(
            "p", 
            "test2", 
            {"test1": "test2", "test3": "test4"}
        )
        node3 = LeafNode(
            tag="p", 
            value="test2", 
            props={"test3": "test4", "test1": "test2"}
        )
        self.assertEqual(node2, node3)

    def test_to_html(self):
        node4 = LeafNode(tag="p", value="test3")
        test4_string = "<p>test3</p>"
        self.assertEqual(node4.to_html(), test4_string)
        node5 = LeafNode("a", "Click me!", props={"href": "https://google.com"})
        test5_string = '<a href="https://google.com">Click me!</a>'
        self.assertEqual(node5.to_html(), test5_string)
        node6 = LeafNode(None, "test6")
        self.assertEqual(node6.to_html(), "test6")

if __name__ == "__main__":
    unittest.main()