from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode


def text_node_to_html_node(text_node):
    if text_node.text_type is TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type is TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type is TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type is TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type is TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type is TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.url})
    else:
        raise Exception("Invalid TextType")


def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print("main")

    text_node = text_node_to_html_node(node)
    print(text_node)


main()
