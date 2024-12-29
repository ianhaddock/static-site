import re
from textnode import (
	TextNode,
	text_type_text,
	text_type_bold,
	text_type_italic,
	text_type_code,
    text_type_link,
    text_type_image
	)


def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type) -> list:
    """Take a list of TextNodes and split at specific markdown"""
    new_nodes = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        split_nodes = []
        sections = node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise Exception(f'Invalid Markdown syntax, missing "{delimiter}"')

        for i in range(len(sections)):
            if sections[i] == "": 
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text: str) -> list:
    """Takes raw markdown and returns list of tuples"""
    
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str) -> list:
    """Takes raw markdown and returns list of tuples""" 
    
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    """ split image nodes into text and image nodes """

    new_nodes = []
    new_text = []
    new_images = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        node_images = extract_markdown_images(node.text)
        if len(node_images) == 0:
            new_nodes.append(node)
            continue

#        print(f'<<>> {node_images}')
        node_text = re.sub(r"!\[(.*?)\]\((.*?)\)", ',', node.text).split(',')
#        print(f'<<>> {node_text}') 

        for image in node_images:
            new_images.append(TextNode(image[0], text_type_image, image[1]))

        for text in node_text:
            new_text.append(TextNode(text, text_type_text))

        for i in range(max(len(new_images), len(new_text))):
#            print(new_text[i])
            if len(new_text[i].text) > 0:
                try:
                    new_nodes.append(new_text[i])
                except:
                    pass
#            print(new_links[i])
            try:
                new_nodes.append(new_images[i])
            except:
                pass

        #print(f'<>> {list(zip(new_links, new_text))} ')
    return new_nodes



def split_nodes_link(old_nodes: list) -> list:
    
    new_nodes = []
    new_text = []
    new_links = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        node_links = extract_markdown_links(node.text)
        if len(node_links) == 0:
            new_nodes.append(node)
            continue

        node_text = re.sub(r'\[(.*?)\]\((.*?)\)', ',', node.text).split(',')

#        print(f'>> node_links: {node_links}')
#        print(f'>> node_text: {node_text}')

        for link in node_links:
#            print(item)
            new_links.append(TextNode(link[0], text_type_link, link[1]))

        for text in node_text:
#            print(node)
#            if len(text) > 0:
            new_text.append(TextNode(text, text_type_text)) 
            
#        print(f'<> {new_text} <> {new_links} ')         

        for i in range(max(len(new_links), len(new_text))):
#            print(new_text[i])
            if len(new_text[i].text) > 0:
                try:
                    new_nodes.append(new_text[i])
                except:
                    pass
#            print(new_links[i])
            try:
                new_nodes.append(new_links[i])
            except:
                pass
        #print(f'<>> {list(zip(new_links, new_text))} ')
        
    return new_nodes



def text_to_textnodes(text) -> list:
    """ convert string of text to list of TextNodes"""

    node = [TextNode(text, text_type_text)]

    node = split_nodes_image(node) # should be run before split_nodes_link
    node = split_nodes_link(node)
    node = split_nodes_delimiter(node, "**", text_type_bold)
    node = split_nodes_delimiter(node, "*", text_type_italic)
    node = split_nodes_delimiter(node, "`", text_type_code)

    return node

