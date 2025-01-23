import unittest
from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_neq_1(self):
        node1 = TextNode("text node 1", TextType.CODE, "https://google.com")
        node2 = TextNode("text node 2", TextType.BOLD, "https://")
        self.assertNotEqual(node1, node2)

    def test_neq2(self):
        node1 = TextNode("text node", TextType.ITALIC)
        node2 = TextNode("text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_text_node_to_html_node(self):
        node_italic = TextNode("italic text", TextType.ITALIC)
        node_link = TextNode("link text", TextType.LINK, "https://google.com")
        self.assertEqual(text_node_to_html_node(node_italic).to_html(), "<i>italic text</i>")
        self.assertEqual(text_node_to_html_node(node_link).to_html(), '<a href="https://google.com">link text</a>')
    
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

if __name__ == "__main__":
    unittest.main()