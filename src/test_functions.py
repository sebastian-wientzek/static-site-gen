import unittest
from textnode import *
from functions import *

class TestFunctions(unittest.TestCase):
    def _string_setup(self):
        return """This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg). This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)."""


    def test_split_nodes_delimiter_simple(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        comp_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, comp_nodes)

    def test_split_nodes_delimiter_complex(self):
        old_nodes = [
            TextNode("Text with **bold** elements, for **testing**.", TextType.TEXT), 
            TextNode("a code block", TextType.CODE),
            TextNode("some *italic* elements.", TextType.TEXT)
            ]
        comp_nodes = [
            TextNode("Text with ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" elements, for ", TextType.TEXT),
            TextNode("testing", TextType.BOLD),
            TextNode(".", TextType.TEXT),
            TextNode("a code block", TextType.CODE),
            TextNode("some *italic* elements.", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(comp_nodes, new_nodes)

    def test_extract_markdown_links_basic(self):
        text = self._string_setup()
        test_comparison = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
        test_result = extract_markdown_links(text)
        self.assertEqual(test_comparison, test_result)

    def test_extract_markdown_images_basic(self):
        text = self._string_setup()
        test_comparison = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        test_result = extract_markdown_images(text)
        self.assertEqual(test_comparison, test_result)

    def test_extraction_markdown_links_none(self):
        text = None
        with self.assertRaises(TypeError) as context:
            extract_markdown_links(text)
        self.assertEqual(str(context.exception), "wrong type, expected <class 'str'>, but got <class 'NoneType'>")

    def test_extraction_markdown_images_none(self):
        text = None
        with self.assertRaises(TypeError) as context:
            extract_markdown_images(text)
        self.assertEqual(str(context.exception), "wrong type, expected <class 'str'>, but got <class 'NoneType'>")

    def test_extraction_markdown_empty_string(self):
        text = ""
        test_comparison = []
        test_result_links = extract_markdown_links(text)
        test_result_images = extract_markdown_images(text)
        self.assertEqual(test_comparison, test_result_links)
        self.assertEqual(test_comparison, test_result_images)

    def test_split_nodes_image_mixed(self):
        node = TextNode(self._string_setup(), TextType.TEXT)
        test_result = split_nodes_image([node])
        test_comparison = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(". This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev).", TextType.TEXT)
        ]
        self.assertEqual(test_comparison, test_result)

    def test_split_nodes_links_mixed(self):
        node = TextNode(self._string_setup(), TextType.TEXT)
        test_result = split_nodes_link([node])
        test_comparison = [
            TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg). This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(test_comparison, test_result)

    def test_split_nodes_image_empty(self):
        test_result = split_nodes_image([])
        test_comparison = []
        self.assertEqual(test_comparison, test_result)

    def test_split_nodes_links_empty(self):
        test_result = split_nodes_link([])
        test_comparison = []
        self.assertEqual(test_comparison, test_result)

    def test_split_nodes_image_none(self):
        with self.assertRaises(TypeError) as context:
            split_nodes_image(None)
        self.assertEqual(str(context.exception), "wrong type, expected <class 'list'>, but got <class 'NoneType'>")

    def test_split_nodes_link_none(self):
        with self.assertRaises(TypeError) as context:
            split_nodes_link(None)
        self.assertEqual(str(context.exception), "wrong type, expected <class 'list'>, but got <class 'NoneType'>")

if __name__ == "__main__":
    unittest.main()