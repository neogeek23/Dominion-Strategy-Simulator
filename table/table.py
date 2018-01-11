from table.trash import Trash
from table.pile import Pile
from card.named.province import Province


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

	def are_there_three_empty_piles(self):
		count = 0
		for p in self.__pile:
			if p.get_remaining() == 0:
				count += 1
		return count > 2

	def has_provinces_run_out(self):
		for p in self.__pile:
			if isinstance(p.get_card_group(), Province):
				return p.get_remaining() == 0
		return False

	def should_game_end(self):
		return self.are_there_three_empty_piles() or self. has_provinces_run_out()

	def play(self):
		player_turn = 0
		should_continue = True
		while should_continue:
			# game ends after
			should_continue = not self.should_game_end() or player_turn % len(self.__player) != 0
			self.print()
			self.__player[player_turn % len(self.__player)].take_turn()
			player_turn += 1
		else:
			self.print()
			print("\n\nGame had " + str(player_turn) + " turns in " + str(player_turn/len(self.__player)) + " rounds.")
			for p in self.__player:
				print("" + str(p) + " scored " + str(p.get_score()) + " points.")
				if p.get_score() > self.__winning_score:
					self.__winning_score = p.get_score()
					self.__winner = p
			print("\n" + str(self.__winner) + " won with " + str(self.__winning_score) + " points.\n\n")

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

		print("")

	def __str__(self):
		return "A table with " + str(len(self.__pile)) + " card piles and " + str(len(self.__player)) + " players."
