import unittest
from block_functions import *
from enums import BlockType

class TestFunctions(unittest.TestCase):  
    def _block_string_setup(self):
        return """    # This is a heading   \n\n\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.    \n\n\n\n       \n\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n\n"""

    def test_markdown_to_blocks(self):
        markdown = self._block_string_setup()
        test_result = markdown_to_blocks(markdown)
        test_comparison = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertEqual(test_comparison, test_result)

    def test_block_to_block_type_paragraph(self):
        test_case = "This is a test paragraph.\nThere is nothing special in this block."
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(test_case))

    def test_block_to_block_type_heading(self):
        test_case = "#### This is a simple heading."
        self.assertEqual(BlockType.HEADING, block_to_block_type(test_case))

    def test_block_to_block_type_code(self):
        test_case = "```this is a code block.\n\n\nthe content is not important.```"
        self.assertEqual(BlockType.CODE, block_to_block_type(test_case))
    
    def test_block_to_block_type_quote(self):
        test_case = ">quote1\n>quote2\n>quote3"
        self.assertEqual(BlockType.QUOTE, block_to_block_type(test_case))
    
    def test_block_to_block_type_unordered_list(self):
        test_case = "* item1\n- item2\n* item3"
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(test_case))
    
    def test_block_to_block_type_ordered_list(self):
        test_case = "1. item1\n2. item2\n3. item3"
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(test_case))

    def test_block_to_block_type_heading_negative(self):
        test_case = "####### This is a simple heading."
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(test_case))

    def test_block_to_block_type_code_negative(self):
        test_case = "``this is a code block.\n\n\nthe content is not important.``"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(test_case))
    
    def test_block_to_block_type_quote_negative(self):
        test_case = ">quote1\n>quote2\n>quote3\n"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(test_case))
    
    def test_block_to_block_type_unordered_list_negative(self):
        test_case = "* item1\n- item2\n. item3"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(test_case))
    
    def test_block_to_block_type_ordered_list_negative(self):
        test_case = "1. item1\n2. item2\n3. item3\n"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(test_case))

    def test_extract_title_positive(self):
        test_case = "#        This is a Title       "
        test_comparison = "This is a Title"
        test_result = extract_title(test_case)
        self.assertEqual(test_comparison, test_result)

    def test_extract_title_negative(self):
        test_case = "## This is a H2 Header        "
        test_comparison = "no title found."
        with self.assertRaises(Exception) as context:
            extract_title(test_case)
        self.assertEqual(str(context.exception), test_comparison)
        
if __name__ == "__main__":
    unittest.main()