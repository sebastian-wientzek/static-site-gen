from functions import *
from block_functions import *
from htmlnode import *
from textnode import *
from enums import *
import os


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    _, files = folder_deep_search(dir_path_content)

    for file in files:
        if file.endswith(".md"):
            target_file = file.replace(dir_path_content, dest_dir_path)
            target_file = target_file.replace(".md", ".html")
            generate_page(file, template_path, target_file)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as md_file:
        md = md_file.read() 
    
    with open(template_path) as template_file:
        template = template_file.read()

    html_content = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)

    dir_path = os.path.dirname(dest_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(dest_path, "w") as result_html:
        result_html.write(template)


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
    text_nodes = _text_to_html_node(block_split[1])
    return ParentNode(f"h{len(block_split[0])}", text_nodes)


def list_block_to_node(block, block_type):
    if block_type == BlockType.ORDERED_LIST:
        block_tag = "ol"
    else:
        block_tag = "ul"

    item_list = block.split("\n")
    child_nodes = []

    for item in item_list:
        text = item.split(" ", 1)[1]
        text_nodes = _text_to_html_node(text)
        child_nodes.append(ParentNode("li", text_nodes))

    return ParentNode(block_tag, child_nodes)


def paragraph_block_to_node(block):
    child_nodes = _text_to_html_node(block)
    return ParentNode("p", child_nodes)


def code_block_to_node(block):
    block_clean = block[3:-3]
    return ParentNode("pre", [LeafNode("code", block_clean)])


def quote_block_to_node(block):
    block_clean = " ".join(block.replace(">","").lstrip().rstrip().split("\n"))
    return ParentNode("blockquote", _text_to_html_node(block_clean))


def _text_to_html_node(text):
    text_nodes = text_to_textnodes(text)
    child_nodes = []
    for text_node in text_nodes:
        child_nodes.append(text_node_to_html_node(text_node))
    return child_nodes