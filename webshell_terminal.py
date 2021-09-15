"""
 Author: Ido
 Date: 27/08/21
 Purpose: Be the main cmd class to use in the project, disable bad cmd2 features
"""

from webshell_master_cmd import WebshellCmd


class WebshellTerminal(WebshellCmd):
    """
    Be the main webshell context
    """

    def __init__(self):
        super(WebshellTerminal, self).__init__()
        self.prompt = "webshell> "


