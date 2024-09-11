import unittest
from htmlnode import HTMLNode

class HTMLNode_Test(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", "this is text in value", [], { "href": "http://www.example.com", "target": "_blank"})
        node2 = HTMLNode("h1", "this is text in value", [], { "href": "http://www.example.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_empty_is_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_value_not_eq(self):
        node = HTMLNode("h1", "his s ext n alue", [], { "href": "http://www.example.com", "target": "_blank"})
        node2 = HTMLNode("h1", "this is text in value", [], { "href": "http://www.example.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("h1", "This is a text value", [], {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(
            "HTMLNode(h1, This is a text value, [], {'href': 'https://www.boot.dev', 'target': '_blank'})", repr(node)
        )

    def test_props_to_html(self):
        node = HTMLNode("h1", "This is a text value", [], {"href": "http://www.example.com", "target": "_blank"})
        self.assertEqual(
        node.props_to_html(), ' href="http://www.example.com" target="_blank"'
        )

if __name__ = "__main__":
    unittest.main()

