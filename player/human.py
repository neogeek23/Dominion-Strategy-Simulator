from player.player import Player


class Human(Player):
	def __str__(self):
		return "Player " + str(self.get_player_index()) + " (human)"

	def militia_input(self, message, target_type):
		return self.get_general_input(message, target_type)
