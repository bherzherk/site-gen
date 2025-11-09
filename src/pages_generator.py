from pathlib import Path

from page_generator import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_path_content = Path(dir_path_content)
    template_path = Path(template_path)
    dest_dir_path = Path(dest_dir_path)

    # Ensure destination directory exists
    dest_dir_path.mkdir(parents=True, exist_ok=True)

    for item in dir_path_content.iterdir():
        if item.is_file():
            if item.suffix == ".md":
                generate_page(item, template_path, dest_dir_path)
        elif item.is_dir():
            child_source = item
            child_dest = dest_dir_path / item.name
            generate_pages_recursive(child_source, template_path, child_dest)
