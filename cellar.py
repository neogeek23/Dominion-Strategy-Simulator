from card import Card


class Cellar(Card):
	def effect(self):
		hand_index = 0
		cards_discarded = 0
		have_not_run_yet = True
		while self._Card__owner.get_hand().get_remaining() >= 0 and \
				0 <= hand_index < self._Card__owner.get_hand().get_remaining() and \
				(hand_index != self._Card__owner.get_hand().get_supply().index(self) or have_not_run_yet):
			hand_index = int(input("Player " + str(self._Card__owner.get_table().get_players().index(self._Card__owner))
								   + ", input the index from your hand to discard that card and gain an action, or "
									 " input an impossible index to end discard selection:  "))

			if 0 <= hand_index < self._Card__owner.get_hand().get_remaining() and \
					hand_index != self._Card__owner.get_hand().get_supply().index(self):
				self._Card__owner.discard_from_hand(hand_index)
				self._Card__owner.print_hand()
				cards_discarded += 1
				# in case last card is discarded as that will kill loop & set to itself
				hand_index = self.__get_index_not_self()
			have_not_run_yet = False
		self._Card__owner.draw_cards(cards_discarded)


