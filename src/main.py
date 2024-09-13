from textnode import TextNode 
from htmlnode import HTMLNode, LeafNode



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
    print(f'Leaf Node: {g.to_html()}')

if __name__ == "__main__":
    main()


