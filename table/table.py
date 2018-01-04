from table.trash import Trash
from table.pile import Pile


class Table:
	def __init__(self):
		self.__player = list()
		self.__pile = list()
		self.__trash = Trash()
		self.__winner = None
		self.__winning_score = 0

	def add_player(self, p):
		self.__player.append(p)

	def get_player(self, n):
		return self.__player[n]

	def get_players(self):
		return self.__player

	def get_trash(self):
		return self.__trash

	def create_pile(self, card):
		p = Pile(card)
		p.add_card(card)
		card.setup()
		self.__pile.append(p)

	def get_piles(self):
		return self.__pile

	def get_pile(self, n):
		return self.__pile[n]

	def get_pile_count(self):
		return len(self.__pile)

	def get_pile_index_of_card(self, card_name):
		result = 0

		for p in self.__pile:
			if p.get_card_group().get_name() == card_name:
				result = self.__pile.index(p)
		return result

	def are_there_any_empty_piles(self):
		result = False
		for p in self.__pile:
			result = result or p.get_remaining() == 0
		return result

	def play(self):
		turn = 0
		# turn < 10 is for testing, otherwise endless as buying card is not yet done
		while not self.are_there_any_empty_piles(): # and turn < 10:
			self.print()
			self.__player[turn % len(self.__player)].take_turn()
			turn += 1
		else:
			self.print()
			for p in self.__player:
				print("" + str(p) + " scored " + str(p.get_score()) + " points.")
				if p.get_score() > self.__winning_score:
					self.__winning_score = p.get_score()
					self.__winner = p
			print("\n\n" + str(self.__winner) + " won with " + str(self.__winning_score) + " points.\n\n")

	def print(self):
		print("\nPiles:  ")
		index = 0
		for s in self.__pile:
			print(str(index) + ":  " + s.get_card_group().identify() + ":  " + str(s.get_remaining()))
			index += 1

		print("\nTrash:  ")
		index = 0
		for s in self.__trash.get_supply():
			print(str(index) + ":  " + s.identify())
			index += 1

	def __str__(self):
		return "A table with " + str(len(self.__pile)) + " card piles and " + str(len(self.__player)) + " players."
