import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMD2Blocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_multiline(self):
        md = """
This is line 1


This is line 2


This is line 3
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is line 1",
                "This is line 2",
                "This is line 3"
            ]
        )

    def test_markdown_to_blocks_code(self):
        md = """
### This may be a heading

```
But this is a code block
```
"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "### This may be a heading",
                "```\nBut this is a code block\n```"
            ]
        )
