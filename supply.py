class Supply:
	def __init__(self):
		self.__card = list()

	def add_card(self, card):
		self.__card.append(card)

	def add_cards(self, card, n):
		for i in range(n):
			self.add_card(card)

	def get_supply(self):
		return self.__card

	def transfer_top_card(self, recipient_supply):
		self.transfer_card(len(self.__card) - 1, recipient_supply)

	def transfer_card(self, n, recipient_supply):
		transfer_card = self.__card.pop(n)
		recipient_supply.add_card(transfer_card)

	def get_card(self, n):
		return self.__card[n]

	def get_remaining(self):
		return len(self.__card)

	def print(self):
		for c in self.__card:
			print(c.identify())
