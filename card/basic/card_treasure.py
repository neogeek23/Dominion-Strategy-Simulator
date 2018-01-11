from card.card import Card
from math import floor


class Treasure(Card):
    @classmethod
    def pile_setup(cls, player_count):
        return (floor(player_count/cls.normal_full_table) + 1) * cls.pile_player_rate
