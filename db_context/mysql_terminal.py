"""
 Author: Ido
 Date: 22/09/21
 Purpose: execute mysql terminal for database context
"""

import cmd2
from webshell_master_cmd import WebshellCmd
from snippets.snippet_handler import get_snippet
from communication import send_snippet


class MySQLTerminal(WebshellCmd):

    def __init__(self):
        super(WebshellCmd, self).__init__()
        self.prompt = "mysql> "

        self.host = "localhost"
        self.username = "toor"
        self.password = "12345"
        self.database = "test"
        self.port = "3306"

    def default(self, statement: cmd2.Statement):
        snippet = get_snippet("mysql_query.snippet",
                              {"SERVER_NAME": f"{self.host}",
                               "DB_USERNAME": self.username,
                               "DB_PASSWORD": self.password,
                               "DB_NAME": self.database,
                               "QUERY": statement.raw})
        print(send_snippet(snippet))
