import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Clickable", {"href":"example.com"})
        self.assertEqual(node.to_html(), '<a href="example.com">Clickable</a>')

    def test_no_tag(self):
        node = LeafNode(value="Just me, nothing else", tag=None)
        self.assertEqual(node.to_html(), 'Just me, nothing else')

    def test_repr(self):
        node = LeafNode("span", "not much new")
        self.assertEqual(node.__repr__(), 'LeafNode:\nTag: span\nValue: not much new\nProps: None')

if __name__=="__main__":
    unittest.main()
