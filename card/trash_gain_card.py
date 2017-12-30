from card.card import Card


class TrashGainEffectCard(Card):
	coin_gain = 0
	trashable_type_restriction = None
	gainable_type_restriction = None

	def effect(self):
		tc = self.__get_trashable_cards()
		self._Card__print_card_list(tc, " Trashable Cards:  ")
		index = 0
		chances = self._Card__owner.get_std_chances()

		while 0 < len(tc) and 0 <= index < len(tc) - 1 and chances > 0:
			index = self.__get_card_to_trash()

			if index < 0 or index >= len(tc):
				print("Acceptable inputs range from 0 to " + str(len(tc) - 1) + ".  1 chance lost.")
				index = 0
				chances -= 1
			else:
				print("Player " + str(self._Card__owner.get_player_index()) + " trashing " + tc[index].get_name() + ".")
				self.__gain_card(tc[index].get_cost() + self.coin_gain)
				self._Card__owner.get_hand().transfer_card_by_card(tc[index], self._Card__owner.get_table().get_trash())
				chances = 0

	def __get_card_to_trash(self):
		return int(input("\nPlease identify the index of the desired card to trash:  "))

	def __get_gain_card(self):
		return int(input("\nPlease identify the index of which card you would like to obtain:  "))

	def __gain_card(self, spending_limit):
		gainable_cards = self.__get_gainable_cards(spending_limit)
		self._Card__print_card_list(gainable_cards, "Gainable Cards:  ")
		index = 0
		chances = self._Card__owner.get_std_chances()

		while len(gainable_cards) > 0 and 0 <= index < len(gainable_cards) - 1 and chances > 0:
			index = self.__get_gain_card()

			if 0 > index >= len(gainable_cards):
				print("Acceptable inputs range from 0 to " + str(len(gainable_cards) - 1) + ".  1 chance lost.")
				index = 0
				chances -= 1
			else:
				pile_index = self._Card__owner.get_table().get_pile_index_of_card(gainable_cards[index].get_name())
				print("Player " + str(self._Card__owner.get_player_index()) + " drawing "
					  + self._Card__owner.get_table().get_pile(pile_index).get_card_group().get_name() + " to hand.")
				self._Card__owner.get_table().get_pile(pile_index).transfer_top_card(self._Card__owner.get_hand())
				self._Card__owner.claim_top_card(self._Card__owner.get_hand())
				chances = 0

	def __get_gainable_cards(self, spending_limit):
		result = list()

		for p in self._Card__owner.get_table().get_piles():
			if p.get_card_group().get_cost() <= spending_limit:
				if self.gainable_type_restriction is None:
					result.append(p.get_card_group())
				elif p.get_card_group().get_type() in self.gainable_type_restriction:
					result.append(p.get_card_group())
		return result

	def __get_trashable_cards(self):
		result = list()

		for c in self._Card__owner.get_hand().get_supply():
			# print(c)
			# print(self)
			# print(c.get_type())
			# print(self.trashable_type_restriction)
			if c != self:
				if self.trashable_type_restriction is None:
					result.append(c)
				elif c.get_type() in self.trashable_type_restriction:
					result.append(c)
		return result
