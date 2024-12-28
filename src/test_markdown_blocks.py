import unittest
from markdown_to_blocks import (
    markdown_to_blocks,
    block_to_block_type
    )


class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        text = "# This is a heading\n\
\n\
   This is a paragraph of text. It has some **bold** and *italic* words inside of it.  \n\
\n\
* This is the first list item in a list block\n\
* This is a list item\n\
* This is another list item"
        new_node = markdown_to_blocks(text)
        self.assertEqual(
            [
                '# This is a heading', 
                'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
            ],
            new_node
        )


    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )


    def test_block_to_block_type_heading(self):
        
        text = "# This is a heading\n\
\n\
## THis is another heading\n\
\n\
### This is a third heading\n\
\n\
#### THis is a forth heading\n\
\n\
##### This is a fifth heading\n\
\n\
###### This is a sixth heading\n\
\n\
THis is a para"

        blocks = markdown_to_blocks(text)
        results = []
        for block in blocks:
            results.append(block_to_block_type(block))
        self.assertEqual(
            results,
            [
                "block_type_heading",
                "block_type_heading",
                "block_type_heading",
                "block_type_heading",
                "block_type_heading",
                "block_type_heading",
                "paragraph"
            ],
        )


    def test_block_to_block_type_quote(self):

        text = "> This is a quote line 1\n\
> This is a quote line 2\n\
> This is a quote line 3\n\
\n\
This is a para."

        blocks = markdown_to_blocks(text)
        results = []
        for block in blocks:
            results.append(block_to_block_type(block))
        self.assertEqual(
            results,
            [
                "block_type_quote",
                "paragraph"
            ]
        )


    def test_block_to_block_type_ordered_list(self):

        text = "1. This is an ordered list line 1\n\
2. This is an ordered list line 2\n\
3. This is an ordered list line 3"

        blocks = markdown_to_blocks(text)
        results = []
        for block in blocks:
            results.append(block_to_block_type(block))
        self.assertEqual(
            results,
            [
                "block_type_ordered_list"
            ]
        )


if __name__ == '__main__':
    unittest.main()
