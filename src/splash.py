import sys
import re
from color_print import color_print, blue, yellow, default

version, mounth, day, year = re.match(r"(\d\.\d(?:\.\d)?)\s*\(.*,\s+(\w+)\s+(\d+)\s(\d+)", sys.version).group(1, 2, 3, 4)


logo = [
    (default, "             _   _                   | oh_my_py - Julia inspired python shell\n"),
    (blue, " _ __ "), (yellow, " _   _"), (default, "| |_| |__   ___  _ __    |\n"),
    (blue,"| '_ \\"), (yellow, "| | | |"), (default, " __| '_ \ / _ \| '_ \   | Type \"?\" for help, \"]\" for pip.\n"),
    (blue, "| |_) "), (yellow, "| |_| |"), (default, " |_| | | | (_) | | | |  |\n"),
    (blue, "| .__/"), (yellow, " \__, |"), (default, f"\__|_| |_|\___/|_| |_|  | Version {version} ({mounth} {day} {year})\n"),
    (blue, "|_|   "), (yellow, " |___/"), (default, "                         |\n\n")
]


def show(stdscr):
    color_print(stdscr, logo)