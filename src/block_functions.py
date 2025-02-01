from enums import BlockType
import re

def block_to_block_type(markdown):
	if len(re.findall(r"^#{1,6} {1}", markdown)) == 1:
		return BlockType.HEADING
	if "```" == markdown[:3] and "```" == markdown[-3:]:
		return BlockType.CODE
	
	md_splitted = markdown.split("\n")

	if all(len(elem) > 0 and elem[0] == ">" for elem in md_splitted):
		return BlockType.QUOTE
	if all(len(elem) > 2 and elem[0:2] == "* " or elem[0:2] == "- " for elem in md_splitted):
		return BlockType.UNORDERED_LIST
	
	for index in range(0, len(md_splitted)):
		if len(md_splitted[index]) < 3 or not md_splitted[index].startswith(f"{index+1}. "):
			return BlockType.PARAGRAPH
		
	return BlockType.ORDERED_LIST


def markdown_to_blocks(markdown):
	md_blocks = markdown.split("\n\n")
	result = []
	for md_block in md_blocks:
		block = md_block.lstrip()
		block = block.rstrip()
		if len(block) > 0:
			result.append(block)
	return result
