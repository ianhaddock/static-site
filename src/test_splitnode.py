import unittest
from splitnode import split_nodes_delimiter
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_node_to_html_node
    )


class TestSplitNode(unittest.TestCase):
    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(
            str(new_nodes), 
            '[TextNode(This is text with a , text, None), TextNode(code block, code, None), TextNode( word, text, None)]'
            )

    def test_two_node_block(self):
        node0 = TextNode("This is first text with a **big old bold** block", text_type_text)
        node1 = TextNode("This is second text with a **big old bold** block", text_type_text)
        new_nodes = split_nodes_delimiter([node0, node1], "**", text_type_bold)
        self.assertEqual(
            str(new_nodes),
            '[TextNode(This is first text with a , text, None), TextNode(big old bold, bold, None), \
TextNode( block, text, None), TextNode(This is second text with a , text, None), TextNode(big old bold, \
bold, None), TextNode( block, text, None)]'
            )

    def test_no_markup_in_text(self):
        node0 = TextNode("This is text with no modifer words", text_type_text)
        new_nodes = split_nodes_delimiter([node0], "*", text_type_italic)
        self.assertEqual(
            str(new_nodes),
            '[TextNode(This is text with no modifer words, text, None)]'
            )
