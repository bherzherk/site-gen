import re

from enum import Enum
from typing import Text


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str):
    if re.findall(r"^#{1,6}\s+.+$", block):
        return BlockType.HEADING
    if re.findall(r"^```(?:\w+)?\n[\s\S]*?\n```$", block):
        return BlockType.CODE
    if re.findall(r"(^>\s?.+\n?)+", block):
        return BlockType.QUOTE
    if re.findall(r"^(?:\s*[-+*]\s+.+\n)*\s*[-+*]\s+.+$", block):
        return BlockType.UNORDERED_LIST
    if re.findall(r"^(?:\s*\d+\.\s+.+\n)*\s*\d+\.\s+.+$", block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown: str):
    split_markdown = markdown.strip().split("\n\n")
    blocks = [b for b in split_markdown if b.strip() != ""]
    return blocks
