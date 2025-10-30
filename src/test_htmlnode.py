import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_all_is_none(self):
        node = HTMLNode()
        for attr, value in vars(node).items():
            with self.subTest(attr=attr):
                self.assertIsNone(value, f"{attr} should be None")

    def test_prop_format(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(tag="a", props=props)
        result = node.props_to_html()
        expected = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(result, expected)

    def test_raise_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            'class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, None, {'class': 'primary'})",
        )

    ## Leaf node tests-----------------------------------------------------------------------------
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_no_value(self):
        node = LeafNode("a", value=None)
        with self.assertRaises(ValueError) as context:
            node.to_html()

        self.assertEquals(str(context.exception), "All leaf nodes must have a value")

    def test_raw_value(self):
        node = LeafNode(tag=None, value="This is a raw")
        self.assertEqual(node.to_html(), "This is a raw")


if __name__ == "__main__":
    unittest.main()
