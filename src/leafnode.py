from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("all leaf nodes must have a value")
        if self.tag == None:
            return self.value
        if self.props is None:
            html_props = ""
        else:
            html_props = self.props_to_html()
        return f'<{self.tag}{html_props}>{self.value}</{self.tag}>'
