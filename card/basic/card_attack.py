from card.basic.card_kingdom import Kingdom


class Attack(Kingdom):
    def effect(self):
        for player in self.get_owner().get_table().get_players():
            if self.get_owner() != player and not player.get_hand().reaction_blocks_attack(self.get_name()):
                self.attack(player)

    def attack(self, player):
        pass
