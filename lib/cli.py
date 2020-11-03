from __future__ import unicode_literals

import sqlite3
from pygments.lexers.sql import SqlLexer
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.history import FileHistory
from prompt_toolkit.lexers import PygmentsLexer

from lib.config import style, bindings, bottom_toolbar, multiline_bool, sql_completer


def main(database):
    print("\nWelcome to Sqshell, an SQL REPL!\n")
    connection = sqlite3.connect(database)
    session = PromptSession(
        lexer=PygmentsLexer(SqlLexer),
        completer=sql_completer,
        history=FileHistory(".sqshell_history"),
        auto_suggest=AutoSuggestFromHistory(),
        complete_in_thread=True,
        key_bindings=bindings,
        multiline=multiline_bool,
        mouse_support=True,
        bottom_toolbar=bottom_toolbar,
        style=style,
    )

    while True:
        try:
            message = [
                ("class:language", "SQL"),
                ("class:arrow", " \u279C "),
            ]
            text = session.prompt(message, style=style)
        except KeyboardInterrupt:
            continue  # Control-C pressed. Try again.
        except EOFError:
            break  # Control-D pressed.

        with connection:
            try:
                messages = connection.execute(text)
            except Exception as e:
                print(repr(e))
            else:
                for message in messages:
                    print(message)

    print("Goodbye!")
