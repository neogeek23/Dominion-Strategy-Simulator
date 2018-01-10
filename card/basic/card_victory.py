from card.card import Card
from math import floor


class Victory(Card):
	two_player_count = 8
	four_player_count = 12
	five_player_count = 15
	six_player_count = 18

	@classmethod
	def pile_setup(cls, player_count):
		if 0 < player_count % Card.normal_full_table < Card.normal_full_table/2:
			supplement = cls.two_player_count
		elif Card.normal_full_table/2 <= player_count % Card.normal_full_table < Card.normal_full_table - 1:
			supplement = cls.four_player_count
		elif player_count % Card.normal_full_table == Card.normal_full_table - 1:
			supplement = cls.five_player_count
		else:
			supplement = cls.six_player_count
		return (floor(player_count/Card.normal_full_table) * cls.six_player_count) + supplement
