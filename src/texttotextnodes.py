from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter
from splitnodes import split_nodes_image, split_nodes_link

def text_to_textnodes(text: str) -> list:
    input_node = TextNode(text, TextType.TEXT)
    convert_bold = split_nodes_delimiter([input_node], "**", TextType.BOLD)
    convert_italic = split_nodes_delimiter(convert_bold, "*", TextType.ITALIC)
    convert_code = split_nodes_delimiter(convert_italic, "`", TextType.CODE)
    return split_nodes_image(split_nodes_link(convert_code))