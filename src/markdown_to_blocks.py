

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"


def markdown_to_blocks(markdown: str) -> list:
    """ takes raw markdown string and returns block strings """

    block_strings = markdown.split('\n\n')

    strings = []

    for block in block_strings:
        if block != "":
            strings.append(block.strip())

    return strings


def block_to_block_type(block: str) -> str:
    """ takes block of markdown and returns block type """

    headings = ['# ', '## ', '### ', '#### ', '##### ', '###### ']

    block_types = {
        'block_type_heading': ['# ', '## ', '### ', '#### ', '##### ', '###### '],
        'block_type_code': ['```'],
        'block_type_quote': ['>'],
        'block_type_unordered_list': ['* ', '- ']
        }


    print(f'<<>> {block}') 

    for heading in block_types['block_type_heading']:
        if heading in block:
            return block_type_heading

    code = block_types['block_type_code'][0] 
    if code in block[:3] and code in block[-3:]:
        return block_type_code
            
    lines = block.splitlines()
    unordered_list = True 
    for line in lines:
        if block_types['block_type_unordered_list'][0] in line[:2]:
            continue
        else:
            unordered_list = False
    if unordered_list == True:
        return block_type_unordered_list

    unordered_list = True 
    for line in lines:
        if block_types['block_type_unordered_list'][1] in line[:2]:
            continue
        else:
            unordered_list = False
            continue
    if unordered_list == True:
        return block_type_unordered_list

    quote_block = True
    for line in lines:
        if block_types['block_type_quote'][0] in line[:1]:
            continue
        else:
            quote_block = False
    if quote_block == True:
        return block_type_quote

    ordered_list = True
    line_number = 1
    for line in lines:
        if f'{line_number}. ' in line[:3]:
            line_number += 1
            continue
        else:
            ordered_list =  False    
    if ordered_list == True:
        return block_type_ordered_list









    return block_type_paragraph    
