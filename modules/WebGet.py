import random
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

		srcIP = "10.%d.%d.%d" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
		target = random.choice(self.websites)

		message = (
			Ether(src="aa:bb:cc:dd:ee:ff", dst="11:22:33:44:55:66")
			/ IP(src=srcIP, dst=target)
			/ TCP(dport=80, sport=random.randint(1,65535))
			/ f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n"
		)

		s.send(message)

