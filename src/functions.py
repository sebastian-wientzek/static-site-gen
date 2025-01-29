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


def split_nodes_image(old_nodes):
	_type_check(old_nodes, list)
	result = []
	for old_node in old_nodes:
		image_tuples = extract_markdown_images(old_node.text)
		images = _node_generator(image_tuples, TextType.IMAGE)
		if len(images) == 0:
			result.append(old_node)
		else:
			result.extend(_node_splitter(old_node.text, images, TextType.IMAGE))
	return result


def split_nodes_link(old_nodes):
	_type_check(old_nodes, list)
	result = []
	for old_node in old_nodes:
		link_tuples = extract_markdown_links(old_node.text)
		links = _node_generator(link_tuples, TextType.LINK)
		if len(links) == 0:
			result.append(old_node)
		else:
			result.extend(_node_splitter(old_node.text, links, TextType.LINK))
	return result


def text_to_textnodes(text):
	_type_check(text, str)
	delimiters = [("**", TextType.BOLD), ("*", TextType.ITALIC), ("`", TextType.CODE)]
	node = TextNode(text, TextType.TEXT)
	result = [node]
	for delimiter in delimiters:
		result = split_nodes_delimiter(result, delimiter[0], delimiter[1])
	result = split_nodes_image(result)
	result = split_nodes_link(result)
	return result


def markdown_to_blocks(markdown):
	md_blocks = markdown.split("\n\n")
	result = []
	for md_block in md_blocks:
		block = md_block.lstrip()
		block = block.rstrip()
		if len(block) > 0:
			result.append(block)
	return result


def _node_generator(tup_list, text_type):
	if text_type != TextType.IMAGE and text_type != TextType.LINK:
		raise Exception(f"node can't be generated for this type: {text_type}")
	result = []
	for tup in tup_list:
		result.append(TextNode(tup[0], text_type, tup[1]))
	return result


def _node_splitter(text, nodes, text_type):
	result = []
	for index in range(0, len(nodes)):
		if text_type == TextType.IMAGE:
			text_split = text.split(f"![{nodes[index].text}]({nodes[index].url})", 1)
		else:
			text_split = text.split(f"[{nodes[index].text}]({nodes[index].url})", 1)

		if text_split[0] != "":
			result.append(TextNode(text_split[0], TextType.TEXT))
		result.append(nodes[index])
		if len(text_split) > 1 and text_split[1] != "":
			text = text_split[1]
			if index + 1 == len(nodes):
				result.append(TextNode(text, TextType.TEXT))
	return result


def _type_check(element, expected_class):
	if not isinstance(element, expected_class):
		raise TypeError(f"wrong type, expected {expected_class}, but got {type(element)}")
