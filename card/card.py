class Card:
	prevent_attack = False
	normal_full_table = 6
	pile_player_rate = 10

	def __init__(self, name, cost, value, coin, action, buy, draw, owner):
		self.__name = name
		self.__cost = cost
		self.__coin = coin
		self.__action = action
		self.__buy = buy
		self.__draw = draw
		self.__value = value
		self.__owner = owner

	def play(self):
		self.__owner.add_actions(self.__action)
		self.__owner.add_buys(self.__buy)
		self.__owner.add_purchase_power(self.__coin)
		self.__owner.draw_cards(self.__draw)
		self.effect()

	def effect(self):
		# This is here so that 'special' card can override this function so that unique card effects can happen.
		pass

	@classmethod
	def pile_setup(cls, player_count):
		# This is here so that each card can override this function so that the right number of .
		pass

	@staticmethod
	def setup():
		# This is here so that 'special' card can override this function so that unique card setup effects can happen.
		pass

	def get_name(self):
		return self.__name

	def get_points(self):
		return self.__value

	def get_cost(self):
		return self.__cost

	def get_purchase_power(self):
		return self.__coin

	def set_owner(self, owner):
		self.__owner = owner

	def get_owner(self):
		return self.__owner

	def identify(self):
		return self.__name + ", " + self.__str__() + ", costing " + str(self.__cost)

	def print_card_list(self, card, message):
		print("\nPlayer " + str(self._Card__owner.get_player_index()) + " " + message)

		counter = 0
		for c in card:
			print(str(counter) + ":  " + c.identify())
			counter += 1

	def __get_index_not_self(self):
		result = -1
		for c in self._Card__owner.get_hand().get_supply():
			if c != self:
				result = self._Card__owner.get_hand().get_player_index()
		return result

	def __str__(self):
		return "a " + self.__name + " card"
