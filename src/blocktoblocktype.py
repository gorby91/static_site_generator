import re

from markdowntoblocks import markdown_to_blocks

def block_to_block_type(block: str) -> str:
    # define a search pattern looking for hashes and match header type to number of hashes returned
    header_pattern = r"^(#{1,6}) "
    header_match = re.search(header_pattern, block)
    if header_match:
        return "head"
    # check start and end for triple backticks to test if code block
    elif block[:3] == "```" and block[-3:] == "```":
        return "code"
    # divide lines for following tests to be performed 
    lines = block.splitlines()
    # check each line commences with ">" for quoteblock by checking no false values with filter
    if len(lines) == len(filter(lambda line: line.startswith(">"), lines)):
        return "blockquote"
    # check each line commences with "* " or "- " for quoteblock by checking no false values with filter
    elif len(lines) == len(filter(lambda line: line.startswith("* ") or line.startswith("- "), lines)):
        return "ul"
    # check if ordered list by looping over lines to check if each line starts with an incrementing value
    for i, line in enumerate(lines):
        startvalue = f"{i + 1}."
        if not line.startswith(startvalue):
            continue
        return "ol"
    else:
        return "body"
    


test = "#### testing"
print(block_to_block_type(test))