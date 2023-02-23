"""

"""
import pathlib
import consts

PHP_HEADER = "<?php\n"
PHP_FOOTER = "?>"


class Snippet:
    def __init__(self):
        self.text = ""

    def add_snippet(self, snippet, variables):
        

    @staticmethod
    def get_snippet(snippet_name: str, variables: dict):
        snippet_path = pathlib.Path(f"snippets/{snippet_name}")
        snippet = snippet_path.read_text()
        snippet = Snippet._insert_variables(snippet, variables)
        snippet = Snippet._remove_php_headers(snippet)
        return snippet

    @staticmethod
    def _remove_php_headers(snippet: str):
        if snippet.startswith(PHP_HEADER) and snippet.endswith(PHP_FOOTER):
            return snippet[len(PHP_HEADER):-1 * len(PHP_FOOTER)]
        raise TypeError("Invalid snippet given!")

    @staticmethod
    def _insert_variables(snippet_text, variables: dict):
        for variable, value in variables.items():
            snippet_text = snippet_text.replace(variable, Snippet.escape_characters(value))
        return snippet_text

    @staticmethod
    def escape_characters(value):
        if type(value) != str:
            return value
        escaped_characters = ["\\", "\""]
        for character in escaped_characters:
            value = value.replace(character, "\\" + character)
        return value
