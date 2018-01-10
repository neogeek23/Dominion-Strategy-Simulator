from card.card import Card
from math import floor


class Kingdom(Card):
    pile_player_rate = 10

    @staticmethod
    def pile_setup(player_count):
        return (floor(player_count/Card.normal_full_table) + 1) * Card.pile_player_rate
