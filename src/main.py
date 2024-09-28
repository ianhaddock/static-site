from textnode import (
    TextNode, 
    text_node_to_html_node
    ) 
from htmlnode import (
    HTMLNode, 
    LeafNode, 
    ParentNode
    )
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


def main():

    print('running main.py\n')

    a = TextNode('text node', 'bold', 'https://www.example.com')
    b = TextNode('text node', 'bold', 'https://www.example.com')
    print(f'TextNode: {a}')


    c = HTMLNode('h1', 'This is a HTML Node', [], {"href": "http://www.example.com", "target": "_blank"})
    d = HTMLNode('h1', 'This is a HTML Node', [], {"href": "http://www.example.com", "target": "_blank"})
    print(f'HTMLNode: {c}')
    print(f'HTMLNode props-to-html: {c.props_to_html()}')


    e = LeafNode('a', 'Click Me!', {'href': 'http://www.example.com'})
    f = LeafNode('p', 'This is a paragraph of text.')
    g = LeafNode(None, 'text')

    print(f'Leaf Node: {e.to_html()}')
    print(f'Leaf Node: {f.to_html()}')
    print(f'Leaf Node: {g.to_html()}\n')

    h = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
) 

    i = ParentNode("p", [ParentNode("u", [LeafNode(None, "internal leaf text")]), LeafNode(None, "normal text")])

    print(h)
    print(f'ParentNode: {h.to_html()}') 
    print(f'ParentNode: {i.to_html()}')

    print('\n\n## textnode to htmlnode ##\n')

    j = TextNode('plain text node', 'text')
    test2 = text_node_to_html_node(j)
    print(f'<=> {test2.to_html()}')

    k = TextNode('bold text node', 'bold')
    test1 = text_node_to_html_node(k)
    print(f'<=> {test1.to_html()}') 

    l = TextNode('italic text node', 'italic')
    test3 = text_node_to_html_node(l)
    print(f'<=> {test3.to_html()}')

    m = TextNode('code text node', 'code')
    test4 = text_node_to_html_node(m)
    print(f'<=> {test4.to_html()}')

    n = TextNode('link text node', 'link', 'http://www.example.com')
    test5 = text_node_to_html_node(n)
    print(f'<=> {test5.to_html()}')

    # <img src="pic_trulli.jpg" alt="Italian Trulli"> 
    o = TextNode('image text node', 'image', 'http://www.example.com')
    test6 = text_node_to_html_node(o)
    print(f'<=> {test6.to_html()}') 


    print('\n\n## split nodes delimiter ##\n') 

    node0 = TextNode("This is text with a `code block` word", text_type_text)
    new_nodes = split_nodes_delimiter([node0], "`", text_type_code)
    print(new_nodes)
 
    node1 = TextNode("This is text with no modifer words", text_type_text)
    new_nodes = split_nodes_delimiter([node1], "*", text_type_italic)
    print(new_nodes)
 
    node2 = TextNode("This is first text with a **big old bold** block", text_type_text)
    node3 = TextNode("This is second text with a **big old bold** block", text_type_text)
    new_nodes = split_nodes_delimiter([node2, node3], "**", text_type_bold)
    print(new_nodes)
 
    new_nodes = split_nodes_delimiter([node0, node1, node2, node3], "`", text_type_code)
    print(f'>> {new_nodes}')

    
    print('\n\n## Regex ##\n')

    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))
    # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]












if __name__ == "__main__":
    main()


