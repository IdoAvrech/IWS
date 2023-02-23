"""
 Author: Ido
 Date: 27/08/21
 Purpose: Be the main cmd class to use in the project, disable bad cmd2 features
"""

RESPONSE_SEPARATOR_CHAR = "-"
RESPONSE_SEPARATOR = RESPONSE_SEPARATOR_CHAR * 50
RESPONSE_SEPARATOR_COMMAND = f"echo(\"{RESPONSE_SEPARATOR_CHAR}\");\n"

INNER_SEPERATOR_CHAR = '_'
INNER_SEPERATOR = INNER_SEPERATOR_CHAR * 50
INNER_SEPERATOR_COMMAND = f'echo(\"{INNER_SEPERATOR_CHAR}\");\n'

HTTP_METHOD = "post"
HTTP_VARIABLE = "test"

url = "http://localhost/index.php"