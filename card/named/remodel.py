from card.basic.card_action import Action
from card.special.card_gain_trash import CardGainTrash


class Remodel(Action, CardGainTrash):
	coin_gain = 2
