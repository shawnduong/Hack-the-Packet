from scapy.all import conf
import random

from modules.HelloWorld import HelloWorld

class Loot:
	"""
	Wrapper over all Loot types.
	"""

	def play(s: conf.L2socket):

		random.choice([
			HelloWorld.play
		])(s)

