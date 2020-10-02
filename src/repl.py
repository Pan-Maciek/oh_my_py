import re

__global__ = {"print": lambda x: x}
__local__ = dict()
_eval = eval


def eval(user_input):
    try:
        x = __local__['ans'] = _eval(user_input, __global__, __local__)
        return x
    except:
        exec(user_input, __global__, __local__)
        if user_input.startswith("import"):
            name, alias = re.match("import\s+(\w+)(?:\s+as\s+(\w+))?", user_input).group(1, 2)
            return _eval(alias or name, __global__, __local__)
        elif user_input.startswith("from"):
            name = re.match("from\s+(\w+)", user_input).group(1)
            tmp = dict()
            exec(f"import {name}", tmp)
            return _eval(name, tmp, tmp)
