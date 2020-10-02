import repl
import sys
import types
import inspect
import re

color = "\u001b[32m"
prompt = f"{color}py> \u001b[0m"


def pretty_print(x):
    if isinstance(x, types.BuiltinFunctionType):
        name = x.__name__
        try:
            sig = inspect.signature(x)
            sys.stdout.write("\u001b[90mbuilt in function\u001b[0m " + re.sub(
                r", ([/*]),?(.*)\)", " \\1\u001b[90m\\2\u001b[0m)", f"{name}{str(sig)}", 1))
        except:
            sys.stdout.write(
                f"\u001b[90mbuilt in function\u001b[0m {name}(??)")
        sys.stdout.flush()
    elif isinstance(x, types.FunctionType):
        name = x.__name__ if x.__name__ != "<lambda>" else 'λ'
        sig = inspect.signature(x)
        sys.stdout.write(re.sub(
            r", ([/*]),?(.*)\)", " \\1\u001b[90m\\2\u001b[0m)", f"{name}{str(sig)}", 1))
        sys.stdout.flush()
    elif isinstance(x, types.ModuleType):
        name = x.__name__
        if hasattr(x, "__version__"):
            sys.stdout.write(
                f"module {name} \u001b[90m(v{x.__version__})\u001b[0m")
            sys.stdout.flush()
        else:
            sys.stdout.write(f"module {name}")
            sys.stdout.flush()
    else:
        sys.stdout.write(repr(x))
        sys.stdout.flush()


def eval(user_input):
    if user_input == 'help':
        return sys.stdout.write("\nPress ? to enter \u001b[33mhelp mode\u001b[0m")

    try:
        x = repl.eval(user_input)
        if user_input.startswith("import"):
            if hasattr(x, '__version__'):
                sys.stdout.write(f" \u001b[90m(v{x.__version__})")
        elif user_input.startswith("from"):
            if hasattr(x, '__version__'):
                sys.stdout.write(f" \u001b[90m(v{x.__version__})")
        else:
            sys.stdout.write("\n")
            pretty_print(x)
    except Exception as e:
        sys.stdout.write(f"\n{str(e)}")
