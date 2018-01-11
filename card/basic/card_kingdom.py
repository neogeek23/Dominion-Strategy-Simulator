from card.card import Card
from math import floor


class Kingdom(Card):
    pile_player_rate = 10

    @classmethod
    def pile_setup(cls, player_count):
        return (floor(player_count/cls.normal_full_table) + 1) * cls.pile_player_rate
