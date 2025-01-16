import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_1(self):
        node1 = HTMLNode(value="test value")
        node2 = HTMLNode(value="test value")
        self.assertEqual(node1, node2)

    def test_eq_2(self):
        test_props = {"href": "https://google.com", "taget": "_blank"}
        node1 = HTMLNode(props=test_props)
        node2 = HTMLNode(props=test_props)
        self.assertEqual(node1.props_to_html(), node2.props_to_html())

    def test_neq_1(self):
        node1 = HTMLNode(tag="test tag")
        node2 = HTMLNode(value="test value")
        self.assertNotEqual(node1, node2)

    def test_neq2(self):
        node1 = HTMLNode(value="test value")
        node2 = HTMLNode(children="test child")
        self.assertNotEqual(node1, node2)
    
if __name__ == "__main__":
    unittest.main()