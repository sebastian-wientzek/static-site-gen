class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        result = ""
        if self.props == None:
            return ""
        for k, v in self.props.items():
            result += f' {k}="{v}"'
        return result
    
    def __eq__(self, other):
        if (
			self.tag == other.tag and 
			self.value == other.value and
			self.children == other.children and
            self.props == other.props
		):
            return True
        return False
    
    def __repr__(self):
        result = []
        if self.tag != None:
            result.append(f"tag={self.tag}")
        if self.value != None:
            result.append(f"value={self.value}")
        if self.children != None:
            result.append(f"children={self.children}")
        if self.props != None:
            result.append(f"props={self.props}")
        return f"HTMLNode(" + ", ".join(result) + ")"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value == None:
            raise ValueError("Leaf node must have a value")
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.tag == None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        