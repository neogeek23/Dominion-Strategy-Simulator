from supply import Supply
from random import shuffle


class Deck(Supply):
	def shuffle(self):
		shuffle(self._Supply__card)
