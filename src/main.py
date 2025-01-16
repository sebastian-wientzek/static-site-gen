from textnode import TextNode, TextType
from htmlnode import HTMLNode
def main():
	textnode = TextNode("test", TextType.BOLD, "https://hi.com")
	htmlnode = HTMLNode(value="test val", props={"href": "https://google.com"})
	print(textnode)
	print(htmlnode)


if __name__ == "__main__":
	main()
