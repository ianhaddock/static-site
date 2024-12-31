# test_markdown_to_html.py

import unittest
from markdown_to_html import (
    markdown_to_html_node,
    text_to_children
    )


class TestMarkdownToHTML(unittest.TestCase):


    def test_markdown_to_html_code_block(self):
        text =\
"```code with **bold** is werid main```\n\n"
        new_node = markdown_to_html_node(text)

        self.assertEqual(
        new_node.to_html(),
"<div><pre><code>code with <b>bold</b> is werid main</code></pre></div>"
        )


    def test_markdown_to_html_headings(self):
        text =\
"# This is a heading\n\n\
## THis is another heading\n\n\
### This is a third heading\n\n\
#### THis is a forth heading\n\n\
##### This is a fifth heading\n\n\
###### This is a sixth heading\n\n\
THis is a para"
        new_node = markdown_to_html_node(text)

        self.assertEqual(
        new_node.to_html(),
"<div><h1>This is a heading</h1><h2>THis is another heading</h2><h3>This is a third heading</h3>\
<h4>THis is a forth heading</h4><h5>This is a fifth heading</h5><h6>This is a sixth heading</h6>\
<p>THis is a para</p></div>" 
        )


    def test_markdown_to_html_paragraphs(self):
        text =\
"This is a paragraph with *lots* of **interesting** kinds of text and a `code block` and an \
![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"


        new_node = markdown_to_html_node(text)

        self.assertEqual(
        new_node.to_html(),
'<div><p>This is a paragraph with <i>lots</i> of <b>interesting</b> \
kinds of text and a <code>code block</code> and an <img src="https://i.imgur.com/fJRm4Vk.jpeg" \
alt="obi wan image"> and a <a href="https://boot.dev">link</a></p></div>'
        )


    def test_markdown_to_html_ordered_lists(self):
        text =\
"11. Ordered list `item` one\n\
12. Ordered list *item* two\n\
13. Ordered list **item** three\n\n"

        new_node = markdown_to_html_node(text)

        self.assertEqual(
        new_node.to_html(),
"<div><ol><li>Ordered list <code>item</code> one</li><li>Ordered list <i>item</i> two</li>\
<li>Ordered list <b>item</b> three</li></ol></div>"
        )


    def test_markdown_to_html_unordered_lists(self):
        text =\
"* Unordered List **Item** One\n\
* Unordered list *Item* two\n\
* Unordered List `Item` Three\n\n"

        new_node = markdown_to_html_node(text)

        self.assertEqual(
        new_node.to_html(),
"<div><ul><li>Unordered List <b>Item</b> One</li><li>Unordered list <i>Item</i> two</li>\
<li>Unordered List <code>Item</code> Three</li></ul></div>"
        )


    def test_markdown_to_html_blockquote(self):
        text = """
> quote `line` one
> quote *line* two
> quote **line** three
"""

        new_node = markdown_to_html_node(text)

        self.assertEqual(
        new_node.to_html(),
"<div><blockquote>quote <code>line</code> one quote <i>line</i> two quote <b>line</b> three</blockquote></div>"


        )
