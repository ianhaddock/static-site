import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links
    )
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


class TestInlineMarkdown(unittest.TestCase):
    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(
            [
                TextNode('This is text with a ', text_type_text), 
                TextNode('code block', text_type_code), 
                TextNode(' word', text_type_text),
            ],
            new_nodes,
        )

    def test_two_node_block(self):
        node0 = TextNode("This is first text with a **big old bold** block", text_type_text)
        node1 = TextNode("This is second text with a **big old bold** block", text_type_text)
        new_nodes = split_nodes_delimiter([node0, node1], "**", text_type_bold)
        self.assertEqual(
            new_nodes,
            [
                TextNode('This is first text with a ', text_type_text),
                TextNode('big old bold', text_type_bold),
                TextNode(' block', text_type_text),
                TextNode('This is second text with a ', text_type_text),
                TextNode('big old bold', text_type_bold),
                TextNode(' block', text_type_text)
            ]
        )

    def test_no_markup_in_text(self):
        node0 = TextNode("This is text with no modifer words", text_type_text)
        new_nodes = split_nodes_delimiter([node0], "*", text_type_italic)
        self.assertEqual(
            new_nodes,
            [
                TextNode('This is text with no modifer words', text_type_text)
            ]
        )


    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic),
            ],
            new_nodes,
        )


    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        output = extract_markdown_images(text)
        self.assertEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                 ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            output
        )

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        output = extract_markdown_links(text)
        self.assertEqual(
            [
                ("to boot dev", "https://www.boot.dev"), 
                ("to youtube", "https://www.youtube.com/@bootdotdev")
            ],
            output
        )





if __name__ == '__main__':
    unittest.main()
