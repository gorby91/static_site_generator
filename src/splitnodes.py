from extract import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType
import re

def split_nodes_image(old_nodes):
    new_nodes = []
    pattern = r"!\[[^\[\]]*\]\([^\(\)]*\)"
    for node in old_nodes:
        matches = extract_markdown_images(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
        else:
            strings = re.split(pattern, node.text)
            for i, string in enumerate(strings):
                if len(string) > 0:
                    new_nodes.append(TextNode(string, node.text_type))
                if i < len(matches):
                    new_nodes.append(TextNode(matches[i][0], TextType.IMAGE, url=matches[i][1]))
    return new_nodes
            

def split_nodes_link(old_nodes):
    new_nodes = []
    pattern = r"(?<!!)\[[^\[\]]*\]\([^\(\)]*\)"
    for node in old_nodes:
        matches = extract_markdown_links(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
        else:
            strings = re.split(pattern, node.text)
            for i, string in enumerate(strings):
                if len(string) > 0:
                    new_nodes.append(TextNode(string, node.text_type))
                if i < len(matches):
                    new_nodes.append(TextNode(matches[i][0], TextType.LINK, url=matches[i][1]))
    return new_nodes