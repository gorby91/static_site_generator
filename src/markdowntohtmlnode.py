import re

from htmlnode import HTMLNode
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from markdowntoblocks import markdown_to_blocks
from blocktoblocktype import block_to_block_type
from texttotextnodes import text_to_textnodes


def markdown_to_html_node(markdown: str) -> ParentNode:
    blocklist = markdown_to_blocks(markdown)
    full_nodelist = []
    for block in blocklist:
        # get block type from the markdown block
        blocktype = block_to_block_type(block)
        # reformat from a markdown block to a html block
        blocktag, block_content = format_htmlblock(blocktype, block)
        # create a list of textnodes to deal with inline markdown syntax
        block_textnodes = text_to_textnodes(block_content)
        # convert list of textnodes to html nodes
        block_children = list(map(text_node_to_html_node, block_textnodes))
        # create a parent node for the block
        block_parent = ParentNode(tag=blocktype, children=block_children)
        full_nodelist.append(ParentNode)
    parent = ParentNode(tag="div", children=full_nodelist)


def format_htmlblock(blocktype: str, block:str) -> tuple:
    if blocktype is "heading":
        content = re.search(r"^\#{1,6} (.*)$")
        return "head", content.group(1)
    if blocktype is "code":
        return "code", block[3:-3]
    lines = block.splitlines()
    if blocktype is "quote":
        extracted_quote = "\n".join(map(lambda line: line[1:], lines))
        return "blockquote", extracted_quote
    if blocktype is "unordered_list":
        labelled_list = "\n".join(map(lambda line: line[2:], lines))
        return "ul", labelled_list
    if blocktype is "ordered_list":
        content = re.search(r"^\d*\. (.*)$") 
        return_list = []
        for i, line in enumerate(content):
            return_list.append(f"<li>{content.group(i+1)}</li>")
            return "ol", "\n".join(return_list)
    else:
        return "p", block