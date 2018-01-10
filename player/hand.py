from table.supply import Supply


class Hand(Supply):
	def contains_one_of(self, acceptable_class):
		result = False
		unique_class_instances = self.__get_unique_class_instances()

		for uci in unique_class_instances:
			result |= isinstance(uci, acceptable_class)
		return result

	def get_card_type_count(self, card_class):
		result = 0

		for c in self.get_supply():
			if isinstance(c, card_class):
				result += 1
		return result

	def blocks_attack(self, what_attack):
		yes_no = False
		found_at = -1

		for c in self.get_supply():
			if c.prevent_attack:
				found_at = self.get_supply().index(c)

		if found_at >= 0:
			owner = self.get_supply()[found_at].get_owner()
			yes_no = "Y" == owner.get_general_input("Player " + str(owner.get_player_index()) + ", enter 'Y' if you'd "
			                                        "like to reveal " + self.get_supply()[found_at].get_name() +
													" to block the " + what_attack + " attack:  ", str)
		return yes_no

	def __get_unique_class_instances(self):
		unique_class_instances = list()

		for c in self.get_supply():
			if c not in unique_class_instances:
				unique_class_instances.append(c)
		return unique_class_instances
