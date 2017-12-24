from trash import Trash
from pile import Pile


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

	def add_pile(self, card, n):
		p = Pile()
		p.add_cards(card, n)
		self.__pile.append(p)

	def get_piles(self):
		return self.__pile

	def get_pile(self, n):
		return self.__pile[n]

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
		# turn < 4 is for testing, otherwise endless as buying cards is not yet done
		while not self.are_there_any_empty_piles() and turn < 4:
			self.print()
			self.__player[turn % len(self.__player)].take_turn()
			turn += 1
		else:
			self.print()
			for p in self.__player:
				if p.get_score() > self.__winning_score:
					self.__winning_score = p.get_score
					self.__winner = p

	def print(self):
		print("Piles:")
		for s in self.__pile:
			print(s.get_card_group().identify() + ":  " + str(s.get_remaining()))
