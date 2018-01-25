from player.bot import Bot


class Militia_Big_Money(Bot):
	target_card = "Militia"
	target_card_threshold = 4

	def __str__(self):
		return "Player " + str(self.get_player_index()) + " (militia big money bot)"