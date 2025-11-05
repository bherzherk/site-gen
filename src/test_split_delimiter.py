import unittest
from inline_mk import split_nodes_delimiter, split_nodes_image, split_nodes_link
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

    # Test Split image------------------------------------------------------------------------------------------
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    #    def test_split_img_error(self):
    #        node = TextNode(
    #            "This is an image: ![image](http://i.image.com to test raise error.",
    #            TextType.TEXT,
    #        )
    #        with self.assertRaises(ValueError):
    #            split_nodes_image([node])

    def test_split_img_single(self):
        node = TextNode("![image](http://img.com)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "http://img.com"),
            ],
            new_nodes,
        )

    # Test Split link------------------------------------------------------------------------------------------

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.TEXT),
            ],
            new_nodes,
        )

    #    def test_split_link_error(self):
    #        node = TextNode(
    #            "This is a text with link: [link](http://test.test this is a format error.",
    #            TextType.TEXT,
    #        )
    #        with self.assertRaises(ValueError):
    #            split_nodes_link([node])

    def test_split_link_single(self):
        node = TextNode("[link](http://link.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [TextNode("link", TextType.LINK, "http://link.com")],
            new_nodes,
        )


# Test text to nodes----------------------------------------------------------------------------


if __name__ == "__main__":
    unittest.main()
