import repl
import sys
import types
import inspect
import re
from color_print import color_print, yellow, default, gray

prompt = (4, "py> ")


def pretty_print(x, stdscr):
    if isinstance(x, types.BuiltinFunctionType):
        name = x.__name__
        try:
            sig = inspect.signature(x)
            color_print(stdscr, [
                (gray, "built in function"),
                (default, re.sub(r", ([/*]),?(.*)\)", " \\1\\2)", f" {name}{str(sig)}", 1))
            ])
        except:
            color_print(stdscr, [
                (gray, "built in function"),
                (default, f" {name}(??)")
            ])
        sys.stdout.flush()
    elif isinstance(x, types.FunctionType):
        name = x.__name__ if x.__name__ != "<lambda>" else 'λ'
        sig = inspect.signature(x)
        stdscr.addstr(re.sub(r", ([/*]),?(.*)\)", " \\1\\2)", f"{name}{str(sig)}", 1))
    elif isinstance(x, types.ModuleType):
        name = x.__name__
        if hasattr(x, "__version__"):
            color_print(stdscr, [
                (default, f"module {name} "),
                (gray, f"(v{x.__version__})")
            ])
        else:
            stdscr.addstr(f"module {name}")
    else:
        stdscr.addstr(repr(x))


def eval(user_input, stdscr):
    if user_input == 'help':
        return color_print(stdscr, [(1, "\nPress ? to enter "), (yellow, "help mode")])

    try:
        x = repl.eval(user_input)
        if user_input.startswith("import"):
            if hasattr(x, '__version__'):
                color_print(stdscr, [(gray, f" (v{x.__version__})")])
        elif user_input.startswith("from"):
            if hasattr(x, '__version__'):
                color_print(stdscr, [(gray, f" (v{x.__version__})")])
        else:
            stdscr.addch("\n")
            pretty_print(x, stdscr)
    except Exception as e:
        sys.stdout.write(f"\n{str(e)}")
