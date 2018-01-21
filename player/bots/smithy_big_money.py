from player.bot import Bot


class Smithy_Big_Money(Bot):
	target_card = "Smithy"
	target_card_threshold = 5

	def __str__(self):
		return "Player " + str(self.get_player_index()) + " (smithy big money bot)"