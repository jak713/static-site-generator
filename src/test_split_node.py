import unittest
from split_node import split_nodes_delimiter, split_nodes_link, split_nodes_image
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


class TestSplitNodeLinks(unittest.TestCase):
    
    def test_two_links(self):
        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT)
        new_nodes = split_nodes_link([node])

        self.assertEqual(new_nodes,
                         [
     TextNode("This is text with a link ", TextType.TEXT),
     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
     TextNode(" and ", TextType.TEXT),
     TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                         ])

    def test_two_of_the_same_link(self):
        node = TextNode("check [here](url) and again [here](url)", TextType.TEXT)
        new_nodes = split_nodes_link([node])

        self.assertEqual(new_nodes,
        [TextNode("check ", TextType.TEXT), TextNode("here", TextType.LINK, "url"), TextNode(" and again ", TextType.TEXT), TextNode("here", TextType.LINK, "url")])

    def test_no_link(self):
        node = TextNode("This is text with no links at all", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes,
                         [
                             TextNode("This is text with no links at all", TextType.TEXT),
                         ])

    def test_link_at_the_start(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev) is a great place to learn",
            TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes,
                         [
                             TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                             TextNode(" is a great place to learn", TextType.TEXT),
                         ])

    def test_link_at_the_end(self):
        node = TextNode(
            "You should check out [boot dev](https://www.boot.dev)",
            TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes,
                         [
                             TextNode("You should check out ", TextType.TEXT),
                             TextNode("boot dev", TextType.LINK, "https://www.boot.dev"),
                         ])

    def test_multiple_nodes(self):
        node1 = TextNode(
            "This has a [link](https://www.boot.dev) in it",
            TextType.TEXT)
        node2 = TextNode("This node has no links", TextType.TEXT)
        node3 = TextNode("bold text", TextType.BOLD)
        new_nodes = split_nodes_link([node1, node2, node3])
        self.assertEqual(new_nodes,
                         [
                             TextNode("This has a ", TextType.TEXT),
                             TextNode("link", TextType.LINK, "https://www.boot.dev"),
                             TextNode(" in it", TextType.TEXT),
                             TextNode("This node has no links", TextType.TEXT),
                             TextNode("bold text", TextType.BOLD),
                         ])

class TestSplitNodeImages(unittest.TestCase):

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ],
        new_nodes,
    )
if __name__ == "__main__":
    unittest.main()
