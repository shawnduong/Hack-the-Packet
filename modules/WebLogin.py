from random import randint, choice
from scapy.all import conf, Ether, IP, TCP

class WebLogin:
	"""
	GET / some web page, then GET /login, then POST login.
	"""

	usernames = None
	passwords = None
	websites  = None

	def __init__(self, usernames, passwords, websites):

		self.usernames = usernames
		self.passwords = passwords
		self.websites  = websites

	def play(self, s: conf.L2socket):
		"""
		Play the traffic on an L2 socket.
		"""

		# Random uniformally generated source and destination MACs.
		srcMAC = "%02X:%02X:%02X:%02X:%02X:%02X" % (
			randint(0, 255), randint(0, 255), randint(0, 255),
			randint(0, 255), randint(0, 255), randint(0, 255)
		)
		dstMAC = "%02X:%02X:%02X:%02X:%02X:%02X" % (
			randint(0, 255), randint(0, 255), randint(0, 255),
			randint(0, 255), randint(0, 255), randint(0, 255)
		)

		# Random uniformally generated source IPs.
		srcIP = "10.%d.%d.%d" % (
			randint(0, 255), randint(0, 255), randint(0, 255)
		)

		# Randomly select a website and username:password from the wordlists.
		target = choice(self.websites)
		username = choice(self.usernames)
		password = choice(self.passwords)

		# GET /
		message = (
			Ether(src=srcMAC, dst=dstMAC)
			/ IP(src=srcIP, dst=target)
			/ TCP(dport=80, sport=randint(1,65535))
			/ f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n"
		)
		s.send(message)

		# GET /login
		message = (
			Ether(src=srcMAC, dst=dstMAC)
			/ IP(src=srcIP, dst=target)
			/ TCP(dport=80, sport=randint(1,65535))
			/ f"GET /login HTTP/1.1\r\nHost: {target}\r\n\r\n"
		)
		s.send(message)

		# POST /login
		message = (
			Ether(src=srcMAC, dst=dstMAC)
			/ IP(src=srcIP, dst=target)
			/ TCP(dport=80, sport=randint(1,65535))
			/ (f"POST /login HTTP/1.1\r\nHost: {target}\r\n\r\n"
			  + "{\"username\": \"%s\", \"password\": \"%s\"}" % (username, password))
		)
		s.send(message)

