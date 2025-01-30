import unittest
from block_functions import *


class TestFunctions(unittest.TestCase):  
    def _block_string_setup(self):
        return """    # This is a heading   \n\n\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.    \n\n\n\n       \n\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"""

    def test_markdown_to_blocks(self):
        markdown = self._block_string_setup()
        test_result = markdown_to_blocks(markdown)
        test_comparison = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertEqual(test_comparison, test_result)

if __name__ == "__main__":
    unittest.main()