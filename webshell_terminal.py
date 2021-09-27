"""
 Author: Ido
 Date: 27/08/21
 Purpose: Be the main cmd class to use in the project, disable bad cmd2 features
"""

from webshell_master_cmd import WebshellCmd

import shell_context.shell_terminal as shell
import db_context.database_terminal as database


class WebshellTerminal(WebshellCmd):
    """
    Be the main webshell context
    """

    def __init__(self):
        super(WebshellTerminal, self).__init__()
        self.prompt = "webshell> "

    def do_shell(self, statement):
        shell_context = shell.ShellTerminal()
        shell_context.cmdloop()

    def do_database(self, statement):
        database_context = database.DatabaseTerminal()
        database_context.cmdloop()
