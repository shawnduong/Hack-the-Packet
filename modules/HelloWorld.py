from scapy.all import conf, IP, UDP

class HelloWorld():
	"""
	13.37.13.37:1337 -> 255.255.255.255:9999
	UDP "Hello World!"
	"""

	def play(s: conf.L2socket):
		"""
		Play the traffic on an L2 socket.
		"""

		message = (
			IP(dst="255.255.255.255", src="13.37.13.37")
			/ UDP(sport=1337, dport=9999)
			/ "Hello World!"
		)

		s.send(message)

