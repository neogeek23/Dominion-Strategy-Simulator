from player.bot import Bot


class Pure_Big_Money(Bot):
	target_card = "Province"
	target_card_threshold = 8

	def take_action(self):
		print("\nAs a BIG MONEY BOT, I'm skipping this unnecessary action phase.  Beep-boop, bow to me humans!")

	def __str__(self):
		return "Player " + str(self.get_player_index()) + " (pure big money bot)"
