from card.basic.card_victory import Victory


class Curse(Victory):
    @classmethod
    def pile_setup(cls, player_count):
        if player_count % cls.normal_full_table < cls.normal_full_table/2:
            return Victory.pile_player_rate
        else:
            return (player_count - 1) * cls.pile_player_rate
