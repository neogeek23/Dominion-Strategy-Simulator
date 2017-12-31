from card.card import Card
from card.card_gain_trash import CardGainTrash


class Mine(CardGainTrash):
	coin_gain = 3
	trashable_type_restriction = [Card.CardType.Treasure]
	gainable_type_restriction = [Card.CardType.Treasure]
