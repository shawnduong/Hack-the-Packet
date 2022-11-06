#!/usr/bin/env python3

import warnings
warnings.simplefilter("ignore", Warning)

from scapy.all import *
import sys
load_layer("http")

N = 10000

def handle(p):

	if p.haslayer(DNS):
		print(":: Found interesting DNS traffic:")
		print(" "*4 + p.summary())
	elif p.haslayer(HTTPRequest):
		print(":: Found interesting HTTP traffic:")
		print(" "*4 + p.summary())

def main(iface):

	print(f":: Sniffing {N} packets on {iface}.")
	sniffer = sniff(iface=iface, prn=handle, count=N)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print(f"Usage: {sys.argv[0]} <interface>")
	else:
		main(sys.argv[1])
