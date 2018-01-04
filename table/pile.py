from table.supply import Supply

class Pile(Supply):
	def __init__(self, card):
		self.__card_group = card
		Supply.__init__(self)

	def get_card_group(self):
		return self.__card_group
