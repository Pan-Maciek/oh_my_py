from curses import *
import repl

def main(stdscr):
    import splash
    import modes.shell as shell_mode
    import modes.python as py_mode
    import modes.help as help_mode
    import modes.pip as pip_mode

    modes = {
        "py": py_mode,
        "help": help_mode,
        "pip": pip_mode,
        "shell": shell_mode
    }

    def set_mode(new_mode):
        nonlocal current_mode, current_prompt
        current_mode = new_mode
        current_prompt = modes[current_mode].prompt

    def print_prompt(stdscr):
        color, prompt = current_prompt
        stdscr.refresh()
        stdscr.attron(color_pair(color))
        y, _ = getsyx()
        stdscr.move(y, 0)
        stdscr.clrtoeol()
        stdscr.addstr(prompt)
        stdscr.attroff(color_pair(color))

    current_mode = 'py'
    current_prompt = py_mode.prompt
    line = ""

    splash.show(stdscr)
    print_prompt(stdscr)

    while True:
        key = stdscr.getch()
        if key in [3, 4]:  # ^C, ^D
            break
        elif key == 12:  # ^L
            stdscr.clear()
            print_prompt(stdscr)
            stdscr.addstr(line)
        elif key == 8:
            if line == "":
                set_mode("py")
                print_prompt(stdscr)
            else:
                stdscr.addstr("\b \b")
                line = line[:-1]
        elif line == "" and current_mode == 'py' and key == ord("]"):
            set_mode("pip")
            print_prompt(stdscr)
        elif line == "" and current_mode == 'py' and key == ord("?"):
            set_mode("help")
            print_prompt(stdscr)
        elif line == "" and current_mode == 'py' and key == ord(";"):
            set_mode("shell")
            print_prompt(stdscr)
        elif key in [10, 14]:  # enter
            modes[current_mode].eval(line, stdscr)
            stdscr.addstr("\n")
            set_mode("py")
            print_prompt(stdscr)
            line = ""
        else:
            c = chr(key)
            line += c
            stdscr.addch(c)

        stdscr.refresh()


if __name__ == '__main__':
    wrapper(main)
