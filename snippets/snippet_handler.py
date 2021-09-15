"""
 Author: Ido
 Date: 15/09/21
 Purpose: Implement snippet utility
"""

import pathlib
import re

PHP_HEADER = "<?php"
PHP_FOOTER = "?>"


def get_snippet(snippet_name: str):
    snippet = pathlib.Path(snippet_name)
    if not snippet.exists():
        raise FileNotFoundError
    return snippet.read_text()


def insert_variables(snippet: str, variables: dict):
    for variable, value in variables:
        snippet = snippet.replace(variable, value)
    return snippet


def remove_php_headers(snippet: str):
    pattern = re.compile(PHP_HEADER + ".*" + PHP_FOOTER, re.DOTALL)
    fixed_snippet = re.finditer(pattern, snippet)
    return fixed_snippet
