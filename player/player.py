from player.deck import Deck
from player.discard import Discard
from player.hand import Hand
from player.counter import Counter
from card.basic.card_treasure import Treasure
from card.basic.card_action import Action
from random import randint


class Player:
	def __init__(self, table):
		self.__std_chances = 3
		self.__deck = Deck()
		self.__discard = Discard()
		self.__hand = Hand()
		self.__purchase_power = 0
		self.__actions = Counter(0)
		self.__buys = 0
		self.__table = table

	def add_actions(self, n):
		self.__actions.int += n

	def add_purchase_power(self, n):
		self.__purchase_power += n

	def add_buys(self, n):
		self.__buys += n

	def get_table(self):
		return self.__table

	def get_std_chances(self):
		return self.__std_chances

	def get_hand(self):
		return self.__hand

	def get_discard(self):
		return self.__discard

	def get_deck(self):
		return self.__deck

	def get_player_index(self):
		return self.__table.get_players().index(self)

	def get_coin(self):
		return self.__purchase_power

	def get_score(self):
		score = 0

		for c in self.__deck.get_supply():
			score += c.get_points()

		for c in self.__hand.get_supply():
			score += c.get_points()

		for c in self.__discard.get_supply():
			score += c.get_points()

		return score

	def draw_card(self):
		self.__deck.transfer_top_card(self.__hand)

	def draw_cards(self, how_many):
		spillover = how_many - self.__deck.get_remaining()
		lacking_cards = spillover - self.__discard.get_remaining()

		if lacking_cards <= 0:
			lacking_cards = 0
		elif lacking_cards == 1:
			print("You are lacking " + str(lacking_cards) + " card.  You cannot draw anymore.")
		else:
			print("You are lacking " + str(lacking_cards) + " card.  You cannot draw anymore.")

		if spillover > 0:
			for i in range(how_many - spillover):
				self.draw_card()

			self.__discard.cycle_card(self.__deck)

			for i in range(spillover - lacking_cards):
				self.draw_card()
		else:
			for i in range(how_many):
				self.draw_card()

	def draw_deck(self, table, deck_setup):
		for ds in deck_setup:
			index = table.get_pile_index_of_card(ds[0])
			for i in range(ds[1]):
				table.get_pile(index).transfer_top_card(self.__deck)
				self.claim_top_card(self.__deck)
		self.__deck.shuffle()

	def draw_hand(self):
		self.draw_cards(5)

	def discard_remaining_hand(self):
		while self.__hand.get_remaining() > 0:
			self.__hand.transfer_top_card(self.__discard)

	def discard_from_hand(self, n):
		self.__hand.transfer_card_by_index(n, self.__discard)

	def claim_top_card(self, supply):
		supply.get_top_card().set_owner(self)

	def print_hand(self):
		print("\nPlayer " + str(self.__table.get_players().index(self)) + " Hand:")
		self.__hand.print()

	def take_turn(self):
		self.__turn_setup()
		self.__print()
		self.take_action()
		self.take_buy()
		self.discard_remaining_hand()
		self.draw_hand()

	# The following two methods are identical under different names so they can be overridden by bot classes later
	def get_play_input(self, message, target_type, card_restriction):
		return self.__get_input(self.__std_chances, target_type, message)

	def get_buy_input(self, message, target_type):
		return self.__get_input(self.__std_chances, target_type, message)

	def get_response_input(self, message, target_type, card_restriction):
		return self.__get_input(self.__std_chances, target_type, message)

	def take_action(self):
		print("\nPlease play an Action card until you have no remaining actions.")
		while self.__actions.int > 0:
			self.play_card(Action, self.__std_chances, self.__actions)

	def take_buy(self):
		if self.__hand.contains_one_of(Treasure):
			print("\nPlease play all Treasure card that you want to play.")

			play_another = Counter(self.__hand.get_card_type_count(Treasure))
			while play_another.int > 0:
				self.play_card(Treasure, self.__std_chances, play_another)
		self.buy_card(self.__std_chances)

	def play_card(self, acceptable_card_class, chances, counter):
		if chances > 0 and self.__hand.contains_one_of(acceptable_card_class):
			hand_index = self.get_play_input("\nPlease identify a card from hand to play by providing its index: ", int,
											 acceptable_card_class)
			self.__check_play_card(hand_index, counter, acceptable_card_class, chances)
		elif chances <= 0:
			print("You have used up all of your chances to enter a valid integer; forfeiting remaining plays.")
			if counter is not None:
				counter.int = 0
		else:
			print("There are no more acceptable card in hand, moving to next phase.")
			if counter is not None:
				counter.int = 0

	def buy_card(self, chances):
		self.__table.print()
		while self.__buys > 0 and not self.__table.are_there_three_empty_piles() and chances > 0:
			pile_index = self.get_buy_input("\nPlease choose a pile from the table that you'd like to purchase:  ", int)

			if pile_index < 0:
				print("You have elected to forfeit any remaining plays.")
				self.__buys = 0
			elif pile_index >= self.__table.get_pile_count():
				print("Acceptable inputs range from 0 to " + str(self.__table.get_pile_count() - 1) + ".")
				chances -= 1
				print("You have " + str(chances) + " chances left to input correctly.")
			elif self.__table.get_pile(pile_index).get_card_group().get_cost() > self.__purchase_power:
				print("You do not have enough coin.")
				chances -= 1
				print("You have " + str(chances) + " chances left to input correctly.")
			else:
				self.__buys -= 1
				self.__purchase_power -= self.__table.get_pile(pile_index).get_card_group().get_cost()
				print("Player " + str(self.get_table().get_players().index(self)) + " buying card " +
				      self.__table.get_pile(pile_index).get_card_group().get_name() + " leaving " +
				      str(self.__purchase_power) + " coin(s) and " + str(self.__buys) + " buy(s) following purchase.")
				self.__table.get_pile(pile_index).transfer_top_card(self.__discard)
				self.claim_top_card(self.__discard)
				chances = self.get_std_chances()

	def __check_play_card(self, hand_index, counter, acceptable_card_class, chances):
		if hand_index < 0:
			print("You have elected to forfeit any remaining plays.")
			if counter is not None:
				counter.int = 0
		elif hand_index >= self.__hand.get_remaining():
			print("Acceptable inputs range from 0 to " + str(self.__hand.get_remaining() - 1) + ".  1 chance lost.")
			self.play_card(acceptable_card_class, chances - 1, counter)
		elif isinstance(self.__hand.get_card(hand_index), acceptable_card_class):
			print("Player " + str(self.get_player_index()) + " playing: " + self.__hand.get_card(hand_index).get_name())
			play_card = self.__hand.get_card(hand_index)
			play_card.play()
			self.__hand.transfer_card_by_card(play_card, self.__discard)
			if counter is not None:
				counter.int -= 1
			self.__print()
		else:
			print("Index in bounds but not an acceptable card type.  Chance to get it right reduced.")
			self.play_card(acceptable_card_class, chances - 1, counter)

	def __get_input(self, chances, target_type, message):
		value = input(message)
		if chances > 0:
			if not self.__does_typecast_error(value, target_type):
				return target_type(value)
			else:
				print("'" + str(value) + "' of type " + str(type(value)) + " is an invalid entry.  " + str(chances) +
				      " chances to input a " + str(target_type) + " remain.")
				return self.__get_input(chances - 1, target_type, message)
		else:
			if target_type == int:
				rand_value = randint(-1, 1)
				print("You've run out of chances to input an int.  A random value of '" + str(rand_value) + "' is being"
				                                                                                        " supplied.")
				return rand_value
			elif target_type == str:
				print("You've run out of chances to input an string.  A zero length string is being supplied.")
				return ""
			else:
				print("You've run out of chances to input a" + str(target_type) + ".  A None is being supplied.")
				return None

	def __does_typecast_error(self, value, target_type):
		try:
			target_type(value)
			return False
		except ValueError:
			return True

	def __print_discard(self):
		self.__discard.print()

	def __print_deck(self):
		print("\nPlayer " + str(self.__table.get_players().index(self)) + " Deck:")
		self.__deck.print()

	def __print(self):
		print("\nPlayer " + str(self.__table.get_players().index(self)) + ":  ")
		print("Actions:  " + str(self.__actions.int))
		print("Buys:  " + str(self.__buys))
		print("Coin:  " + str(self.__purchase_power))
		print("Deck Remaining:  " + str(self.__deck.get_remaining()))
		self.__print_discard()
		self.print_hand()
		print("")

	def __turn_setup(self):
		self.__actions.int = 1
		self.__buys = 1
		self.__purchase_power = 0

	def __str__(self):
		return "Player " + str(self.get_player_index())
