from htmlnode import *
from textnode import *
import re

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

def extract_markdown_images(text):
	_type_check(text, str)
	return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
	_type_check(text, str)
	return re.findall(r"[^!]\[(.*?)\]\((.*?)\)", text)

def _type_check(element, expected_class):
	if not isinstance(element, expected_class):
		raise TypeError(f"wrong type, expected string, but got {type(element)}")
	