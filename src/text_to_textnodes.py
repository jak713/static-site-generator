from split_node import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text) -> list[TextNode]:
    delimiters = {
        "**":TextType.BOLD,
        "_":TextType.ITALIC,
        "`":TextType.CODE
    }

    nodes = [TextNode(text, TextType.TEXT)]

    for d,t in delimiters.items():
        nodes = split_nodes_delimiter(nodes, d, t)

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
