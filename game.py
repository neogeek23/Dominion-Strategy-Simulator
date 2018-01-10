from table.table import Table
from player.human import Human
from player.bots.pure_big_money import Pure_Big_Money
from card.basic.card_action import Action
from card.basic.card_curse import Curse
from card.basic.card_victory import Victory
from card.named.estate import Estate
from card.named.copper import Copper
from card.named.silver import Silver
from card.named.gold import Gold
from card.named.militia import Militia
from card.named.moat import Moat
from card.named.cellar import Cellar
from card.named.merchant import Merchant
from card.named.mine import Mine
from card.named.remodel import Remodel
from card.named.workshop import Workshop


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
	bots = parameter[1]

	index = 0
	for p in parameter[2:]:
		if p:
			for i in range(card_info[index][7].pile_setup(humans + bots)):
				card = card_info[index][7](card_info[index][0], card_info[index][1], card_info[index][2],
										   card_info[index][3], card_info[index][4], card_info[index][5],
		                                   card_info[index][6], None)
				if i == 0:
					t.create_pile(card)
				else:
					t.get_pile(t.get_pile_index_of_card(card_info[index][0])).add_card(card)
			card_info[index][7].setup()
		index += 1

	for i in range(humans):
		human = Human(t)
		human.draw_deck(t, get_starting_deck())
		human.draw_hand()
		t.add_player(human)

	for i in range(bots):
		bot = Pure_Big_Money(t)
		bot.draw_deck(t, get_starting_deck())
		bot.draw_hand()
		t.add_player(bot)

	game_list.append(t)


def get_game_parameters():
	# humans, bots, card #1, card #2, ... etc
	return [1, 1, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True]


def get_card_info():
	#       0               1  2    3  4  5  6  7
	#		[name, 		 cost, v,	c, a, b, d, class] - values to pass to Card()
	return [["Copper",		0, 0,	1, 0, 0, 0, Copper],    	# 0
			["Silver",		3, 0,	2, 0, 0, 0, Silver],		# 1
			["Gold",		6, 0,	3, 0, 0, 0, Gold],	    	# 2
			["Estate",		2, 1,	0, 0, 0, 0, Estate],		# 3
			["Dutchy",		5, 3,	0, 0, 0, 0, Victory],		# 4
			["Province",	8, 6,	0, 0, 0, 0, Victory],    	# 5
			["Curse",		0, -1,	0, 0, 0, 0, Curse],    		# 6
			["Cellar",		2, 0,	0, 1, 0, 0, Cellar],    	# 7
			["Market",		5, 0,	1, 1, 1, 1, Action],    	# 8
			["Merchant",    3, 0,	0, 1, 0, 1, Merchant],		# 9
			["Militia",		4, 0,	2, 0, 0, 0, Militia],		# 10
			["Mine", 		5, 0, 	0, 0, 0, 0, Mine],    		# 11
			["Moat",		2, 0,	0, 0, 0, 2, Moat],    		# 12
			["Remodel", 	4, 0,	0, 0, 0, 0, Remodel],		# 13
			["Smithy",		4, 0,	0, 0, 0, 3, Action],    	# 14
			["Village",		3, 0,	0, 2, 0, 1, Action],    	# 15
			["Workshop",	4, 0,	0, 0, 0, 0, Workshop]]		# 16
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
	return [["Copper", 7], ["Estate", 3]]
	# return [["Market", 2], ["Merchant", 2], ["Smithy", 2], ["Village", 2], ["Moat", 2]]
	# return [["Militia", 4], ["Cellar", 3], ["Moat", 3]]
	# return [["Silver", 7], ["Merchant", 3]]
	# return [["Copper", 4], ["Mine", 2], ["Remodel", 2], ["Workshop", 2]]
	# return [["Copper", 1], ["Silver", 1], ["Gold", 1], ["Estate", 1], ["Dutchy", 1], ["Province", 1], ["Cellar", 1],
	# 		["Market", 1], ["Merchant", 1], ["Militia", 1], ["Mine", 1], ["Moat", 1], ["Remodel", 1], ["Smithy", 1],
	# 		["Village", 1], ["Workshop", 1]]


main()
