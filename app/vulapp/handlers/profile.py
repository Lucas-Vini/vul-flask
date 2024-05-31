from app.vulapp.database.queries import account as account_queries

class ProfileHandler():
	def __init__(self):
		pass

	def get_score(self, user_id):
		return account_queries.get_score(user_id)

	def get_products(self, user_id):
		pass