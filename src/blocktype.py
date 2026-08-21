from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'


def block_to_block_type(block: str) -> BlockType:
    if '# ' in block[:6]:
        return BlockType.HEADING
    if '```\n' in block[:4] and '```' in block[-3:]:
        return BlockType.CODE
    if block[0] == '>':
        return BlockType.QUOTE
    
    lines = block.split("\n")
    counter = 1
    while counter <= len(lines):
        if counter == len(lines):
            if lines[counter-1][:2] == '- ':
                return BlockType.UNORDERED_LIST
            if lines[counter-1][:3] == f'{counter}. ':
                return BlockType.ORDERED_LIST

        if lines[counter-1][:2] not in ['- ', f'{counter}.']:
            break

        counter+=1

    return BlockType.PARAGRAPH

