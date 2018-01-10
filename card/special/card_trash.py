from card.card import Card


class CardTrash(Card):
	trashable_type_restriction = None

	def trash_card_get_cost(self):
		tc = self.__get_trashable_cards()
		self.print_card_list(tc, " Trashable Cards:  ")
		index = 0
		bonus = 0
		chances = self.get_owner().get_std_chances()

		while 0 < len(tc) and 0 <= index < len(tc) - 1 and chances > 0:
			index = self.__get_card_to_trash()

			if index < 0 or index >= len(tc):
				print("Acceptable inputs range from 0 to " + str(len(tc) - 1) + ".  1 chance lost.")
				index = 0
				chances -= 1
			else:
				print("Player " + str(self.get_owner().get_player_index()) + " trashing " + tc[index].get_name() + ".")
				bonus = tc[index].get_cost()
				self.get_owner().get_hand().transfer_card_by_card(tc[index], self.get_owner().get_table().get_trash())
				chances = 0
		return bonus

	def trash_card(self):
		self.trash_card_get_cost()

	def __get_card_to_trash(self):
		return self.get_owner().get_general_input("\nPlease identify the index of the desired card to trash:  ", int)

	def __get_trashable_cards(self):
		result = list()

		for c in self.get_owner().get_hand().get_supply():
			if c != self:
				if self.trashable_type_restriction is None:
					result.append(c)
				elif isinstance(c, self.trashable_type_restriction):
					result.append(c)
		return result
