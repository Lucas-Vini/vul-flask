from werkzeug.security import generate_password_hash, check_password_hash
from app.vulapp.database.queries import auth as auth_queries
from app.vulapp.database.queries import account as account_queries

class SignUpHandler():
	def __init__(self, username, password):
		self.username = username
		self.password_hash = generate_password_hash(password)
		self.user_created = False

		if not self.user_exist(self.username):
			self.create_user(self.username, self.password_hash)
			self.user_created = True

	def user_exist(self, username):
		user = auth_queries.get_user(username)
		if user:
			return True
		return False

	def create_user(self, username, password_hash):
		user = auth_queries.add_new_user(username, password_hash)
		account_queries.create_user_account(user.id)

class LoginHandler():
	def check_user(self, username, password):
		user = auth_queries.get_user(username)
		if user:
			if check_password_hash(user.password_hash, password):
				return user
		return None
