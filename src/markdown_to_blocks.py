def markdown_to_blocks(markdown:str) -> list[str]:
    raw = markdown.split("\n\n")
    blocks = []
    for line in raw:
        line = line.strip()
        if line == "":
            continue
        blocks.append(line)

    return blocks
