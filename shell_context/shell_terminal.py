"""
 Author: Ido
 Date: 27/08/21
 Purpose: Be the shell context for the webshell, run shell commands, putfile and getfile
"""

import cmd2
from webshell_master_cmd import WebshellCmd


class ShellTerminal(WebshellCmd):
    """
    Be shell context for the webshell, run shell commands, putfile and getfile
    """

    def __init__(self):
        super(WebshellCmd, self).__init__()
        self.prompt = "shell> "

    def default(self, statement: cmd2.Statement):
        pass
