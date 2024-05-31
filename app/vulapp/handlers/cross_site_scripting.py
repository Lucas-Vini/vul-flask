import random
from app.vulapp.database.queries import account as account_queries

class BetHandler():
	def __init__(self):
		self.animals = ('Macaco', 'Lagarto', 'Tartaruga', 'Galinha', 'Tubarão',
						'Cobra', 'Baleia', 'Besouro', 'Onça', 'Tucano')

	def draw_an_animal(self):
		return self.animals[random.randint(0,9)]

	def bet_checker(self, bet, animal, user_id):
		if animal == bet:
			account_queries.change_score(user_id, 50)
			return True
		account_queries.change_score(user_id, -2)
		return False