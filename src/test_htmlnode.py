import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    # leaf node tests

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_raise_value_error(self):
        node = LeafNode("a", None)
        self.assertRaises(ValueError, node.to_html)

    # parent node tests

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

    def test_raise_value_error_no_tag(self):
        node = ParentNode(None, [])
        self.assertRaises(ValueError, node.to_html)

    def test_raise_value_error_no_children(self):
        node = ParentNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_nested_parent_nodes(self):
        node = ParentNode("p", [ParentNode("u", [LeafNode(None, "internal leaf text")]), LeafNode(None, "top level text")])
        self.assertEqual(node.to_html(), "<p><u>internal leaf text</u>top level text</p>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()

