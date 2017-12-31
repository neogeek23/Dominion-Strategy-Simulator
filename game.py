from table.table import Table
from player.player import Player
from card.card import Card
from card.militia import Militia
from card.moat import Moat
from card.cellar import Cellar
from card.merchant import Merchant
from card.mine import Mine
from card.remodel import Remodel
from card.workshop import Workshop


def main():
	game = list()
	card_info = get_card_info()
	setup_new_game(game, get_game_parameters(), card_info)
	play_game(game[0])


def play_game(game_table):
	game_table.play()


# place holder setup for testing until frontend constructed
def setup_new_game(game_list, parameter, card_info):
	t = Table()
	humans = parameter[0]
	# bots = parameter[1]

	index = 0
	for p in parameter[2:]:
		if p:
			for i in range(card_info[index][9]):
				card = card_info[index][8](card_info[index][0], card_info[index][1], card_info[index][2],
		                                   card_info[index][3], card_info[index][4], card_info[index][5],
		                                   card_info[index][6], card_info[index][7], None)
				if i == 0:
					t.add_pile(card)
				else:
					t.get_pile(t.get_pile_index_of_card(card_info[index][0])).add_card(card)
		index += 1

	for i in range(humans):
		human = Player(True, t)
		human.draw_deck(t, get_starting_deck())
		human.draw_hand()
		t.add_player(human)

	# for i in range(bots):
	# 	bot = Player(False, t)
	# 	bot.draw_deck(t, get_starting_deck())
	# 	bot.draw_hand()
	# 	t.add_player(bot)

	game_list.append(t)


def get_game_parameters():
	# humans, bots, card #1, card #2, ... etc
	return [2, 1, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True]


def get_card_info():
	#       0               1   2                       3   4  5  6  7  8           9
	#		[name, 		cost, cardtype,			    	v,	c, a, b, d, class,      count] - values to pass to Card()
	return [["Copper",		0, Card.CardType.Treasure,	0,	1, 0, 0, 0, Card,       60],    # 1
			["Silver",		3, Card.CardType.Treasure,	0,	2, 0, 0, 0, Card,       40],    # 2
			["Gold",		6, Card.CardType.Treasure,	0,	3, 0, 0, 0, Card,       30],    # 3
			["Estate",		2, Card.CardType.Victory,	1,	0, 0, 0, 0, Card,       24],    # 4
			["Dutchy",		5, Card.CardType.Victory,	3,	0, 0, 0, 0, Card,       12],    # 5
			["Province",	8, Card.CardType.Victory,	6,	0, 0, 0, 0, Card,       12],    # 6
			["Curse",		0, Card.CardType.Curse,		-1,	0, 0, 0, 0, Card,       30],    # 7
			["Cellar",		2, Card.CardType.Action,	0,	0, 1, 0, 0, Cellar,     10],    # 8
			["Market",		5, Card.CardType.Action, 	0,	1, 1, 1, 1, Card,       10],    # 9
			["Merchant",    3, Card.CardType.Action,    0,  0, 1, 0, 1, Merchant,	10],    # 10
			["Militia",		4, Card.CardType.Attack,	0,	2, 0, 0, 0, Militia,	10],    # 11
			["Mine", 		5, Card.CardType.Action, 	0, 	0, 0, 0, 0, Mine,       10],    # 12
			["Moat",		2, Card.CardType.Reaction,	0,	0, 0, 0, 2, Moat,       10],    # 13
			["Remodel", 	4, Card.CardType.Action,	0,	0, 0, 0, 0, Remodel,    10],    # 14
			["Smithy",		4, Card.CardType.Action,	0,	0, 0, 0, 3, Card,       10],    # 15
			["Village",		3, Card.CardType.Action,	0,	0, 2, 0, 1, Card,       10],    # 16
			["Workshop",	4, Card.CardType.Action,	0,	0, 0, 0, 0, Workshop,	10]]    # 17
	#	Big Money
	#		["Adventurer",
	#		["Bureaucrat",
	#		["Chancellor",
	#		["Chapel",
	#		["Feast",
	#		["Laboratory",
	#		["Moneylender",
	#		["Throne Room",
	#	Interaction
	#		["Council Room",
	#		["Festival",
	#		["Library",
	#		["Spy",
	#		["Thief",
	#	Size Distortion
	#		["Gardens",
	#		["Woodcuter",
	#		["Witch",
	#	Villiage Square
	#	Trash Heap
	#	http://dominioncg.wikia.com/wiki/Pre-set_Sets_of_10
	#	http://www.dominiondeck.com/games/popular


def get_starting_deck():
	# return [["Copper", 7], ["Estate", 3]]
	# return [["Market", 2], ["Merchant", 2], ["Smithy", 2], ["Village", 2], ["Moat", 2]]
	# return [["Militia", 4], ["Cellar", 3], ["Moat", 3]]
	# return [["Silver", 7], ["Merchant", 3]]
	# return [["Copper", 4], ["Mine", 2], ["Remodel", 2], ["Workshop", 2]]
	return [["Copper", 1], ["Silver", 1], ["Gold", 1], ["Estate", 1], ["Dutchy", 1], ["Province", 1], ["Cellar", 1],
			["Market", 1], ["Merchant", 1], ["Militia", 1], ["Mine", 1], ["Moat", 1], ["Remodel", 1], ["Smithy", 1],
			["Village", 1], ["Workshop", 1]]


main()
