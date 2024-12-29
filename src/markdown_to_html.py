from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_to_blocks import markdown_to_blocks, block_to_block_type

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
    )
from textnode import (
    TextNode, 
    text_node_to_html_node
    ) 

block_type_paragraph = "paragraph"
block_type_heading = ['# ', '## ', '### ', '#### ', '##### ', '###### ']
block_type_code = "```"
block_type_quote = ">"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"


#  ParentNode(
#          "h2",
#          [
#              LeafNode("b", "Bold text"),
#              LeafNode(None, "Normal text"),
#              LeafNode("i", "italic text"),
#              LeafNode(None, "Normal text"),
#          ],
#      )


def markdown_to_html_node(markdown: str) -> list:
    """ coverts a full markdown document into a single parent HTMLNode """

    blocks = markdown_to_blocks(markdown)
    nodes_list = []

    for block in blocks:
        if block_to_block_type(block) == 'block_type_heading':
            # html_leaf_nodes = text_to_children(block)
            for heading in block_type_heading:
                if block.startswith(heading):
                    node = ParentNode(f'h{len(heading)-1}', text_to_children(block[len(heading):]))
                    #node = text_to_children(block)
                    #new_node_text = text_to_children(node.to_html())
            nodes_list.append(node)

        elif block_to_block_type(block) == 'block_type_code':
            node = ParentNode('code', text_to_children(block.strip('```')))
            nodes_list.append(node)
        elif block_to_block_type(block) == 'block_type_quote':
            node = ParentNode('quote', text_to_children(block.strip('>')))
            nodes_list.append(node)
      #  elif block_to_block_type(block) == 'block_type_unordered_list':
      #      node = LeafNode('unordered_list', block.strip('* '))
      #      nodes_list.append(node.to_html())
      #  elif block_to_block_type(block) == 'block_type_ordered_list':
      #      node = LeafNode('ordered_list', block)
      #      nodes_list.append(node.to_html())
      #  else:  # block type is regular text
      #      node = LeafNode(None, block)
      #      nodes_list.append(node.to_html())

        parent_node = ParentNode("div", nodes_list)

    return parent_node    


def text_to_children(text_block: str) -> list:
    """ takes a string of text and returns a list of HTMLNodes that represent the
    inline markdown """

    text_nodes = text_to_textnodes(text_block)
    html_leaf_nodes = []

    for node in text_nodes:
        html_leaf_nodes.append(text_node_to_html_node(node))

    return html_leaf_nodes

