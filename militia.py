from card import Card
from random import randint


class Militia(Card):
	def effect(self):
		print("Who am I: " + str(self._Card__owner.get_table().get_players().index(self._Card__owner)) + " " + str(self._Card__owner))
		for player in self._Card__owner.get_table().get_players():
			print("player before if: " + str(self._Card__owner.get_table().get_players().index(player)) + " " + str(player))
			if self._Card__owner != player:
				print(str(self._Card__owner) + " " + str(player))
				print("self._Card__owner: " + str(self._Card__owner.get_table().get_players().index(self._Card__owner)))
				print("Player: " + str(self._Card__owner.get_table().get_players().index(player)))
				player.print_hand()
				print("Player " + str(self._Card__owner.get_table().get_players().index(player)) + ", you MUST discard "
				                                                                                   "down to 3 cards.")
				self.__force_discard(self._Card__owner.get_std_chances(), player)

	def __force_discard(self, chances, player):
		if self._Card__owner.get_hand().get_remaining() > 3 and chances > 0:
			hand_index = int(input("\nPlease identify a card from hand you would like to discard by providing "
			                       "its index:  "))

			if 0 > hand_index >= self.__hand.get_remaining() and chances > 0:
				print("Acceptable inputs range from 0 to " + str(self.__hand.get_remaining() - 1) + ".  1 chance lost.")
				self.__force_discard(chances - 1)
			else:
				print("Discarding " + player.get_hand().get_card(hand_index).get_name() + ".")
				player.discard_from_hand(hand_index)
				self.__force_discard(chances, player)
		elif self._Card__owner.get_hand().get_remaining() > 3 and chances < 0:
			print("You're out of chances to select a valid card to discard, randomly selecting for you.")
			player.discard_from_hand(randint(0, self.__hand.get_remaining() - 1))

