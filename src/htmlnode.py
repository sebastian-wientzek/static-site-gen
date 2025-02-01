class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props == None:
            return ""
        result = ""
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
        super().__init__(tag=tag, value=value, props=props)
        self._check_attributes()

    def to_html(self):
        self._check_attributes()
        if self.tag == None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        
    def _check_attributes(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        self._check_attributes()

    def to_html(self):
        self._check_attributes()
        result = ""
        for node in self.children:
            result += node.to_html()
        return f'<{self.tag}{self.props_to_html()}>{result}</{self.tag}>'

        
    def _check_attributes(self):
        if type(self.tag) is not str:
            raise ValueError("tag is missing")
        if type(self.children) is not list:
            raise ValueError("list of children is missing")
        