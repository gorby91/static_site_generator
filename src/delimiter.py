from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: TextType) -> list:
    new_nodes = []
    for node in old_nodes:
        if node.text.count(delimiter) == 0:
            new_nodes.append(node)
        elif delimiter == "*" and node.text.count("**") > 0:
            raise Exception("Split by bold before splitting by italic")
        elif node.text.count(delimiter) % 2 == 1:
            raise Exception("Invalid markdown syntax")
        else:
            # separate strings by delimiter
            strings = node.text.split(delimiter)
            # apportion alternating split strings, discarding empty values
            for i, string in enumerate(strings):
                if i % 2 == 0 and len(string) > 0:
                    new_nodes.append(TextNode(string, node.text_type))
                elif len(string) > 0:                    
                    new_nodes.append(TextNode(string, text_type))             
    return new_nodes
