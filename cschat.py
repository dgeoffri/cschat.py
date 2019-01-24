#!/usr/bin/env python

import curses
import curses.textpad
from time import gmtime, strftime
import socket
import asyncore

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

outputwin = curses.newwin(48, 80, 0, 0)
outputwin.scrollok(True)
linewin = curses.newwin(1, 80, 49, 0)
linewin.hline('-', 80)
linewin.refresh()
inputwin = curses.newwin(1, 80, 50, 0)
inputwin.nodelay(1)
inputbox = curses.textpad.Textbox(inputwin)
# pad.edit()
while(True):
	ch = inputwin.getch()
	if ch > 0:
		if ch == 10:
			line = inputbox.gather()
			inputwin.clear()
			if line == "/quit ":
				break
			else:
				outputwin.addstr("Me(" + strftime("%H:%M:%S", gmtime()) + "): " + line + "\n")
				outputwin.refresh();
		else:
			inputbox.do_command(ch)

curses.echo()
curses.nocbreak()
curses.endwin()
