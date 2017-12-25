from table import Table
from player import Player
from card import Card


def main():
	game = list()
	card_info = get_card_info()
	setup_new_game(game, get_game_parameters(), card_info)
	play_game(game[0])


def setup_new_game(game_list, parameter, card_info):
	t = Table()
	humans = parameter[0]
	bots = parameter[1]

	index = 0
	for p in parameter[2:]:
		if p:
			card = Card(card_info[index][0], card_info[index][1], card_info[index][2], card_info[index][3],
						card_info[index][4], card_info[index][5], card_info[index][6], card_info[index][7],
						card_info[index][8], card_info[index][9])
			t.add_pile(card, card_info[index][10])
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


def play_game(game_table):
	game_table.play()


def get_game_parameters():
	return [1, 1, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True]


def get_card_info():
	#		[name, 		cost, cardtype,			    	v,	c, a, r, b, d, effect, count] - value to pass to Card()
	return [["Copper",		0, Card.CardType.Treasure,	0,	1, 0, 0, 0, 0, None, 60],   # 1
			["Silver",		3, Card.CardType.Treasure,	0,	2, 0, 0, 0, 0, None, 40],   # 2
			["Gold",		6, Card.CardT]ype.Treasure,	0,	3, 0, 0, 0, 0, None, 30],   # 3

			["Estate",		2, Card.CardType.Victory,	1,	0, 0, 0, 0, 0, None, 24],   # 4
			["Dutchy",		5, Card.CardType.Victory,	3,	0, 0, 0, 0, 0, None, 12],   # 5
			["Province",	8, Card.CardType.Victory,	6,	0, 0, 0, 0, 0, None, 12],   # 6

			["Curse",		0, Card.CardType.Curse,		-1,	0, 0, 0, 0, 0, None, 30],   # 7

			["Cellar",		2, Card.CardType.Action,	0,	0, 1, 0, 0, 0, "Name", 10], # 8
			["Market",		5, Card.CardType.Action, 	0,	1, 1, 0, 1, 1, None, 10],   # 9
			["Merchant",    3, Card.CardType.Action,    0,  0, 1, 0, 0, 1, "Name", 10], # 10
	        ["Militia",		4, Card.CardType.Attack,	0,	2, 0, 1, 0, 0, "Name", 10], # 11
			["Mine", 		5, Card.CardType.Action, 	0, 	0, 0, 0, 0, 0, "Name", 10], # 12
			["Moat",		2, Card.CardType.Reaction,	0,	0, 0, 0, 0, 2, "Name", 10], # 13
			["Remodel", 	4, Card.CardType.Action,	0,	0, 0, 0, 0, 0, "Name", 10], # 14
			["Smithy",		4, Card.CardType.Action,	0,	0, 0, 0, 0, 3, None, 10],   # 15
			["Village",		3, Card.CardType.Action,	0,	0, 2, 0, 0, 1, None, 10],   # 16
			["Workshop",	4, Card.CardType.Action,	0,	0, 0, 0, 0, 0, "Name", 10]] # 17


def get_starting_deck():
	return [["Copper", 7], ["Estate", 3]]
	# return [["Market", 2], ["Merchant", 2], ["Smithy", 2], ["Village", 2], ["Moat", 2]]

main()