"""
 Author: Ido
 Date: 15/09/21
 Purpose: Implement snippet utility
"""


def combine_snippets(snippets: str, variables: dict):
    snippet_data = []
    for snippet in snippets:
        snippet_data += [get_snippet(snippet, variables)]
    combined_snippet = consts.INNER_SEPERATOR_COMMAND.join(snippet_data)
    combined_snippet = add_separators(combined_snippet)
    return combined_snippet





def add_separators(snippet: str):
    return consts.INNER_SEPERATOR + snippet + consts.INNER_SEPERATOR
