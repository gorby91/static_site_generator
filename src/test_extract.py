import unittest
from extract import extract_markdown_images, extract_markdown_links

class TestExtract(unittest.TestCase):
    def test_multi_images(self):
        self.assertEqual(extract_markdown_images(test1), result1)
    def test_multi_links(self):
        self.assertEqual(extract_markdown_links(test2), result2)
    def test_images_with_links_function(self):
        self.assertEqual(extract_markdown_links(test1), [])
    def test_links_with_images_function(self):
        self.assertEqual(extract_markdown_images(test2), [])
    def test_only_alt_text(self):
        self.assertEqual(extract_markdown_images(test3), [])
        self.assertEqual(extract_markdown_links(test4), [])
    def test_nonstandard_format(self):
        self.assertEqual(extract_markdown_images(test5), [])





test1 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
result1 = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

test2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
result2 = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

test3 = "This is text with a ![rick roll] and ![obi wan]"
test4 = "This is text with a link [to boot dev] and [to youtube]"

test5 = "This is text with a ![rick roll] (https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg"


if __name__ == "__main__":
    unittest.main()