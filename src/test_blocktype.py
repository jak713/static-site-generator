import unittest
from blocktype import BlockType, block_to_block_type
import blocktype

class TestBlockType(unittest.TestCase):

    def test_block_to_blocktype_code(self):
        block = "```\nimport hello\ndef hello():\n\t...\n```"

        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.CODE)

    def test_block_to_blocktype_ordered_list(self):
        block = "1. one\n2. two\n3. three"

        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.ORDERED_LIST)

    def test_block_to_blocktype_heading(self):
        block = "### this is a size 3 heading"

        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.HEADING)
