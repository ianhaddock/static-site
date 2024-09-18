import unittest
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

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a text node", "bold", "http://www.example.com")
        node2 = TextNode("This is a text node", "bold", "http://www.example.com")
        self.assertEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This i ext ode", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", "italic", "http://www.example.com")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, bold, https://www.boot.dev)", repr(node)
        )

    # textnode to htmlnode tests #

class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text_node_to_html_node(self):
        node = TextNode('plain text node', text_type_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(
            html_node.to_html(),
            "plain text node"
            )
        self.assertEqual(html_node.tag, None)  # nice test idea

    def test_bold_node_to_html_node(self):
        node = TextNode('bold text node', text_type_bold)
        out = text_node_to_html_node(node)
        self.assertEqual(
                out.to_html(),
                "<b>bold text node</b>"
                )
        self.assertEqual(out.tag, 'b')

    def test_link_text_node_to_html_node(self):
        node = TextNode('link text node', text_type_link, 'http://www.example.com')
        out = text_node_to_html_node(node)
        self.assertEqual(
                out.to_html(), '<a href="http://www.example.com">link text node</a>'
                )

    def test_img_text_node_to_html_node(self):
        node = TextNode('image text node', text_type_image, 'http://www.example.com')
        out = text_node_to_html_node(node)
        self.assertEqual(
                out.to_html(), '<img src="http://www.example.com" alt="image text node">'
                )
        self.assertEqual(out.tag, "img")
        self.assertEqual(out.value, "")


if __name__ == "__main__":
    unittest.main()

