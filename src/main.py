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


    print('\n\n## split images and links ##\n')

    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        text_type_text,
    )
    new_nodes = split_nodes_link([node])
    print(new_nodes)

    node2 = TextNode(
        "This is text with no link to boot dev but with a link to [to youtube](https://www.youtube.com/@bootdotdev) and text at the end",
        text_type_text,
    )
    new_nodes = split_nodes_link([node2])
    print(f'{new_nodes}\n\n')

    node3 = TextNode(
        "[This starts with a link](http://www.to-stuff.org) then this text with no link to boot dev but with a link to [to youtube](https://www.youtube.com/@bootdotdev)",
        text_type_text,
    )
    new_nodes = split_nodes_link([node3])
    print(f'{new_nodes}\n\n')

    node4 = TextNode(
        "This has no links at all, just text",
        text_type_text,
    )
    new_nodes = split_nodes_link([node4])
    print(new_nodes)

    # [
    #     TextNode("This is text with a link ", text_type_text),
    #     TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
    #     TextNode(" and ", text_type_text),
    #     TextNode(
    #         "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
    #     ),
    # ]


    node = TextNode(
        "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
        text_type_text,
        )
    new_nodes = split_nodes_image([node])
    print(new_nodes)

    node2 = TextNode(
        "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and some text at the end",
        text_type_text,
        )
    new_nodes = split_nodes_image([node2])
    print(new_nodes)

    node3 = TextNode(
        "This is text without a image at all, just a string of text",
        text_type_text,
        )
    new_nodes = split_nodes_image([node3])
    print(new_nodes)


    print(f'\n\n## text to textnodes ##\n')

    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)" 
    new_nodes = text_to_textnodes(text)
    print(new_nodes) 

#    [
#    TextNode(This is , text, None),
#    TextNode(text, bold, None), 
#    TextNode( with an , text, None), 
#    TextNode(italic, italic, None), 
#    TextNode( word and a , text, None), 
#    TextNode(code block, code, None), 
#    TextNode( and an !, text, None), 
#    TextNode(obi wan image, link, https://i.imgur.com/fJRm4Vk.jpeg), 
#    TextNode( and a , text, None), 
#    TextNode(link, link, https://boot.dev)
#    ]

    text = "This is just text" 
    new_nodes = text_to_textnodes(text)
    print(new_nodes) 

#   [
#   TextNode(This is just text, text, None)
#   ]


    print(f'\n\n## markdown to blocks ##\n')

    text = "# This is a heading\n\
\n\
   This is a paragraph of text. It has some **bold** and *italic* words inside of it.  \n\
\n\
 ```this is some code```\n\
\n\
* This is the first list item in a list block\n\
* This is a list item\n\
* This is another list item\n\
\n\
> This is a quote line 1\n\
> This is a quote line 2\n\
> This is a quote line 3\n\
\n\
This is a para.\n\
\n\
1. This is an ordered list line 1\n\
2. This is an ordered list line 2\n\
3. This is an ordered list line 3\n\
\n\
## THis is another heading\n\
\n\
### This is a third heading\n\
\n\
#### THis is a forth heading\n\
\n\
##### This is a fifth heading\n\
\n\
###### This is a sixth heading\n\
\n\
THis is a para\n\
\n\
```This is a code block that spans\n\
two lines ```\n\
\n\
1. THis is a broken ordered list\n\
3. THis is a broken orderd list 2\n\
4. This is a borken ordere list 3\n\
\n\
THis is a para"

    new_node = markdown_to_blocks(text)
    print(new_node)


    print(f'\n\n## resulting block types ##\n')

    for node in new_node:
        block_type = block_to_block_type(node)
        print(block_type)


    print(f'/n/n ## markdown to html node ## \n')

    input_markdown = "# Heading 1 with *bold* text\n\n## Heading 2\n\n### Heading 3\n\nParagraph One. No modifiers.\n\n```code goes here```\n\n\
            Para two with *bold text* and _italics_ and stuff\n\n* Unordered List Item One\n* Unordered list Item two\n\
            * Unordered LIst Number Three\n\n\
            > quote line one\n\
            > quote line two\n\
            > quote line three\n\n"

    output_markdown = markdown_to_html_node(input_markdown)

    print(type(output_markdown))
    print(output_markdown)
    out = output_markdown.to_html()
    print(out)

    print(f'\n\n### same as above\n')
    string = "This *is* all **the** weird `code` stuff in one line"
    print(string)

    text_nodes = text_to_textnodes(string)
    html_nodes = []
    output = ''

    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))

    print(html_nodes)

    for node in html_nodes:
        output += str(node.to_html())

    print(output)















if __name__ == "__main__":
    main()


