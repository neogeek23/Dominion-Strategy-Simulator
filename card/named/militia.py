from card.basic.card_attack import Attack
from card.basic.card_action import Action
from random import randint


class Militia(Action, Attack):
	def attack(self, player):
		player.print_hand()
		print("Player " + str(player.get_player_index()) + ", you MUST discard down to 3 card.")
		self.__force_discard(self.get_owner().get_std_chances(), player)

	def __force_discard(self, chances, player):
		if player.get_hand().get_remaining() > 3 and chances > 0:
			hand_index = player.get_response_input("\nPlease provide an index to identify a card from hand you would "
												"like to discard (0 to " + str(player.get_hand().get_remaining() - 1)
												+ "):  ", int, self.__class__)
			self.__check_discard(hand_index, player, chances)
		elif self.get_owner().get_hand().get_remaining() > 3 and chances <= 0:
			print("You're out of chances to select a valid card to discard, randomly selecting for you.")
			player.discard_from_hand(randint(0, self.get_owner().get_hand().get_remaining() - 1))

	def __check_discard(self, index, player, chances):
		if 0 > index >= player.get_hand().get_remaining():
			print("Valid inputs range from 0 to " + str(player.get_hand().get_remaining() - 1) + ". " + str(chances - 1)
			      + "chances to input a valid index.")
			self.__force_discard(chances - 1, player)
		else:
			print("Discarding " + player.get_hand().get_card(index).get_name() + ".")
			player.discard_from_hand(index)
			player.print_hand()
			self.__force_discard(self.get_owner().get_std_chances(), player)
