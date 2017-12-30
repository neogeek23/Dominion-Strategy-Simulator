from card.card import Card
from random import randint


class Militia(Card):
	def effect(self):
		for player in self._Card__owner.get_table().get_players():
			if self._Card__owner != player and not player.get_hand().blocks_attack(self.get_name()):
				player.print_hand()
				print("Player " + str(self._Card__owner.get_table().get_players().index(player)) + ", you MUST discard "
				                                                                                   "down to 3 card.")
				self.__force_discard(self._Card__owner.get_std_chances(), player)

	def __force_discard(self, chances, player):
		if player.get_hand().get_remaining() > 3 and chances > 0:
			hand_index = int(input("\nPlease identify a card from hand you would like to discard by providing "
			                       "its index 0 to " + str(player.get_hand().get_remaining() - 1) + ":  "))

			if chances <= 0:
				print("Somehow chances ran out, you'll randomly discard a card now.")
				self.__force_discard(chances, player)
			elif 0 > hand_index or hand_index >= self._Card__owner.get_hand().get_remaining():
				print("Acceptable inputs range from 0 to " + str(player.get_hand().get_remaining() - 1) +
				      ".  1 chance lost.")
				self.__force_discard(chances - 1, player)
			else:
				print("Discarding " + player.get_hand().get_card(hand_index).get_name() + ".")
				player.discard_from_hand(hand_index)
				player.print_hand()
				self.__force_discard(chances, player)
		elif self._Card__owner.get_hand().get_remaining() > 3 and chances < 0:
			print("You're out of chances to select a valid card to discard, randomly selecting for you.")
			player.discard_from_hand(randint(0, self.__hand.get_remaining() - 1))

