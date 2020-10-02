from curses import *

default, blue, yellow = 1, 2, 3
gray = 6 
green = 4
red = 5

init_pair(default, COLOR_WHITE, COLOR_BLACK)
init_pair(blue, COLOR_BLUE, COLOR_BLACK)
init_pair(yellow, COLOR_YELLOW, COLOR_BLACK)
init_pair(green, COLOR_GREEN, COLOR_BLACK)
init_pair(red, COLOR_RED, COLOR_BLACK)
init_pair(gray, 8, COLOR_BLACK)

def color_print(stdscr, data):
    for cp, s in data:
        stdscr.attron(color_pair(cp))
        stdscr.addstr(s)
    stdscr.attroff(color_pair(data[-1][0]))