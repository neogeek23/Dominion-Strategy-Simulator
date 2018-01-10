from card.card import Card


class Curse(Card):
    @staticmethod
    def pile_setup(player_count):
        if player_count % Card.normal_full_table < Card.normal_full_table/2:
            return Card.pile_player_rate
        else:
            return (player_count - 1) * Card.pile_player_rate
