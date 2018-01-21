from player.player import Player


class Human(Player):
	def __str__(self):
		return "Player " + str(self.get_player_index()) + " (human)"

