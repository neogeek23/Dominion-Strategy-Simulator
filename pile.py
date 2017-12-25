from supply import Supply

class Pile(Supply):
	def get_card_group(self):
		return self._Supply__card[0]
