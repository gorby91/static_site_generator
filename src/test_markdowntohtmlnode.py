import unittest

from markdowntohtmlnode import *


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_format_heading(self):
        self.assertEqual(format_heading_block(test1), result1)
        self.assertEqual(format_heading_block(test2), result2)
        with self.assertRaises(AttributeError):
            format_heading_block(test3)
        with self.assertRaises(AttributeError):
            format_heading_block(test4)
    def test_format_code_block(self):
        self.assertEqual(format_code_block(test5), result5)
        self.assertEqual(format_code_block(test6), result6)
    def test_format_ordered_list(self):
        self.assertEqual(format_ordered_list_block(test7), result7)
    def test__format_unordered_list(self):
        self.assertEqual(format_unordered_list_block(test8), result8)
    def test_format_quote(self):
        self.assertEqual(format_quote_block(test9), result9)
    def test_format_paragraph(self):
        self.assertEqual(format_htmlblock(None, test3), result_para1)
        self.assertEqual(format_htmlblock(None, test4), result_para2)
    def test_all_together(self):
        self.assertEqual(markdown_to_html_node(test10).to_html(), result10)
        self.assertEqual(markdown_to_html_node(test11).to_html(), result11)
    








test1 = "# This is h1"
result1 = ("h1", "This is h1")
test2 = "###### This is h6"
result2 = ("h6", "This is h6")
test3 = "####### h7 doesn't exist"
result_para1 = ("p", "####### h7 doesn't exist")
test4 = "#you need space between the hash and the heading"
result_para2 = ("p", "#you need space between the hash and the heading")
test5 = "```This is a code block```"
result5 = ("code", "This is a code block")
test6 = """```
as is this here
as well
```"""
result6 = ("code", "\nas is this here\nas well\n")
test7 = """1. This
2. is
3. an
4. ordered
5. list""".splitlines()
result7 = ("ol", "<li>This</li><li>is</li><li>an</li><li>ordered</li><li>list</li>")
test8 = """* This
* is
* an
* unordered
* list""".splitlines()
result8 = ("ul", "<li>This</li><li>is</li><li>an</li><li>unordered</li><li>list</li>")
test9 = """>This
>is
>a
>blockquote""".splitlines()
result9 = ("blockquote", "This\nis\na\nblockquote")


test10 = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
result10 = "<div><h1>This is a heading</h1><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul></div>"
test11 = """This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)

This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"""
result11 = '<div><p>This is text with a <img src="https://i.imgur.com/aKaOqIh.gif" alt="rick roll"></img> and <img src="https://i.imgur.com/fJRm4Vk.jpeg" alt="obi wan"></img></p><p>This is text with a link <a href="https://www.boot.dev">to boot dev</a> and <a href="https://www.youtube.com/@bootdotdev">to youtube</a></p></div>'


if __name__ == "__main__":
    unittest.main()