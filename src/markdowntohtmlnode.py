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
        block_parent = ParentNode(tag=blocktag, children=block_children)
        full_nodelist.append(block_parent)
    return ParentNode(tag="div", children=full_nodelist)


def format_htmlblock(blocktype: str, block:str) -> tuple:
    if blocktype == "heading":
        return format_heading_block(block)
    if blocktype == "code":
        return format_code_block(block)
    lines = block.splitlines()
    if blocktype == "quote":
        return format_quote_block(lines)
    if blocktype == "unordered_list":
        return format_unordered_list_block(lines)
    if blocktype == "ordered_list":
        return format_ordered_list_block(lines)    
    else:
        return "p", block
    
def format_heading_block(block):
    content = re.search(r"^(\#{1,6}) (.*)$", block)
    head_tag = f"h{len(content.group(1))}"
    return head_tag, content.group(2)

def format_code_block(block):
    return "code", block[3:-3]

def format_quote_block(lines):
    extracted_quote = "\n".join(map(lambda line: line[1:].lstrip(), lines))
    return "blockquote", extracted_quote

def format_unordered_list_block(lines):
    labelled_list = "".join(map(lambda line: f"<li>{line[2:]}</li>", lines))
    return "ul", labelled_list

def format_ordered_list_block(lines):
    return_list = []
    for i, line in enumerate(lines):
        content = re.search(r"^\d*\. (.*)$", line) 
        return_list.append(f"<li>{content.group(1)}</li>")
    return "ol", "".join(return_list)
