from card.card import Card


class Merchant(Card):
	def effect(self):
		silver_card_index = self._Card__owner.get_hand().get_index_of_card_by_name("Silver")
		if silver_card_index >= 0:
			yes_no = self.__get_Merchant_input("'Y' if you'd like to play a silver card and gain an extra coin:  ")

			if yes_no:
				self._Card__owner.get_hand().transfer_card_by_card(
					self._Card__owner.get_hand().get_card(silver_card_index), self._Card__owner.get_discard())
				self._Card__owner.add_purchase_power(3)

	def __get_Merchant_input(self, message):
		return self.__Card_owner.get_general_input("Player " + str(self._Card__owner.get_player_index()) + ", " +
												   message, str)
