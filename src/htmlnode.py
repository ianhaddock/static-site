
class HTMLNode():
    """HTML Node """

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ''

        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and \
                self.children == other.children and self.props == self.props:
                    return True

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'


class LeafNode(HTMLNode):
    """ Leaf Node, no parents """

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Invalid HTML: no value")
        if self.tag == None:
            return f'{self.value}'
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'    

    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'

class ParentNode(HTMLNode):
    """ handles nested HTML nodes """

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Invalid HTML: no tag")
        if self.children == None:
            raise ValueError("Invalid: no children")

        children_html = ''
        for child in self.children:
            children_html += child.to_html()
            
        return f'<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>'

    def __repr__(self):
        return f'ParentNode({self.tag}, children: {self.children}, {self.props})'
