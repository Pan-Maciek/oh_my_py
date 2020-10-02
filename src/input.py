import curses
import time

def main(stdscr):
    x, y = 5, 5

    max_y, max_x = stdscr.getmaxyx()

    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    stdscr.attron(curses.color_pair(1))

    stdscr.addstr(y, x, "Hello")
    stdscr.attroff(curses.color_pair(1))

    stdscr.refresh()

    while True:
        key = stdscr.getch()
        stdscr.clear()
        stdscr.addstr(0, 0, f"{key}, {curses.KEY_UP} {chr(key)}")
        if key == curses.KEY_UP or key == curses.KEY_UP:
            return


curses.wrapper(main)


