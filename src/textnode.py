from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
	TEXT = "text"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = "code"
	LINK = "link"
	IMAGE = "image"

class TextNode:
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other):
		if (
			self.text == other.text and 
			self.text_type == other.text_type and
			self.url == other.url
		):
			return True
		return False
	
	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"
	

def text_node_to_html_node(text_node):
	if not isinstance(text_node, TextNode):
		raise Exception("Not an instance of class TextNode")

	match text_node.text_type:
		case TextType.TEXT:
			return LeafNode(value=text_node.text)
		case TextType.BOLD:
			return LeafNode("b", text_node.text)
		case TextType.ITALIC:
			return LeafNode("i", text_node.text)
		case TextType.CODE:
			return LeafNode("code", text_node.text)
		case TextType.LINK:
			return LeafNode("a", text_node.text, {"href": text_node.url})
		case TextType.IMAGE:
			return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
		case _:
			raise Exception(f"TextType {text_node.text_type} is invalid")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	for node in old_nodes:
		if node.text_type == TextType.TEXT and delimiter in node.text:
			text_splitted = node.text.split(delimiter)
			if len(text_splitted) % 2 == 0:
				raise Exception("Missing a closing delimiter")
			for num in range(len(text_splitted)):
				if num % 2 == 0:
					new_nodes.append(TextNode(text_splitted[num], TextType.TEXT))
				else:
					new_nodes.append(TextNode(text_splitted[num], text_type))
		else:
			new_nodes.append(node)
	return new_nodes