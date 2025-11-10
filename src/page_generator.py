# import os
import re
from pathlib import Path

from markdown_to_html import markdown_to_html_node


def extract_title(markdown):
    if re.findall(r"^#\s+(.*)", markdown):
        title = markdown.strip("#").strip()
        return title

    raise ValueError("No h1 header detected!")


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # Read markdown file
    markdown = from_path.read_text()

    # Read template file
    template = Path(template_path).read_text()

    # Convert markdown to HTML
    node = markdown_to_html_node(markdown)
    html = node.to_html()

    # Extract title
    title = extract_title(markdown)

    # Replace placeholders
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace("href='/", "href='" + basepath)
    template = template.replace("src='/", "src='" + basepath)

    # Build destination file path (same name, but .html extension)
    dest_file = dest_path / (from_path.stem + ".html")

    # Ensure destination directory exists
    dest_path.mkdir(parents=True, exist_ok=True)

    # Write output
    dest_file.write_text(template)
