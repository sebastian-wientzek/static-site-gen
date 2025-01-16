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