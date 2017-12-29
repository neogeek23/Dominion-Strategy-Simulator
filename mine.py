from card import Card


class Mine(Card):
	def effect(self):
		treasure_cards = self.__get_Treasures()
		self.__print_Treasures(treasure_cards)
		trash_card = 0
		chances = self._Card__owner.get_std_chances()

		while len(treasure_cards) > 0 and 0 <= trash_card < len(treasure_cards) - 1 and chances > 0:
			trash_card = int(input("\nPlayer " + str(self._Card__owner.get_table()
													 .get_players().index(self._Card__owner))
							   + ", input the index of the treasure card you want to trash to gain another treasure "
								 "card from the table's piles that costs up to 3 coins more than the trashed card:  "))

			if trash_card < 0 or trash_card >= len(treasure_cards):
				print("Acceptable inputs range from 0 to " + str(len(treasure_cards) - 1) + ".  1 chance lost.")
				trash_card = 0
				chances -= 1
			else:
				print("Player " + str(self._Card__owner.get_table().get_players().index(self._Card__owner))
									  + " trashing " + treasure_cards[trash_card].get_name() + ".")
				self.__gain_treasure(treasure_cards[trash_card].get_cost() + 3)
				self._Card__owner.get_hand().transfer_card_by_card(treasure_cards[trash_card],
																   self._Card__owner.get_table().get_trash())
				self._Card__owner.claim_top_card(self._Card__owner.get_hand())
				# self._Card__owner.get
				chances = 0

	def __gain_treasure(self, spending_limit):
		treasures_I_can_buy = self.__get_affordable_treasures(spending_limit)
		self.__print_affordable_treasures(treasures_I_can_buy)
		buy_card = 0
		chances = self._Card__owner.get_std_chances()

		while len(treasures_I_can_buy) > 0 and 0 <= buy_card < len(treasures_I_can_buy) - 1 and chances > 0:
			buy_card = int(input("\nPlease identify the index of which treasure you would like to obtain:  "))

			if buy_card < 0 or buy_card >= len(treasures_I_can_buy):
				print("Acceptable inputs range from 0 to " + str(len(treasures_I_can_buy) - 1) + ".  1 chance lost.")
				buy_card = 0
				chances -= 1
			else:
				pile_index = self._Card__owner.get_table().get_piles().index(treasures_I_can_buy[buy_card])
				print("Player " + str(self._Card__owner.get_table().get_players().index(self._Card__owner))
					  + " drawing " + self._Card__owner.get_table().get_pile(pile_index).get_card_group().get_name()
					  + " to hand.")
				self._Card__owner.get_table().get_pile(pile_index).transfer_top_card(self._Card__owner.get_hand())

	def __print_affordable_treasures(self, affordable_treasure):
		print("\nPlayer " + str(self._Card__owner.get_table().get_players().index(self._Card__owner))
							  + " Affordable Treasures:  ")
		counter = 0
		for t in affordable_treasure:
			print(str(counter) + ":  " + t.get_card_group().identify())
			counter += 1

	def __get_affordable_treasures(self, spending_limit):
		result = list()

		for p in self._Card__owner.get_table().get_piles():
			if p.get_card_group().get_cost() <= spending_limit \
					and p.get_card_group().get_type() == Card.CardType.Treasure:
				result.append(p)
		return result

	def __get_Treasures(self):
		result = list()
		for c in self._Card__owner.get_hand().get_supply():
			if c.get_type() == Card.CardType.Treasure:
				result.append(c)
		return result

	def __print_Treasures(self, Treasure):
		print("\nPlayer " + str(self._Card__owner.get_table().get_players().index(self._Card__owner)) + " Treasures:")
		index = 0
		for c in Treasure:
			print(str(index) + ":  " + c.identify())
			index += 1

