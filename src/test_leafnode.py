import unittest
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_1(self):
        node1 = LeafNode(tag=None, value="test value")
        node2 = LeafNode(tag=None, value="test value")
        self.assertEqual(node1, node2)

    def test_eq_2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        cmp_str = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), cmp_str)
    
if __name__ == "__main__":
    unittest.main()