from enum import Enum, auto


class Card:
	class CardType(Enum):
		Action = auto()
		Attack = auto()
		Treasure = auto()
		Victory = auto()
		Curse = auto()
		Reaction = auto()

	def __init__(self, name, cost, cardtype, value, coin, action, reaction, buy, draw, effect):
		self.__name = name
		self.__cost = cost
		self.__coin = coin
		self.__type = cardtype
		self.__action = action
		self.__buy = buy
		self.__draw = draw
		self.__effect = effect
		self.__value = value
		self.__reaction = reaction

	def play(self, player):
		player.add_actions(self.__action)
		player.add_buys(self.__buy)
		player.add_purchase_power(self.__coin)
		player.add_reactions(self.__reaction)
		self.effect()

	def effect(self):
		pass

	def get_name(self):
		return self.__name

	def get_type(self):
		return self.__type

	def identify(self):
		return self.__name + ", " + str(self.__type) + ", " + str(self.__cost)