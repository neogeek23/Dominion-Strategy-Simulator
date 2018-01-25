from card.basic.card_action import  Action
from card.basic.card_reaction import Reaction


class Moat(Action, Reaction):
	def react(self, what_attack):
		owner = self.get_owner()
		return "Y" == owner.take_input("Player " + str(owner.get_player_index()) + ", enter 'Y' if you'd "
		                                      "like to reveal " + str(self) + " to block the " + str(what_attack) +
		                                      " attack:  ", str)
