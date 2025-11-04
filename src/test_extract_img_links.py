from extract_img_links import extract_markdown_images, extract_markdown_links
import unittest


class TestExtractImgLink(unittest.TestCase):
    def test_img_markdown(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            extract_markdown_images(text),
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )

    def test_img_mk_error(self):
        text = "This is a text with ![Rick and Morty](http://test.com(text.com)) image of my fav series"
        with self.assertRaises(ValueError):
            extract_markdown_images(text)

    def test_img_mk_incomplete(self):
        text = "This is a text with ![my image](http://test.com : test it!"
        with self.assertRaises(ValueError):
            extract_markdown_images(text)

    def test_img_mk_noimg(self):
        text = "Is this and image: [my image](http:image.com)?"
        with self.assertRaises(ValueError):
            extract_markdown_images(text)

    def test_link_markdown(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(
            extract_markdown_links(text),
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
        )

    def test_link_mk_error(self):
        text = "This is a link: [[link](http://test(url))"
        with self.assertRaises(ValueError):
            extract_markdown_links(text)

    def test_incomplete_link(self):
        text = "click on [this](http://test.com and you will see..."
        with self.assertRaises(ValueError):
            extract_markdown_links(text)

    def test_no_link(self):
        text = "Check this site ![my site](https://url.com)"
        with self.assertRaises(ValueError):
            extract_markdown_links(text)
