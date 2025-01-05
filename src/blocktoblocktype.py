import re

from markdowntoblocks import markdown_to_blocks

def block_to_block_type(block: str) -> str:
    if check_header(block):
        return "head"
    if check_code(block):
        return "code"
    # divide lines for following tests to be performed 
    lines = block.splitlines()
    if check_blockquote(lines):
        return "blockquote"
    if check_unordered_list(lines):
        return "ul"
    if check_ordered_list(lines):
        return "ol"
    else:
        return "body"
    

def check_header(block: str) -> bool:
    # define a search pattern looking for hashes and match header type
    if re.search(r"^#{1,6} ", block):
        return "True"
    return False

def check_code(block: str) -> bool:
    # check start and end for triple backticks to test if code block
    return block[:3] == "```" and block[-3:] == "```"

def check_blockquote(lines: list) -> bool:
    # check each line commences with ">" for quoteblock by checking no false values with filter
    return len(lines) == len(
        list(
            filter(
                lambda line: line.startswith(">"), lines
            )
        )
    )

def check_unordered_list(lines: list) -> bool:
    # check each line commences with "* " or "- " for quoteblock by checking no false values with filter
    return len(lines) == len(
        list(
            filter(
                lambda line: line.startswith("* ") or line.startswith("- "), lines
            )
        )
    )

def check_ordered_list(lines: list) -> bool:
     # check if ordered list by looping over lines to check if each line starts with an incrementing value
    for i, line in enumerate(lines):
        start_true = line.startswith(f"{i + 1}. ")
        if not start_true:
            break
    return start_true