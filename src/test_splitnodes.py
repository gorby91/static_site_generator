import unittest
from textnode import TextNode, TextType
from splitnodes import split_nodes_image, split_nodes_link


class TestSplitNodes(unittest.TestCase):
    def test_split_links(self):
        self.assertEqual(split_nodes_link([node2]), result2)
    def test_split_images(self):
        self.assertEqual(split_nodes_image([node1]), result1)
    def test_stacked(self):
        self.assertEqual(split_nodes_image(split_nodes_link([node3])), result3)
    def test_no_image_or_link(self):
        self.assertEqual(split_nodes_image(split_nodes_link([node4])), [node4])

test1 = "![rick roll](https://i.imgur.com/aKaOqIh.gif) is at the start and at the end is ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
node1 = TextNode(test1, TextType.TEXT)
result1 = [
    TextNode("rick roll", TextType.IMAGE, url="https://i.imgur.com/aKaOqIh.gif"),
    TextNode(" is at the start and at the end is ", TextType.TEXT),
    TextNode("obi wan", TextType.IMAGE, url="https://i.imgur.com/fJRm4Vk.jpeg")
]


test2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
node2 = TextNode(test2, TextType.TEXT)
result2 = [
    TextNode("This is text with a link ", TextType.TEXT),
    TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
    TextNode(" and ", TextType.TEXT),
    TextNode(
        "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
    ),
]

test3 = "This is text with a link [to boot dev](https://www.boot.dev) and an image ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
node3 = TextNode(test3, TextType.TEXT)
result3 = [
    TextNode("This is text with a link ", TextType.TEXT),
    TextNode("to boot dev", TextType.LINK, url="https://www.boot.dev"),
    TextNode(" and an image ", TextType.TEXT),
    TextNode("obi wan", TextType.IMAGE, url="https://i.imgur.com/fJRm4Vk.jpeg")
]

test4 = "And this is just plain old text ![with something to throw off] (the computer)"
node4 = TextNode(test4, TextType.TEXT)

if __name__ == "__main__":
    unittest.main()