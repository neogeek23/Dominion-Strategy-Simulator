from card.basic.card_action import Action
from card.basic.card_treasure import Treasure
from card.special.card_gain_trash import CardGainTrash


class Mine(Action, CardGainTrash):
	coin_gain = 3
	trashable_type_restriction = Treasure
	gainable_type_restriction = Treasure
