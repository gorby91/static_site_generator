def markdown_to_blocks(markdown: str) -> list:
    # split blocks by double newline, remove any empty blocks with filter
    blocks = filter(len, markdown.split("\n\n"))
    # return a list of blocks stripped of extra whitespace and newlines
    return list(map(lambda block: block.strip(), blocks))