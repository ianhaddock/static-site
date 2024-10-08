

block_type_paragraph = "paragraph"
block_type_heading = ['# ', '## ', '### ', '#### ', '##### ', '###### ']
block_type_code = "```"
block_type_quote = ">"
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

    block_types = {
        'block_type_heading': ['# ', '## ', '### ', '#### ', '##### ', '###### '],
        'block_type_code': '```',
        'block_type_quote': '>',
        'block_type_unordered_list': ['* ', '- ', '+ ']
        }


#    print(f'<<>> {block}') 
    lines = block.splitlines()

    for heading in block_type_heading:
        if heading == block[:len(heading)]:
            return 'block_type_heading'

    if block_type_code == block[:3] and block_type_code == block[-3:]:
        return 'block_type_code'
            
    ordered_list = True
    line_number = 1
    for line in lines:
        if f'{line_number}. ' in line[:3]:
            line_number += 1
            continue
        else:
            ordered_list =  False    
    if ordered_list == True:
        return 'block_type_ordered_list'

    # this solves unordered lists and quote blocks - but too code golf?
    for block_type, values in block_types.items():
        check = True
        for value in values:
            for line in lines:
               # print(f'{value} >> {line[:len(value)-1]}') 
                if value == line[:len(value)]:
                    continue
                else:
                    check = False
            if check == True:
                return block_type

    return block_type_paragraph    

#        print(f'{block_type} >>>> {values}')

#    unordered_list = True 
#    for line in lines:
#        if block_types['block_type_unordered_list'][0] in line[:2]:
#            continue
#        else:
#            unordered_list = False
#    if unordered_list == True:
#        return 'block_type_unordered_list'
#
#    unordered_list = True 
#    for line in lines:
#        if block_types['block_type_unordered_list'][1] in line[:2]:
#            continue
#        else:
#            unordered_list = False
#            continue
#    if unordered_list == True:
#        return 'block_type_unordered_list'
#
#    quote_block = True
#    for line in lines:
#        if block_types['block_type_quote'] in line[:1]:
#            continue
#        else:
#            quote_block = False
#    if quote_block == True:
#        return 'block_type_quote'
#
