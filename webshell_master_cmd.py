"""
 Author: Ido
 Date: 27/08/21
 Purpose: Be the main cmd class to use in the project, disable bad cmd2 features
"""

import cmd2
import os


class WebshellCmd(cmd2.Cmd):
    delattr(cmd2.Cmd, 'do_shell')  # disable shell builtin command (runs generic shell terminal)
    delattr(cmd2.Cmd, 'do_ipy')  # disable ipy command (runs ipython)
    delattr(cmd2.Cmd, 'do_macro')  # disable macro builtin command (creates macros)
    delattr(cmd2.Cmd, 'do_py')  # disable py builtin command (runs python command)
    delattr(cmd2.Cmd, 'do_edit')  # disable edit builtin command (opens in editor a text file)
    delattr(cmd2.Cmd, 'do_alias')  # disable alias builtin command (create alias)

    def __init__(self):
        super().__init__()
        # Prints an intro banner once upon application startup
        self.intro = cmd2.style('Welcome to cmd2!', fg=cmd2.fg.red, bg=cmd2.bg.white, bold=True)
        # Show this as the prompt when asking for input
        self.prompt = 'master_cmd> '
        # Used as prompt for multiline commands after the first line
        self.continuation_prompt = '... '
        # Color to output text in with echo command
        self.foreground_color = 'cyan'
        # Make echo_fg settable at runtime
        self.add_settable(cmd2.Settable('foreground_color',
                                        str,
                                        'Foreground color to use with echo command',
                                        self,
                                        choices=cmd2.Wfg.colors()))

    @staticmethod
    def do_clear():
        """
        clear screen
        """
        os.system("cls || clear")
