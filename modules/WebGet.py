from random import randint, choice
from scapy.all import conf, Ether, IP, TCP

class WebGet:
	"""
	GET / some web page.
	"""

	websites = None

	def __init__(self, websites):
		self.websites = websites

	def play(self, s: conf.L2socket):
		"""
		Play the traffic on an L2 socket.
		"""

		srcMAC = "%02X:%02X:%02X:%02X:%02X:%02X" % (
			randint(0, 255), randint(0, 255), randint(0, 255),
			randint(0, 255), randint(0, 255), randint(0, 255)
		)
		dstMAC = "%02X:%02X:%02X:%02X:%02X:%02X" % (
			randint(0, 255), randint(0, 255), randint(0, 255),
			randint(0, 255), randint(0, 255), randint(0, 255)
		)
		srcIP = "10.%d.%d.%d" % (
			randint(0, 255), randint(0, 255), randint(0, 255)
		)
		target = choice(self.websites)

		message = (
			Ether(src=srcMAC, dst=dstMAC)
			/ IP(src=srcIP, dst=target)
			/ TCP(dport=80, sport=randint(1,65535))
			/ f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n"
		)

		s.send(message)

