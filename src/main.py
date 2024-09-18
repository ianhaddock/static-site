from textnode import TextNode, text_node_to_html_node 
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():

    print('running main.py')

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
    print(f'Leaf Node: {g.to_html()}\n\n')

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
    print(f'ParentNode: {h.to_html()}\n') 
    print(f'ParentNode: {i.to_html()}\n\n')

    print('## textnode to htmlnode ##\n')

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



if __name__ == "__main__":
    main()


