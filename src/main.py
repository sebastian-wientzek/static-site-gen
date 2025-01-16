from textnode import TextNode, TextType

def main():
	textnode = TextNode("test", TextType.BOLD, "https://hi.com")
	print(textnode)


if __name__ == "__main__":
	main()
