import unittest
from textnode import TextNode, TextType


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
    
if __name__ == "__main__":
    unittest.main()