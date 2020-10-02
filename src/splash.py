import sys
import re

version, mounth, day, year = re.match(r"(\d\.\d(?:\.\d)?)\s*\(.*,\s+(\w+)\s+(\d+)\s(\d+)", sys.version).group(1, 2, 3, 4)

# blue, yellow, restore
b, y, r = (f"\u001b[{v}m" for v in [34, 33, 0])

logo = f"""
             _   _                   | oh_my_py - Julia inspired python shell
{b} _ __ {y} _   _{r}| |_| |__   ___  _ __    |
{b}| '_ \{y}| | | |{r} __| '_ \ / _ \| '_ \   | Type "?" for help, "]" for pip.
{b}| |_) {y}| |_| |{r} |_| | | | (_) | | | |  |
{b}| .__/{y} \__, |{r}\__|_| |_|\___/|_| |_|  | Version {version} ({mounth} {day} {year})
{b}|_|   {y} |___/{r}                         |

"""
