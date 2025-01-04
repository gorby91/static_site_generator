def markdown_to_blocks(markdown: str) -> list:
    # split blocks by double newline, remove any empty blocks with filter
    blocks = filter(len, markdown.split("\n\n"))
    return list(map(lambda x: x.strip, blocks))