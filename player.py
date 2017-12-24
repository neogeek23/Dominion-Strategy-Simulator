from deck import Deck
from discard import Discard
from hand import Hand
from card import Card
from counter import Counter


class Player:
	def __init__(self, human, table):
		self.__deck = Deck()
		self.__discard = Discard()
		self.__hand = Hand()
		self.__purchase_power = 0
		self.__actions = Counter(0)
		self.__buys = 0
		self.__draws = 0
		self.__reactions = Counter(0)
		self.__is_human = human
		self.__table = table

	def add_actions(self, n):
		self.__actions.int += n

	def add_purchase_power(self, n):
		self.__purchase_power += n

	def add_buys(self, n):
		self.__buys += n

	def add_draws(self, n):
		self.__draws += n

	def add_reactions(self, n):
		self.__reactions.int += n

	def get_score(self):
		return 0

	def draw_card(self):
		self.__deck.transfer_top_card(self.__hand)

	def draw_cards(self, how_many):
		spillover = how_many - self.__deck.get_remaining()

		if spillover > 0:
			for i in range(how_many - spillover):
				self.draw_card()

			self.__discard.cycle_card(self.__deck)

			for i in range(spillover):
				self.draw_card()
		else:
			for i in range(how_many):
				self.draw_card()

	def draw_deck(self, table, deck_setup):
		for ds in deck_setup:
			index = table.get_pile_index_of_card(ds[0])
			for i in range(ds[1]):
				table.get_pile(index).transfer_top_card(self.__deck)
		self.__deck.shuffle()

	def draw_hand(self):
		self.draw_cards(5)

	def discard_remaining_hand(self):
		while self.__hand.get_remaining() > 0:
			self.__hand.transfer_top_card(self.__discard)

	def __print_hand(self):
		print("Hand:")
		self.__hand.print()

	def __print_discard(self):
		print("Discard:")
		self.__discard.print()

	def __print_deck(self):
		print("Deck")
		self.__deck.print()

	def __gain_turn_events(self):
		self.add_actions(1)
		self.add_buys(1)

	def play_card(self, acceptable_card_type, chances, counter):
		if chances > 0 and self.__hand.contains_one_of(acceptable_card_type):
			hand_index = int(input("Please identify a card from hand you would like to play by providing its index:  "))

			if self.__hand.get_card(hand_index).get_type() in acceptable_card_type:
				self.__hand.get_card(hand_index).play(self)
				self.__hand.transfer_card(hand_index, self.__discard)
				if counter is not None:
					counter.int -= 1
			elif hand_index < 0:
				print("You have elected to forfeit any remaining plays.")
				if counter is not None:
					counter.int = 0
			else:
				self.play_card(acceptable_card_type, chances - 1, counter)
		elif chances <= 0:
			print("You have used up all of your chances to enter a positive integer; forfeiting remaining plays.")
		else:
			print("There are no more acceptable cards in hand, moving to next phase.")
			if counter is not None:
				counter.int = 0

	def take_action(self):
		print("Please play an Action, Attack, or Reaction card until you have no remaining actions.")
		while self.__actions.int > 0:
			self.play_card([Card.CardType.Action, Card.CardType.Attack, Card.CardType.Reaction], 3, self.__actions)

	def give_reaction(self):
		pass

	def take_reaction(self):
		pass

	def take_buy(self):
		print("Please play all Treasure cards that you want to play.")

		play_another = Counter(self.__hand.get_card_type_count(Card.CardType.Treasure))
		while play_another.int > 0:
			self.play_card([Card.CardType.Treasure], 3, play_another)
		self.buy_card()

	def buy_card(self):
		while self.__buys > 0 and not self.__table.are_there_any_empty_piles():
			pile_index = int(input("Please identify a pile from the table that you'd like to purchase:  "))
			self.__table.get_pile(pile_index).transfer_top_card(self.__discard)
			self.__buys -= 1

	def take_turn(self):
		print("Deck Size:  " + str(self.__deck.get_remaining()))
		self.__print_hand()
		self.__gain_turn_events()
		self.take_action()
		self.__print_discard()
		self.__print_deck()
		# self.give_reaction()
		self.take_buy()
		# self.discard_remaining_hand()
		# self.draw_hand()
		# self.__print_hand()