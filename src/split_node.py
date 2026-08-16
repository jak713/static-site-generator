from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    nodes = []
    
    for node in old_nodes:
        if node.text_type!=TextType.TEXT:
            nodes.append(node)
            continue
        if node.text.count(delimiter)%2!=0:
            raise Exception("closing delimiter not found")

        text = node.text.split(delimiter)
        i = 0
        while i < len(text):
            if text[i] == "":
                i+=1
                continue

            if i%2==0:
                nodes.append(TextNode(text=text[i], text_type=TextType.TEXT))
            else:
                nodes.append(TextNode(text=text[i], text_type=text_type))
            i+=1

    return nodes

if __name__=="__main__":
    node = TextNode("**bold of you**", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
