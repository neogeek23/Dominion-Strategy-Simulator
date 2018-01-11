from card.special.card_trash import CardTrash
from card.special.card_gain import CardGain


class CardGainTrash(CardTrash, CardGain):
	coin_gain = 0

	def effect(self):
		self.gain_card(self.trash_card_get_cost() + self.coin_gain)
