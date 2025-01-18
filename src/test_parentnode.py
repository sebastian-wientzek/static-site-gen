import unittest
from htmlnode import ParentNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def _setup_children(self):
        children = [
            LeafNode("b", "bold text"),
            LeafNode(None, "normal text"),
            LeafNode("i", "italic text"),
            LeafNode("code", "code block")
        ]
        return children

    def test_initialzation(self):
        children = self._setup_children()
        node = ParentNode("div", children)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.children, children)
        self.assertIsNone(node.value)
        self.assertIsNone(node.props)

    def test_invalid_tag_init(self):
        children = self._setup_children()
        with self.assertRaises(ValueError) as context:
            ParentNode(None, children)
        self.assertEqual(str(context.exception), "tag is missing")

    def test_invalid_tag_to_html(self):
        children = self._setup_children()
        node = ParentNode("div", children)
        node.tag = None
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "tag is missing")
    
    def test_invalid_children_init(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", "invalid argument")
        self.assertEqual(str(context.exception), "list of children is missing")

    def test_invalid_children_to_html(self):
        children = self._setup_children()
        node = ParentNode("div", children)
        node.children = {}
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "list of children is missing")

    def test_to_html(self):
        children = self._setup_children()
        node = ParentNode("div", children)
        expected_result = "<div><b>bold text</b>normal text<i>italic text</i><code>code block</code></div>"
        self.assertEqual(node.to_html(), expected_result)

    def test_to_html_empty_children(self):
        node = ParentNode("div", [])
        expected_result = "<div></div>"
        self.assertEqual(node.to_html(), expected_result)

    def test_to_html_nested_parents(self):
        node_top = ParentNode("p", self._setup_children())
        node_bottom = ParentNode("div", self._setup_children())
        node_top.children.append(node_bottom)
        expected_result = "<p><b>bold text</b>normal text<i>italic text</i><code>code block</code><div><b>bold text</b>normal text<i>italic text</i><code>code block</code></div></p>"
        self.assertEqual(node_top.to_html(), expected_result)

    
if __name__ == "__main__":
    unittest.main()