"""
 Author: Ido
 Date: 27/08/21
 Purpose: Be the main cmd class to use in the project, disable bad cmd2 features
"""

import cmd2


class WebshellCmd(cmd2.Cmd):
    delattr(cmd2.Cmd, 'do_shell')  # disable shell builtin command (runs generic shell terminal)
    delattr(cmd2.Cmd, 'do_ipy')  # disable ipy command (runs ipython)
    delattr(cmd2.Cmd, 'do_macro')  # disable macro builtin command (creates macros)
    delattr(cmd2.Cmd, 'do_py')  # disable py builtin command (runs python command)
    delattr(cmd2.Cmd, 'do_edit')  # disable edit builtin command (opens in editor a text file)
    delattr(cmd2.Cmd, 'do_alias')  # disable alias builtin command (create alias)

    def __init__(self):
        super().__init__()
