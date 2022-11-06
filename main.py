#!/usr/bin/env python3

import warnings
warnings.simplefilter("ignore", Warning)

from scapy.all import *
from modules.HelloWorld import HelloWorld

import curses
import random
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

class Loot:
	"""
	Wrapper over all Loot types.
	"""

	def play(s: conf.L2socket):

		random.choice([
			WebGet.play
		])(s)

def main(iface, pcap):

	print(f":: Reading username wordlist...")
	usernames = [l for l in open("wordlists/usernames.txt").read().split("\n")]

	print(f":: Reading password wordlist...")
	passwords = [l for l in open("wordlists/passwords.txt").read().split("\n")]

	print(f":: Reading website wordlist...")
	websites = [l for l in open("wordlists/websites.txt").read().split("\n")]

	print(f":: Loading reader for packets from {pcap}...")
	preader = PcapReader(pcap)

	print(f":: Creating layer 2 socket on {iface}...")
	s = conf.L2socket(iface=iface)

	print(f":: Sending out a \"Hello World!\" as a sanity check...")
	HelloWorld.play(s)

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

	# Non-blocking getch.
	stdscr.nodelay(True)

	speed = 0  # packets/second e [0, inf)
	loot = 0   # probability e [0, 1]

	for i,line in enumerate(BANNER.split("\n")):
		stdscr.addstr(i, 1, line)

	stati = i

	stdscr.addstr(stati+1, 1, f" Current settings:               ")
	stdscr.addstr(stati+2, 1, f" rate = {speed} packets/second   ")
	stdscr.addstr(stati+3, 1, f" P(loot) = {loot:.2f}            ")
	stdscr.addstr(stati+4, 1, f"                                 ")
	stdscr.addstr(stati+5, 1, f" q   Quit the program.           ")
	stdscr.addstr(stati+6, 1, f"     Increase replay speed.      ")
	stdscr.addstr(stati+7, 1, f"     Decrease replay speed.      ")
	stdscr.addstr(stati+8, 1, f"     Increase loot probability.  ")
	stdscr.addstr(stati+9, 1, f"     Decrease loot probability.  ")
	stdscr.addch(stati+6, 2, curses.ACS_UARROW, curses.A_ALTCHARSET)
	stdscr.addch(stati+7, 2, curses.ACS_DARROW, curses.A_ALTCHARSET)
	stdscr.addch(stati+8, 2, curses.ACS_RARROW, curses.A_ALTCHARSET)
	stdscr.addch(stati+9, 2, curses.ACS_LARROW, curses.A_ALTCHARSET)
	stdscr.refresh()

	# Main loop.
	while True:

		c = stdscr.getch()

		if c == ord("q"):
			break
		elif c == curses.KEY_UP:
			speed += DELTA_SPEED
			stdscr.addstr(stati+2, 1, f" rate = {speed} packets/second   ")
			stdscr.refresh()
		elif c == curses.KEY_DOWN and speed-DELTA_SPEED >= -0.0001:
			speed -= DELTA_SPEED
			stdscr.addstr(stati+2, 1, f" rate = {speed} packets/second   ")
			stdscr.refresh()
		elif c == curses.KEY_RIGHT and loot+DELTA_LOOT <= 1.0001:
			loot += DELTA_LOOT
			stdscr.addstr(stati+3, 1, f" P(loot) = {loot:.2f}            ")
			stdscr.refresh()
		elif c == curses.KEY_LEFT and loot-DELTA_LOOT >= -0.0001:
			loot -= DELTA_LOOT
			stdscr.addstr(stati+3, 1, f" P(loot) = {loot:.2f}            ")
			stdscr.refresh()

		# Random probability of a loot sequence.
		try:
			if random.random() < loot:
				Loot.play(s)
			elif speed > 0:
				s.send(preader.next())
		except:
			pass

		if speed == 0:
			time.sleep(0.01)
		else:
			time.sleep(1/speed)

	# End the TUI.
	curses.echo()
	curses.nocbreak()
	curses.curs_set(1)
	stdscr.keypad(False)
	curses.endwin()

	print(f":: Session complete.")

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: %s <INTERFACE> <PACKETCAP>" % sys.argv[0])
		print("<INTERFACE>    Interface to transmit packets on.")
		print("<PACKETCAP>    Capture of packets to replay as noise.")
	else:
		main(sys.argv[1], sys.argv[2])
