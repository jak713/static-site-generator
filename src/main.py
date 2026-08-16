from textnode import TextNode, TextType

def main():
    textnode = TextNode("dummy anchor", TextType.LINK, "https://www.wikipedia.org")
    print(textnode)

if __name__ == "__main__":
    main()
