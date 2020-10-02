import os
import sys

prompt = (5, "shell> ")


def eval(user_input, stdscr):
    stdscr.addch("\n")
    stdscr.refresh()
    os.system(user_input)
