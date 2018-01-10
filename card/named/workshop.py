from card.basic.card_action import Action
from card.special.card_gain import CardGain


class Workshop(Action, CardGain):
	coin_gain = 4

	def effect(self):
		self.gain_card(self.coin_gain)
