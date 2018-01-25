from player.player import Player
from card.basic.card_action import Action
from card.basic.card_treasure import Treasure
from card.named.militia import Militia


class Bot(Player):
	target_card = None
	target_card_threshold = 0

	def get_play_input(self, message, target_type, restriction):
		if restriction == Treasure:
			choice = self.get_subclass_input(Treasure)
		elif restriction == Action:
			choice = self.get_subclass_input(Action)
		else:
			choice = -1

		print(message + str(choice))
		return choice

	def get_response_input(self, message, target_type, restriction):
		if restriction == Militia:
			choice = self.get_militia_input()
		else:
			choice = -1
		return choice

	def can_afford_on_avg(self, card_name):
		card_cost = self.get_table().get_piles()[self.get_table().get_pile_index_of_card(card_name)].get_card_group()\
			.get_cost()
		total_coin = 0
		hand = self.get_hand().get_supply()
		deck = self.get_deck().get_supply()
		discard = self.get_discard().get_supply()
		supplies = hand + deck + discard

		for c in supplies:
			total_coin += c.get_purchase_power()
		return card_cost <= total_coin/(len(hand) + len(deck) + len(discard))

	def has_how_many_of_card(self, card_name):
		total = 0
		hand = self.get_hand().get_supply()
		deck = self.get_deck().get_supply()
		discard = self.get_discard().get_supply()
		supplies = hand + deck + discard

		for c in supplies:
			if c.get_name() == card_name:
				total += 1
		return total

	#This will pick either the first or the first least effective purchasing card as this bot doesn't care about that
	def get_militia_input(self):
		choice = self.__get_first_non_Treasure()
		min_coin = self.get_hand().get_supply()[choice].get_purchase_power()

		for c in self.get_hand().get_supply():
			# We want to do isinstance rather than not isinstance because we only want to evaluate this loop when we are
			# evaluating an all treasure card hand as at that point the choice will be a treasure card, otherwise the
			# choice will already be non-treasure and we don't need to check anything since this bot doesn't do action
			if c.get_purchase_power() < min_coin and isinstance(c, Treasure):
				min_coin = c.get_purchase_power()
				choice = self.get_hand().get_supply().index(c)
		return choice

	# This method will only be called when it is time to buy things, a very simple logic will decide its action.
	def get_buy_input(self, message, target_type):
		coin = self.get_coin()
		choice = -1

		if coin >= self.target_card_threshold and not self.get_table().pile_is_empty(self.target_card) and \
				self.has_how_many_of_card(self.target_card) < 3:
			choice = self.get_table().get_pile_index_of_card(self.target_card)
		elif coin >= 8 and not self.get_table().pile_is_empty("Province"):
			choice = self.get_table().get_pile_index_of_card("Province")
		elif coin >= 8 and not self.get_table().pile_is_empty("Dutchy"):
			choice = self.get_table().get_pile_index_of_card("Dutchy")
		elif coin >= 6 and not self.get_table().pile_is_empty("Gold") and not \
				self.get_table().pile_is_empty("Province"):
			choice = self.get_table().get_pile_index_of_card("Gold")
		elif coin >= 5 and not self.get_table().pile_is_empty("Dutchy") and \
				(self.can_afford_on_avg("Province") or self.get_table().pile_is_empty("Province")):
			choice = self.get_table().get_pile_index_of_card("Dutchy")
		elif coin >= 3 and not self.get_table().pile_is_empty("Silver"):
			choice = self.get_table().get_pile_index_of_card("Silver")

		print(message + str(choice))
		return choice

	def get_subclass_input(self, subclass):
		choice = -1
		hand = self.get_hand().get_supply()

		for c in hand:
			if isinstance(c, subclass):
				choice = hand.index(c)
		return choice

	def __get_first_non_Treasure(self):
		for c in self.get_hand().get_supply():
			if not isinstance(c, Treasure):
				return self.get_hand().get_supply().index(c)
		return 0