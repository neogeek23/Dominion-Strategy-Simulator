from player.player import Player
from card.card import Card


class Bot(Player):
	def take_action(self):
		print("\nAs a BIG MONEY BOT, I'm skipping this unnecessary action phase.  Beep-boop, bow to me humans!")

	#This method will only be called for this bot when it is time to play treasures, it will play all of them always.
	def get_play_input(self, message):
		choice = -1
		hand = self.get_hand().get_supply()

		for c in hand:
			if c.get_type() == Card.CardType.Treasure:
				choice = hand.index(c)

		print(message + str(choice))
		return choice

	#This method will only be called when it is time to buy things, a very simple logic will decide its action.
	def get_buy_input(self, message):
		coin = self._Player__purchase_power
		choice = -1

		if coin >= 8:
			choice = self.get_table().get_pile_index_of_card("Province")
		elif coin >= 6:
			choice = self.get_table().get_pile_index_of_card("Gold")
		elif coin >= 3:
			choice = self.get_table().get_pile_index_of_card("Silver")

		print(message + str(choice))
		return choice
