import modes.shell as shell_mode
import modes.python as py_mode
import modes.help as help_mode
import modes.pip as pip_mode
import splash
import repl

import msvcrt
import sys


modes = {
    "py": py_mode,
    "help": help_mode,
    "pip": pip_mode,
    "shell": shell_mode
}


def set_mode(new_mode):
    global current_mode, current_prompt
    current_mode = new_mode
    current_prompt = modes[current_mode].prompt
    sys.stdout.write("\u001b[2K\r")  # erase entire line
    sys.stdout.write(current_prompt)
    sys.stdout.flush()


current_mode = 'py'
current_prompt = py_mode.prompt
backspace = b"\x08"


line = ""

if __name__ == '__main__':
    sys.stdout.write(splash.logo)
    sys.stdout.write(current_prompt)
    sys.stdout.flush()


    while True:
        c = msvcrt.getch()

        if c == b'\xe0':
            c = msvcrt.getch()
            continue

        if c in [b'\x04', b'\x03']:
            if line == '':
                exit(0)

        elif c == b'\x0c':
            sys.stdout.write(f"\u001b[2J\u001b[0;0H{current_prompt}{line}")
            sys.stdout.flush()
        elif line == "" and current_mode == 'py' and c == b"]":
            set_mode("pip")
        elif line == "" and current_mode == 'py' and c == b"?":
            set_mode("help")
        elif line == "" and current_mode == 'py' and c == b";":
            set_mode("shell")
        elif c == backspace:
            if line == "":
                set_mode("py")
            elif len(line) > 0:
                line = line[:-1]
                sys.stdout.write('\b \b')
                sys.stdout.flush()
        elif c == b'\r':
            modes[current_mode].eval(line)

            sys.stdout.write(f"\n{current_prompt}")
            sys.stdout.flush()
            line = ""
        else:
            try:
                c = c.decode("utf-8")
                sys.stdout.write(c)
                sys.stdout.flush()
                line += c
            except:
                print(c)
