from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from functions import *
from block_functions import *
from converter import *
import os, shutil
import sys

def main(args):
	basepath = args[0]
	copy_static_to_target()
	generate_pages_recursive("content/", "template/template.html", "docs/", basepath)


def copy_static_to_target(target="/docs"):
	shutil.rmtree("." + target, True)
	folders, files = folder_deep_search("./static")

	for folder in folders:
		public_folder = folder.replace("/static", target)
		os.mkdir(public_folder)

	for file in files:
		public_file = file.replace("/static", target)
		print(f"copy from {file} to {public_file}")
		shutil.copy(file, public_file)


if __name__ == "__main__":
	main(sys.argv)
