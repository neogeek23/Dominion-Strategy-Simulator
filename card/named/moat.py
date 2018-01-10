from card.basic.card_action import  Action
from card.basic.card_reaction import Reaction


class Moat(Action, Reaction):
	prevent_attack = True
