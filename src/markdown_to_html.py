from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_to_blocks import markdown_to_blocks, block_to_block_type

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
            for heading in block_type_heading:
                if block.startswith(heading):
                    node = LeafNode(f'h{len(heading)-1}', block[len(heading):])
            nodes_list.append(node.to_html())
        elif block_to_block_type(block) == 'block_type_code':
            node = LeafNode('code', block.strip('```'))
            nodes_list.append(node.to_html())
        elif block_to_block_type(block) == 'block_type_quote':
            node = LeafNode('quote', block.strip('>'))
            nodes_list.append(node.to_html())
        elif block_to_block_type(block) == 'block_type_unordered_list':
            node = LeafNode('unordered_list', block.strip('* '))
            nodes_list.append(node.to_html())
        elif block_to_block_type(block) == 'block_type_ordered_list':
            node = LeafNode('ordered_list', block)
            nodes_list.append(node.to_html())
        else:  # block type is regular text
            node = LeafNode(None, block)
            nodes_list.append(node.to_html())

        parent_node = ParentNode("div", nodes_list)

    return parent_node    
