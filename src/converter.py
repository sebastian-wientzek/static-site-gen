from functions import *
from block_functions import *
from htmlnode import *
from textnode import *
from enums import *


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_node = block_to_node(block, block_type)
        block_nodes.append(block_node)
    return ParentNode("div", block_nodes)

def block_to_node(block, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_block_to_node(block)
        case BlockType.HEADING:
            return header_block_to_node(block)
        case BlockType.CODE:
            return code_block_to_node(block)
        case BlockType.QUOTE:
            return quote_block_to_node(block)
        case _:
            return list_block_to_node(block, block_type)


def header_block_to_node(block):
    block_split = block.split(" ", 1)
    return LeafNode(f"h{len(block_split[0])}", block_split[1])


def list_block_to_node(block, block_type):
    if block_type == BlockType.ORDERED_LIST:
        block_tag = "ol"
    else:
        block_tag = "ul"

    item_list = block.split("\n")
    child_nodes = []

    for item in item_list:
        child_nodes.append(LeafNode("li", item.split(" ", 1)[1]))

    return ParentNode(block_tag, child_nodes)


def paragraph_block_to_node(block):
    text_nodes = text_to_textnodes(block)
    child_nodes = []
    for text_node in text_nodes:
        child_nodes.append(text_node_to_html_node(text_node))
    return ParentNode("p", child_nodes)


def code_block_to_node(block):
    block_clean = block[3:-3]
    return ParentNode("pre", [LeafNode("code", block_clean)])


def quote_block_to_node(block):
    block_clean = " ".join(block.replace(">","").split("\n"))
    return LeafNode("blockquote", block_clean)