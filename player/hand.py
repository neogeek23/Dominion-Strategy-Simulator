from table.supply import Supply


class Hand(Supply):
	def contains_one_of(self, acceptible_types):
		result = False
		unique_types = self.__get_unique_types()

		for at in acceptible_types:
			result |= at in unique_types
		return result

	def get_card_type_count(self, card_type):
		result = 0

		for c in self._Supply__card:
			if c.get_type() == card_type:
				result += 1
		return result

	def blocks_attack(self, what_attack):
		yes_no = False
		found_at = -1

		for c in self._Supply__card:
			if c.prevent_attack:
				found_at = self._Supply__card.index(c)

		if found_at >= 0:
			owner = self._Supply__card[found_at].get_owner()
			yes_no = "Y" == owner.get_general_input("Player " + str(owner.get_player_index()) + ", enter 'Y' if you'd "
			                                                                                    "like to reveal "
			                                        + self._Supply__card[found_at].get_name() + " to block the "
			                                        + what_attack + " attack:  ", str)
		return yes_no

	def __get_unique_types(self):
		unique_type = list()

		for c in self._Supply__card:
			current_type = c.get_type()
			if not current_type in unique_type:
				unique_type.append(current_type)
		return unique_type
