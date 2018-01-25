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

	def reaction_blocks_attack(self, what_attack):
		attack_blocked = False
		for c in self.get_supply():
			attack_blocked |= c.react(what_attack)
			if attack_blocked:
				print(str(c.get_owner()) + " has " + str(c) + " as the " + str(self.get_supply().index(c)) +
					  ' and blocked the ' + what_attack + " attack.")
				return True
		return False

	def __get_unique_class_instances(self):
		unique_class_instances = list()

		for c in self.get_supply():
			if c not in unique_class_instances:
				unique_class_instances.append(c)
		return unique_class_instances
