# main.py

import os
import shutil
import argparse

from htmlnode import (
    HTMLNode, 
    LeafNode, 
    ParentNode
    )
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
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_node_to_html_node
    )
from markdown_to_blocks import (
    markdown_to_blocks,
    block_to_block_type
    )
from markdown_to_html import (
    markdown_to_html_node
    )
from copy_static import (
    recursive_copy
    )
from generate_html import (
    extract_title,
    generate_pages
    )

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_file = "./template.html"

def main():
    """ main """

    if os.path.exists(dir_path_public):
        print(" > Deleting local public directory....")
        shutil.rmtree(dir_path_public)

    print(" > Copying static files to local public directory...")
    recursive_copy(dir_path_static, dir_path_public)

    print(" > Generating HTML pages...")
    generate_pages(dir_path_content, template_file, dir_path_public)



if __name__ == "__main__":
    main()


