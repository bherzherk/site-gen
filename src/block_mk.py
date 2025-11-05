def markdown_to_blocks(markdown):
    split_markdown = markdown.strip().split("\n\n")
    blocks = [b for b in split_markdown if b.strip() != ""]
    return blocks
