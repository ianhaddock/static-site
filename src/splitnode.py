from textnode import TextNode







def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type) -> list:
    """Take a list of TextNodes and split at specific markdown"""
    new_nodes = []

    for node in old_nodes:
        if delimiter in node.text: 
            if node.text.count(delimiter) != 2:
                raise Exception(f'not valid Markup syntax, missing "{delimiter}"')

            prefix, markdown, postfix = node.text.split(delimiter)

            new_nodes.append( TextNode(prefix, node.text_type) )
            new_nodes.append( TextNode(markdown, text_type) )
            new_nodes.append( TextNode(postfix, node.text_type) )

            #print(f'Prefix: {prefix}, Markdown: {markdown}, Postfix: {postfix}')
        else:
            new_nodes.append(node)
      
    return new_nodes
