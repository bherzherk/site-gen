import os
import shutil
import sys

from pages_generator import generate_pages_recursive
from textnode import TextNode, TextType


def main():
    source = "./static"
    destination = "./docs"
    basepath = "/"
    copy_content_to_dir(source, destination)
    base_path = os.path.dirname(__file__)
    source_path = os.path.join(base_path, "..", "content")
    destination_path = os.path.join(base_path, "..", "docs")
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    generate_pages_recursive(source_path, "template.html", destination_path, basepath)


def copy_content_to_dir(source: str, destination: str):
    delete_folder_content(destination)
    copy_content(source, destination)


def delete_folder_content(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
        else:
            shutil.rmtree(file_path)


def copy_content(source, destination):
    items = os.listdir(source)
    for item in items:
        source_path = os.path.join(source, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, os.path.join(destination, item))
        else:
            destination_path = os.path.join(destination, item)
            os.mkdir(destination_path)
            copy_content(source_path, destination_path)


if __name__ == "__main__":
    main()
