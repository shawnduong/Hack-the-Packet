from scapy.all import conf, Ether, IP, UDP

class HelloWorld():
	"""
	13.37.13.37:1337 -> 12.34.56.78:6767
	UDP "Hello World! Welcome to Hack the Packet!"
	"""

	def play(s: conf.L2socket):
		"""
		Play the traffic on an L2 socket.
		"""

		message = (
			Ether()
			/ IP(dst="12.34.56.78", src="13.37.13.37")
			/ UDP(sport=1337, dport=6767)
			/ "Hello World! Welcome to Hack the Packet!"
		)

		s.send(message)

