import repl
import sys
import re

color = "\u001b[33m"
prompt = f"{color}help?> \u001b[0m"


def eval(user_input):
    sys.stdout.write("\n\n")
    doc = repl.eval(user_input).__doc__
    doc = re.sub("``(.*?)``", "\u001b[33m\\1\u001b[0m", doc, 0)
    doc = re.sub(r"\*(.*?)\*", "\u001b[32m\\1\u001b[0m", doc, 0)
    print(doc)
