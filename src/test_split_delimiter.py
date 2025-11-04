import unittest
from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitDelimiter(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is **bold** text.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_double_italic(self):
        node = TextNode(
            "This is a text with _italic_ and it is _important_ to test.", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is a text with ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and it is ", TextType.TEXT),
                TextNode("important", TextType.ITALIC),
                TextNode(" to test.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_empty_section(self):
        node = TextNode("This text ``contain`` empty section.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This text ", TextType.TEXT),
                TextNode("contain", TextType.TEXT),
                TextNode(" empty section.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_incomplete_section(self):
        node = TextNode("This text is **imcomplete bold.", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_multiple_nodes(self):
        node_1 = TextNode("This is the code: `print('hi')`", TextType.TEXT)
        node_2 = TextNode("This is the output: `hi`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node_1, node_2], "`", TextType.CODE)

        self.assertListEqual(
            [
                TextNode("This is the code: ", TextType.TEXT),
                TextNode("print('hi')", TextType.CODE),
                TextNode("This is the output: ", TextType.TEXT),
                TextNode("hi", TextType.CODE),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
