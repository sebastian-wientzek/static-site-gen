from enums import BlockType

def block_to_block_type(markdown):
    pass


def markdown_to_blocks(markdown):
	md_blocks = markdown.split("\n\n")
	result = []
	for md_block in md_blocks:
		block = md_block.lstrip()
		block = block.rstrip()
		if len(block) > 0:
			result.append(block)
	return result
