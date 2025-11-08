import os
import re

from markdown_to_html import markdown_to_html_node


def extract_title(markdown):
    if re.findall(r"^#\s+().*", markdown):
        title = markdown.strip("#").strip()
        return title

    raise ValueError("No h1 header detected!")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    source = os.path.dirname(__file__)
    from_path = os.path.join(source, from_path)
    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    node = markdown_to_html_node(markdown)
    html = node.to_html()

    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    with open(dest_path, "w") as f:
        f.write(template)
