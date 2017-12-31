from card.card_gain import CardGain


class Workshop(CardGain):
	coin_gain = 4

	def effect(self):
		self.gain_card(self.coin_gain)
