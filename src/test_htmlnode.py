import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)
        node3 = HTMLNode("h1")
        node4 = HTMLNode("h1")
        self.assertEqual(node3, node4)
        node5 = HTMLNode(
            "p", 
            None, 
            ["test", "test2"], 
            {"test1": "test2", "test3": "test4"}
        )
        node6 = HTMLNode(
            tag="p", 
            props={"test1": "test2", "test3": "test4"}, 
            children=["test", "test2"]
        )
        self.assertEqual(node5, node6)
        node7 = HTMLNode(props={"test1": "test2", "test3": "test4"})
        node8 = HTMLNode(props={"test3": "test4", "test1": "test2"})
        self.assertEqual(node7, node8)
    
    def test_props_to_html(self):
        node9 = HTMLNode(props={"test1": "test2", "test3": "test4"})
        expected_text = ' test1="test2" test3="test4"'
        self.assertEqual(node9.props_to_html(), expected_text)
        node10 = HTMLNode()
        self.assertEqual(node10.props_to_html(), None)


if __name__ == "__main__":
    unittest.main()