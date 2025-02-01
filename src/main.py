from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from functions import *
import os, shutil

def main():
	copy_static_to_public()


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


def folder_deep_search(start_folder, folders=None, files=None):
	if folders == None and files == None:
		folders = [start_folder]
		files = []

	if not os.path.exists(start_folder):
		raise Exception(f"The given path '{start_folder}' doesn not exist.")
	
	current_folder = os.listdir(start_folder)

	for elem in current_folder:
		joined_path = os.path.join(start_folder, elem)

		if os.path.isfile(joined_path):
			files.append(joined_path)
		
		if os.path.isdir(joined_path):
			folders.append(joined_path)
			folder_deep_search(joined_path, folders, files)

	return (folders, files)


if __name__ == "__main__":
	main()
