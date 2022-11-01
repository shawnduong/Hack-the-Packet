#!/usr/bin/env python3

import warnings
warnings.simplefilter("ignore", Warning)

from scapy.all import *
import sys

def main(iface, pcap, icap):

	print(f":: Loading reader for packets from {pcap}...")
	preader = PcapReader(pcap)

	print(f":: Loading reader for packets from {icap}...")
	ireader = PcapReader(icap)

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("Usage: %s <INTERFACE> <PACKETCAP> <INJECTCAP>" % sys.argv[0])
		print("<INTERFACE>    Interface to replay packets on.")
		print("<PACKETCAP>    Capture of packets to replay.")
		print("<INJECTCAP>    Capture of packets to inject.")
	else:
		main(sys.argv[1], sys.argv[2], sys.argv[3])
