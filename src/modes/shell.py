import os
import sys

color = "\u001b[31m"
prompt = f"{color}shell> \u001b[0m"


def eval(user_input):
    sys.stdout.write("\n")
    os.system(user_input)
