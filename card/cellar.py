from card.card import Card


class Cellar(Card):
	def effect(self):
		hand_index = 0
		cards_discarded = 0
		have_not_run_yet = True
		while self._Card__owner.get_hand().get_remaining() >= 0 and \
				0 <= hand_index < self._Card__owner.get_hand().get_remaining() and \
				(hand_index != self._Card__owner.get_hand().get_supply().index(self) or have_not_run_yet):
			hand_index = self.__get_index("Player " + str(self._Card__owner.get_player_index()) + ", input the index "
										  "from your hand to discard that card and gain an action, or  input an "
										  "impossible index to end discard selection:  ")

			if 0 <= hand_index < self._Card__owner.get_hand().get_remaining() and \
					hand_index != self._Card__owner.get_hand().get_supply().index(self):
				self._Card__owner.discard_from_hand(hand_index)
				self._Card__owner.print_hand()
				cards_discarded += 1
				hand_index = self.__get_index_not_self()
			have_not_run_yet = False
		self._Card__owner.draw_cards(cards_discarded)

	def __get_index(self, message):
		return self.__Card_owner.get_general_input(message, int)

