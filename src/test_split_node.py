import unittest
from split_node import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNode(unittest.TestCase):

    def test_code_correct(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE),TextNode(" word", TextType.TEXT)])

    def test_only_delimited(self):
        node = TextNode("**bold of you**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(new_nodes, [TextNode("bold of you", TextType.BOLD)])

    def test_empty_string_between(self):
        node = TextNode("   `some code`    ", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [TextNode("   ", TextType.TEXT), TextNode("some code", TextType.CODE), TextNode("    ", TextType.TEXT)])

    def test_no_delimiter(self):
        node = TextNode("Just some text, no delimiters here", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [node])

    def test_multiple_input_nodes(self):
        node1 = TextNode("Just some text, no delimiters here", TextType.TEXT)
        node2 = TextNode("Some **very** bold text", TextType.TEXT)
        node3 = TextNode("Even _more_ and **bolder** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2, node3], "_", TextType.ITALIC)

        self.assertEqual(new_nodes,
                         [node1, node2, TextNode("Even ", TextType.TEXT), TextNode("more", TextType.ITALIC), TextNode(" and **bolder** text", TextType.TEXT)])
if __name__ == "__main__":
    unittest.main()
