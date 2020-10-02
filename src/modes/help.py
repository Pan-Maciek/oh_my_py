import repl
import sys
import re

prompt = (3, "help?> ")


def eval(user_input, stdscr):
    sys.stdout.write("\n\n")
    doc = repl.eval(user_input).__doc__
    # doc = re.sub("``(.*?)``", "\u001b[33m\\1\u001b[0m", doc, 0)
    # doc = re.sub(r"\*(.*?)\*", "\u001b[32m\\1\u001b[0m", doc, 0)
    stdscr.addch("\n")
    stdscr.addstr(doc)
