from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
def main():
	textnode = TextNode("test", TextType.BOLD, "https://hi.com")
	htmlnode = HTMLNode(value="test val", props={"href": "https://google.com"})
	leafnode = LeafNode(tag="a", value="some text", props={"href": "https://google.com"})
	print(textnode)
	print(htmlnode.props_to_html())
	print(leafnode.to_html())


if __name__ == "__main__":
	main()
