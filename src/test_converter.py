import unittest
from converter import *

class TestHTMLNode(unittest.TestCase):

    def _string_setup_input(self):
        val = ""
        val += "### This is a header\n\n"
        val += "This is a simple paragraph. Here is some ** bold ** and here * italic *.\n\n"
        val += "We also need an image ![I'm alt text](https://linktonowhere.com/nothing.png) and some [link](https://www.boot.dev/).\n\n"
        val += 5 * "* unordered list item\n- unordered list item 2\n"
        val += "\n\n"
        val += ">a little quote here.\n>another line can't be bad, right?\n\n"
        val += "#### a little code example:\n\n"
        val += "```x = 10\nprint(x * 20)```\n\n"
        val += "last line.\n"
        return val
    
    def _string_setup_html(self):
        val = "<div>"
        val += "<h3>This is a header</h3>"
        val += "<p>This is a simple paragraph. Here is some <b> bold </b> and here <i> italic </i>.</p>"
        val += '''<p>We also need an image <img src="https://linktonowhere.com/nothing.png" alt="I'm alt text"></img> and some <a href="https://www.boot.dev/">link</a>.</p>'''
        val += "<ul><li>unordered list item</li><li>unordered list item 2</li><li>unordered list item</li><li>unordered list item 2</li><li>unordered list item</li><li>unordered list item 2</li><li>unordered list item</li><li>unordered list item 2</li><li>unordered list item</li><li>unordered list item 2</li></ul>"
        val += "<blockquote>a little quote here. another line can't be bad, right?</blockquote>"
        val += "<h4>a little code example:</h4>"
        val += "<pre><code>x = 10\nprint(x * 20)</code></pre>"
        val += "<p>last line.</p>"
        val += "</div>"
        return val

    

    def test_markdown_to_html_node(self):
        test_input = self._string_setup_input()
        test_comparison = self._string_setup_html()
        test_result = markdown_to_html_node(test_input).to_html()
        self.assertEqual(test_comparison, test_result)
    
if __name__ == "__main__":
    unittest.main()