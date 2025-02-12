from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from functions import *
from block_functions import *
from converter import *
import os, shutil

def main():
	copy_static_to_public()
	generate_pages_recursive("content/", "template/template.html", "public/")


def copy_static_to_public():
	shutil.rmtree("./public/", True)
	folders, files = folder_deep_search("./static")

	for folder in folders:
		public_folder = folder.replace("/static", "/public")
		os.mkdir(public_folder)

	for file in files:
		public_file = file.replace("/static", "/public")
		print(f"copy from {file} to {public_file}")
		shutil.copy(file, public_file)


if __name__ == "__main__":
	main()
