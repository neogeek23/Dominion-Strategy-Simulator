from player.player import Player
from card.basic.card_treasure import Treasure


class Pure_Big_Money(Player):
	def take_action(self):
		print("\nAs a BIG MONEY BOT, I'm skipping this unnecessary action phase.  Beep-boop, bow to me humans!")

	#This method will only be called for this bot when it is time to play treasures, it will play all of them always.
	def get_play_input(self, message, target_type):
		choice = -1
		hand = self.get_hand().get_supply()

		for c in hand:
			if isinstance(c, Treasure):
				choice = hand.index(c)

		print(message + str(choice))
		return choice

	#This method will only be called when it is time to buy things, a very simple logic will decide its action.
	def get_buy_input(self, message, target_type):
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

	#This will pick either the first or the first least effective purchasing card as this bot doesn't care about that
	def militia_input(self, message, target_type):
		choice = self.__get_first_non_Treasure()
		min_coin = self.get_hand().get_supply()[choice].get_purchase_power()

		for c in self.get_hand().get_supply():
			# We want to do isinstance rather than not isinstance because we only want to evaluate this loop when we are
			# evaluating an all treasure card hand as at that point the choice will be a treasure card, otherwise the
			# choice will already be non-treasure and we don't need to check anything since this bot doesn't do action
			if c.get_purchase_power() < min_coin and isinstance(c, Treasure):
				min_coin = c.get_purchase_power()
				choice = self.get_hand().get_supply().index(c)

		print(message + str(choice))
		return choice

	def __get_first_non_Treasure(self):
		for c in self.get_hand().get_supply():
			if not isinstance(c, Treasure):
				return self.get_hand().get_supply().index(c)
		return 0

	def __str__(self):
		return "Player " + str(self.get_player_index()) + " (pure big money bot)"
