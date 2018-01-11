from table.supply import Supply


class Discard(Supply):
	def cycle_card(self, deck):
		while self.get_remaining() > 0:
			self.transfer_top_card(deck)
		deck.shuffle()

	def print(self):
		if len(self.get_supply()) > 0:
			print("Discard shows " + str(self.get_top_card()) + " face up.")
		else:
			print("Discard is empty.")
