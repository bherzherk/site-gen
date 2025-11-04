from textnode import TextNode, TextType
from extract_img_links import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(
    old_nodes: list["TextNode"], delimiter: str, text_type: TextType
):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        parts = old_node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Invalid format, in markdown: section not closed")
        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(parts[i], text_type))

        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_image(old_nodes: list["TextNode"]):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        images_mk = extract_markdown_images(text)
        if len(images_mk) == 0:
            new_nodes.append(old_node)
            continue

        for image_mk in images_mk:
            # dividing original text, using as delimiter the img_mk
            text_part = text.split(f"![{image_mk[0]}]({image_mk[1]})", 1)
            if len(text_part) != 2:
                raise ValueError("Invalid Markdown Format: image not closed!")
            if text_part[0] != "":
                new_nodes.append(TextNode(text_part[0], TextType.TEXT))

            # building the node for image
            new_nodes.append(
                TextNode(
                    image_mk[0],
                    TextType.IMAGE,
                    image_mk[1],
                )
            )

            text = text_part[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes: list["TextNode"]):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        links_mk = extract_markdown_links(text)
        if len(links_mk) == 0:
            new_nodes.append(old_node)
            continue

        for link_mk in links_mk:
            # dividing text when link is found
            text_parts = text.split(f"[{link_mk[0]}]({link_mk[1]})", 1)
            if len(text_parts) != 2:
                raise ValueError("Invalid Markdown Format: Link not closed!")
            if text_parts[0] != "":
                new_nodes.append(TextNode(text_parts[0], TextType.TEXT))

            # building the node for link
            new_nodes.append(
                TextNode(
                    link_mk[0],
                    TextType.LINK,
                    link_mk[1],
                )
            )

            text = text_parts[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes
