#!/usr/bin/env python3

import warnings
warnings.simplefilter("ignore", Warning)

from scapy.all import *

import curses
import sys
import time

BANNER = r"""
   __ __         __     __  __         ___           __       __ 
  / // /__ _____/ /__  / /_/ /  ___   / _ \___ _____/ /_____ / /_
 / _  / _ `/ __/  '_/ / __/ _ \/ -_) / ___/ _ `/ __/  '_/ -_) __/
/_//_/\_,_/\__/_/\_\  \__/_//_/\__/ /_/   \_,_/\__/_/\_\\__/\__/ 
                                                                 
"""

DELTA_SPEED = 1
DELTA_LOOT = 0.01

# Global status variables.
speed = 0  # packets/second
loot = 0   # probability e [0, 1]

def main(iface, pcap, icap):

	print(f":: Loading reader for packets from {pcap}...")
	preader = PcapReader(pcap)

	print(f":: Loading reader for packets from {icap}...")
	ireader = PcapReader(icap)

	print(f":: Creating layer 2 socket on {iface}...")
	s = conf.L2socket(iface=iface)

	print(f":: Initialization complete.")
	print(f":: Starting replay.")
	time.sleep(1)

	# Set up TUI.
	stdscr = curses.initscr()
	curses.noecho()
	curses.cbreak()
	curses.curs_set(0)
	stdscr.keypad(True)
	stdscr.clear()

	for i,line in enumerate(BANNER.split("\n")):
		stdscr.addstr(i, 1, line)

	stdscr.addstr(i+1, 1, f" Current settings:               ")
	stdscr.addstr(i+2, 1, f" rate = {speed} packets/second   ")
	stdscr.addstr(i+3, 1, f" P(loot) = {loot:.2f}            ")
	stdscr.addstr(i+4, 1, f"                                 ")
	stdscr.addstr(i+5, 1, f" q   Quit the program.           ")
	stdscr.addstr(i+6, 1, f"     Increase replay speed. ")
	stdscr.addstr(i+7, 1, f"     Decrease replay speed.      ")
	stdscr.addstr(i+8, 1, f"     Increase loot probability.  ")
	stdscr.addstr(i+9, 1, f"     Decrease loot probability.  ")
	stdscr.addch(i+6, 2, curses.ACS_UARROW, curses.A_ALTCHARSET)
	stdscr.addch(i+7, 2, curses.ACS_DARROW, curses.A_ALTCHARSET)
	stdscr.addch(i+8, 2, curses.ACS_RARROW, curses.A_ALTCHARSET)
	stdscr.addch(i+9, 2, curses.ACS_LARROW, curses.A_ALTCHARSET)
	stdscr.refresh()

	# Main loop.
	while True:

		c = stdscr.getch()

		if c == ord("q"):
			break

	# End the TUI.
	curses.echo()
	curses.nocbreak()
	curses.curs_set(1)
	stdscr.keypad(False)
	curses.endwin()

	print(f":: Session complete.")

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("Usage: %s <INTERFACE> <PACKETCAP> <INJECTCAP>" % sys.argv[0])
		print("<INTERFACE>    Interface to replay packets on.")
		print("<PACKETCAP>    Capture of packets to replay.")
		print("<INJECTCAP>    Capture of packets to inject.")
	else:
		main(sys.argv[1], sys.argv[2], sys.argv[3])
