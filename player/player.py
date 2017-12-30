from player.deck import Deck
from player.discard import Discard
from player.hand import Hand
from player.counter import Counter
from card.card import Card


class Player:
	def __init__(self, human, table):
		self.__std_chances = 3
		self.__deck = Deck()
		self.__discard = Discard()
		self.__hand = Hand()
		self.__purchase_power = 0
		self.__actions = Counter(0)
		self.__buys = 0
		self.__is_human = human
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

	def get_player_index(self):
		return self.__table.get_players().index(self)

	def get_score(self):
		return 0

	def draw_card(self):
		self.__deck.transfer_top_card(self.__hand)
		self.__hand.get_top_card().passive()

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

	def play_card(self, acceptable_card_type, chances, counter):
		if chances > 0 and self.__hand.contains_one_of(acceptable_card_type):
			hand_index = int(input("\nPlease identify a card from hand you would like to play by providing its index:  "))

			if hand_index < 0:
				print("You have elected to forfeit any remaining plays.")
				if counter is not None:
					counter.int = 0
			elif hand_index >= self.__hand.get_remaining():
				print("Acceptable inputs range from 0 to " + str(self.__hand.get_remaining() - 1) + ".  1 chance lost.")
				self.play_card(acceptable_card_type, chances - 1, counter)
			elif self.__hand.get_card(hand_index).get_type() in acceptable_card_type:
				card = self.__hand.get_card(hand_index)
				print("Player " + str(self.get_table().get_players().index(self)) + " playing:  " + card.get_name())
				card.play()
				self.__hand.transfer_card_by_card(card, self.__discard)
				if counter is not None:
					counter.int -= 1
				self.__print()
			else:
				print("Index in bounds but not an acceptable card type.  Chance to get it right reduced.")
				self.play_card(acceptable_card_type, chances - 1, counter)
		elif chances <= 0:
			print("You have used up all of your chances to enter a valid integer; forfeiting remaining plays.")
			if counter is not None:
				counter.int = 0
		else:
			print("There are no more acceptable card in hand, moving to next phase.")
			if counter is not None:
				counter.int = 0

	def take_action(self):
		print("\nPlease play an Action, Attack, or Reaction card until you have no remaining actions.")
		while self.__actions.int > 0:
			self.play_card([Card.CardType.Action, Card.CardType.Attack, Card.CardType.Reaction],
			               self.__std_chances, self.__actions)

	def take_buy(self):
		if self.__hand.contains_one_of([Card.CardType.Treasure]):
			print("\nPlease play all Treasure card that you want to play.")

			play_another = Counter(self.__hand.get_card_type_count(Card.CardType.Treasure))
			while play_another.int > 0:
				self.play_card([Card.CardType.Treasure], self.__std_chances, play_another)
		self.buy_card(self.__std_chances)

	def buy_card(self, chances):
		self.__table.print()
		while self.__buys > 0 and not self.__table.are_there_any_empty_piles() and chances > 0:
			pile_index = int(input("\nPlease identify a pile from the table that you'd like to purchase:  "))

			if pile_index < 0:
				print("You have elected to forfeit any remaining plays.")
				self.__buys = 0
			elif pile_index >= self.__table.get_pile_count():
				print("Acceptable inputs range from 0 to " + str(self.__table.get_pile_count() - 1) + ".  Try again.")
				chances -= 1
			elif self.__table.get_pile(pile_index).get_card_group().get_cost() > self.__purchase_power:
				print("You do not have enough coin.  Try again.")
				chances -= 1
			else:
				print("Player " + str(self.get_table().get_players().index(self)) + " buying card " +
				      self.__table.get_pile(pile_index).get_card_group().get_name())
				self.__table.get_pile(pile_index).transfer_top_card(self.__discard)
				self.claim_top_card(self.__discard)
				self.__buys -= 1

	def take_turn(self):
		self.__turn_setup()
		self.__print()
		self.take_action()
		self.take_buy()
		self.discard_remaining_hand()
		self.draw_hand()
		self.print_hand()

	def claim_top_card(self, supply):
		supply.get_top_card().set_owner(self)

	def print_hand(self):
		print("\nPlayer " + str(self.__table.get_players().index(self)) + " Hand:")
		self.__hand.print()

	def __print_discard(self):
		print("\nPlayer " + str(self.__table.get_players().index(self)) + " Discard:")
		self.__discard.print()

	def __print_deck(self):
		print("\nPlayer " + str(self.__table.get_players().index(self)) + " Deck:")
		self.__deck.print()

	def __print(self):
		print("\nPlayer " + str(self.__table.get_players().index(self)) + ":  ")
		print("Actions:  " + str(self.__actions.int))
		print("Buys:  " + str(self.__buys))
		print("Coin:  " + str(self.__purchase_power))
		self.print_hand()
		self.__print_discard()
		self.__print_deck()

	def __turn_setup(self):
		self.__actions.int = 1
		self.__buys = 1
		self.__purchase_power = 0
