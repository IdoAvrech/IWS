"""
 Author: Ido
 Date: 27/08/21
 Purpose: Be the main cmd class to use in the project, disable bad cmd2 features
"""

import cmd2


class webshell_cmd(cmd2.Cmd):

    def __init__(self):
        super().__init__()

    def do_ipy(self, **kwargs):
        """
        disable ipy command (runs ipython)
        """
        raise NotImplementedError

    def do_macro(self, **kwargs):
        """
        disable macro builtin command (creates macros)
        """
        raise NotImplementedError

    def do_py(self, **kwargs):
        """
        disable py builtin command (runs python command)
        """
        raise NotImplementedError

    def do_shell(self, **kwargs):
        """
        disable shell builtin command (runs generic shell terminal)
        """
        raise NotImplementedError

    def do_edit(self, **kwargs):
        """
        disable edit builtin command (opens in editor a text file)
        """
        raise NotImplementedError