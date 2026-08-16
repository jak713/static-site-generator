import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(props={"href":"www.dev.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="www.dev.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode("tag", "value", None, props={"div": "center"})
        self.assertEqual(node.__repr__(), "HTMLNode:\nTag: tag\nValue: value\nChildren: None\nProps: {'div': 'center'}"
        )
if __name__ == "__main__":
    unittest.main()
