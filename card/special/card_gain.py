from card.card import Card


class CardGain(Card):
	gainable_type_restriction = None

	def gain_card(self, spending_limit):
		gainable_cards = self.__get_gainable_cards(spending_limit)
		self.print_card_list(gainable_cards, "Gainable Cards:  ")
		index = 0
		chances = self.get_owner().get_std_chances()

		while len(gainable_cards) > 0 and 0 <= index < len(gainable_cards) - 1 and chances > 0:
			index = self.__get_gain_card()

			if 0 > index >= len(gainable_cards):
				print("Acceptable inputs range from 0 to " + str(len(gainable_cards) - 1) + ".  1 chance lost.")
				index = 0
				chances -= 1
			else:
				pile_index = self.get_owner().get_table().get_pile_index_of_card(gainable_cards[index].get_name())
				print("Player " + str(self.get_owner().get_player_index()) + " drawing "
					  + self.get_owner().get_table().get_pile(pile_index).get_card_group().get_name() + " to hand.")
				self.get_owner().get_table().get_pile(pile_index).transfer_top_card(self.get_owner().get_hand())
				self.get_owner().claim_top_card(self.get_owner().get_hand())
				chances = 0

	def __get_gain_card(self):
		return self.get_owner().get_general_input("\nPlease identify the index of which card you would like to "
		                                           "obtain:  ", int)

	def __get_gainable_cards(self, spending_limit):
		result = list()

		for p in self.get_owner().get_table().get_piles():
			if p.get_card_group().get_cost() <= spending_limit:
				if self.gainable_type_restriction is None:
					result.append(p.get_card_group())
				elif isinstance(p.get_card_group(), self.gainable_type_restriction):
					result.append(p.get_card_group())
		return result
