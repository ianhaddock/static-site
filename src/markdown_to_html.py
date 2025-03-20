# markdown_to_html.py

import re
from htmlnode import (
    ParentNode
    )
from markdown_to_blocks import (
    markdown_to_blocks,
    block_to_block_type
    )
from inline_markdown import (
    text_to_textnodes
    )
from textnode import (
    text_node_to_html_node
    )

block_type_paragraph = "paragraph"
block_type_heading = ['# ', '## ', '### ', '#### ', '##### ', '###### ']
block_type_code = "```"
block_type_quote = ">"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"


def markdown_to_html_node(markdown: str) -> object:
    """ coverts a full markdown document into a single parent HTMLNode """

    blocks = markdown_to_blocks(markdown)
    nodes_list = []
    for block in blocks:
        nodes_list.append(block_to_html_node(block))

    return ParentNode("div", nodes_list, None)


def block_to_html_node(block: str) -> object:
    """ converts markdown block to html LeafNode """

    block_type = block_to_block_type(block)

    if block_type == 'block_type_heading':
        return heading_to_html_node(block)
    elif block_type == 'block_type_code':
        return code_to_html_node(block)
    elif block_type == 'block_type_quote':
        return quote_to_html_node(block)
    elif block_type == 'block_type_unordered_list':
        return unordered_list_to_html(block)
    elif block_type == 'block_type_ordered_list':
        return ordered_list_to_html(block)
    elif block_type == 'block_type_paragraph':
        return paragraph_to_html(block)
    else:
        raise ValueError(f"Invalid block type: {block}")


def heading_to_html_node(block: str) -> object:
    for heading in block_type_heading:
        if block.startswith(heading):
            node = ParentNode(f'h{len(heading)-1}', text_to_children(block[len(heading):]))

    return node


def code_to_html_node(block: str) -> object:
    code = []

    if not block.startswith('```') or not block.endswith('```'):
        raise ValueError("Invalid code block")
    code.append(ParentNode('code', text_to_children(block.strip('```'))))
    node = ParentNode('pre', code)

    return node


def quote_to_html_node(block: str) -> object:
    block_list = block.splitlines(keepends=False)
    clean_list = []
    for line in block_list:
        if not line.startswith('> '):
            raise ValueError("Quote block is invalid")
        clean_list.append(line.strip('> '))
    clean_quote = " ".join(clean_list)
    node = ParentNode('blockquote', text_to_children(clean_quote))

    return node


def unordered_list_to_html(block: str) -> object:
    block_list = block.splitlines(keepends=False)
    clean_list = []
    for line in block_list:
        clean_line = line[2:]
        clean_list.append(ParentNode("li", text_to_children(clean_line)))
    node = ParentNode('ul', clean_list)

    return node


def ordered_list_to_html(block: str) -> object:
    block_list = block.splitlines(keepends=False)
    clean_list = []
    for line in block_list:
        ### regex: remove one or more digits + '. ' at beginning of line
        clean_line = re.sub(r"\d+\. ", "", line)
        clean_list.append(ParentNode('li', text_to_children(clean_line)))
    node = ParentNode('ol', clean_list)

    return node


def paragraph_to_html(block: str) -> object:
    lines = block.splitlines(keepends=False)
    paragraph = "".join(lines)
    node = ParentNode('p', text_to_children(paragraph))

    return node


def text_to_children(text_block: str) -> list:
    """ takes a string of text and returns a list of HTMLNodes that represent the
    inline markdown """

    text_nodes = text_to_textnodes(text_block)
    html_leaf_nodes = []

    for node in text_nodes:
        html_leaf_nodes.append(text_node_to_html_node(node))

    return html_leaf_nodes
