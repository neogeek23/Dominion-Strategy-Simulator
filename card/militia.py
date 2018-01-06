from card.card import Card
from random import randint


class Militia(Card):
	def effect(self):
		for player in self._Card__owner.get_table().get_players():
			if self._Card__owner != player and not player.get_hand().blocks_attack(self.get_name()):
				player.print_hand()
				print("Player " + str(player.get_player_index()) + ", you MUST discard down to 3 card.")
				self.__force_discard(self._Card__owner.get_std_chances(), player)

	def __force_discard(self, chances, player):
		if player.get_hand().get_remaining() > 3 and chances > 0:
			hand_index = player.militia_input("\nPlease provide an index to identify a card from hand you would like to"
											  " discard (0 to " + str(player.get_hand().get_remaining() - 1) + "):  "
			                                  , int)
			self.__check_discard(hand_index, player, chances)
		elif self._Card__owner.get_hand().get_remaining() > 3 and chances <= 0:
			print("You're out of chances to select a valid card to discard, randomly selecting for you.")
			player.discard_from_hand(randint(0, self.__hand.get_remaining() - 1))

	def __check_discard(self, index, player, chances):
		if 0 > index or index >= self._Card__owner.get_hand().get_remaining():
			print("Valid inputs range from 0 to " + str(player.get_hand().get_remaining() - 1) + ".  1 chance lost.")
			self.__force_discard(chances - 1, player)
		else:
			print("Discarding " + player.get_hand().get_card(index).get_name() + ".")
			player.discard_from_hand(index)
			player.print_hand()
			self.__force_discard(self._Card__owner.get_std_chances(), player)
