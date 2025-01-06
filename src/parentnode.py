from htmlnode import HTMLNode
from functools import reduce

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode requires tag")
        if not self.children:
            raise ValueError("ParentNode requires children")
        if self.props:
            html_props = self.props_to_html()
        else:
            html_props = ""
        return f"<{self.tag}{html_props}>{
                reduce(
                lambda acc, child: acc + child.to_html(),
                self.children,
                ""
                )
            }</{self.tag}>"