import re


def extract_markdown_images(text: str):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    if matches:
        return matches
    raise ValueError("Image in markdown not found!")


def extract_markdown_links(text: str):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    if matches:
        return matches
    raise ValueError("Link in markdown not found!")
