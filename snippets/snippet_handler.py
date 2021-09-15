"""
 Author: Ido
 Date: 15/09/21
 Purpose: Implement snippet utility
"""

import pathlib
import consts

PHP_HEADER = "<?php\n"
PHP_FOOTER = "?>"


def get_snippet(snippet_name: str, variables: dict):
    snippet_path = pathlib.Path(f"snippets/{snippet_name}")
    snippet = snippet_path.read_text()
    snippet = remove_php_headers(snippet)
    snippet = insert_variables(snippet, variables)
    snippet = add_separators(snippet)
    return snippet


def insert_variables(snippet: str, variables: dict):
    for variable, value in variables.items():
        snippet = snippet.replace(variable, escape_characters(value))
    return snippet


def escape_characters(value):
    if type(value) != str:
        return value
    escaped_characters = ["\\", "\""]
    for character in escaped_characters:
        value = value.replace(character, "\\" + character)
    return value


def remove_php_headers(snippet: str):
    if snippet.startswith(PHP_HEADER) and snippet.endswith(PHP_FOOTER):
        return snippet[len(PHP_HEADER):-1 * len(PHP_FOOTER)]
    raise TypeError("Invalid snippet given!")


def add_separators(snippet: str):
    return consts.PHP_SEPARATOR + snippet + consts.PHP_SEPARATOR
