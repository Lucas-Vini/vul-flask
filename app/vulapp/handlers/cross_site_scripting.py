import random

class BetHandler():
	def __init__(self):
		self.animals = ('Macaco', 'Lagarto', 'Tartaruga', 'Galinha', 'Tubarão',
						'Cobra', 'Baleia', 'Besouro', 'Onça', 'Tucano')

	def draw_an_animal(self):
		return self.animals[random.randint(0,9)]

	def bet_checker(self, bet, animal):
		if animal == bet:
			return True
		return False