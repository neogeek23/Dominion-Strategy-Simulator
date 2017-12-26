from supply import Supply


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

	def __get_unique_types(self):
		unique_type = list()

		for c in self._Supply__card:
			current_type = c.get_type()
			if not current_type in unique_type:
				unique_type.append(current_type)
		return unique_type