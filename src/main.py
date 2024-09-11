from textnode import TextNode 
from htmlnode import HTMLNode




def main():

    print('running main.py')

    a = TextNode('text node', 'bold', 'https://www.example.com')
    b = TextNode('text node', 'bold', 'https://www.example.com')
    print(f'TextNode: {a}')
    c = HTMLNode('h1', 'This is a HTML Node', [], {"href": "http://www.example.com", "target": "_blank"})
    d = HTMLNode('h1', 'This is a HTML Node', [], {"href": "http://www.example.com", "target": "_blank"})
    print(f'HTMLNode: {c}')
    print(f'HTMLNode props-to-html: {c.props_to_html()}')

if __name__ == "__main__":
    main()


