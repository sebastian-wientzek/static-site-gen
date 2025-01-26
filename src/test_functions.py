import unittest
from textnode import *
from functions import *

class TestFunctions(unittest.TestCase):
    def _string_setup(self):
        return """
        This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) 
        This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)
        """


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
        self.assertEqual(str(context.exception), "wrong type, expected string, but got <class 'NoneType'>")

    def test_extraction_markdown_images_none(self):
        text = None
        with self.assertRaises(TypeError) as context:
            extract_markdown_images(text)
        self.assertEqual(str(context.exception), "wrong type, expected string, but got <class 'NoneType'>")

    def test_extraction_markdown_empty_string(self):
        text = ""
        test_comparison = []
        test_result_links = extract_markdown_links(text)
        test_result_images = extract_markdown_images(text)
        self.assertEqual(test_comparison, test_result_links)
        self.assertEqual(test_comparison, test_result_images)

if __name__ == "__main__":
    unittest.main()