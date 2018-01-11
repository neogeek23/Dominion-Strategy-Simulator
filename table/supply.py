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

	def get_index_of_card_by_name(self, name):
		for c in self.__card:
			if c.get_name() == name:
				return self.__card.index(c)
		return -1

	def get_index_of_card_by_card(self, card):
		for c in self.__card:
			if c == card:
				return self.__card.index(c)
		return -1

	def transfer_top_card(self, recipient_supply):
		self.transfer_card_by_index(len(self.__card) - 1, recipient_supply)

	def transfer_card_by_index(self, n, recipient_supply):
		transfer_card = self.__card.pop(n)
		recipient_supply.add_card(transfer_card)

	def transfer_card_by_card(self, card, recipient_supply):
		card_index = self.get_index_of_card_by_card(card)

		if card_index >= 0:
			self.transfer_card_by_index(card_index, recipient_supply)
		else:
			raise ValueError('Card not found in hand during attempt to transfer card.')

	def get_card(self, n):
		return self.__card[n]

	def get_top_card(self):
		if len(self.__card) > 0:
			return self.__card[len(self.__card) - 1]

	def get_remaining(self):
		return len(self.__card)

	def print(self):
		index = 0
		for c in self.__card:
			print(str(index) + ":  " + c.identify())
			index += 1

	def __str__(self):
		return "A " + type(self).__name__ + " with " + str(len(self.__card)) + " cards."
