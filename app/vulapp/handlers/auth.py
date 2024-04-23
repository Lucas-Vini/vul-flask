from werkzeug.security import generate_password_hash

class SignUpHandler():
	def __init__(self, username, password):
		self.username = username
		self.password_hash = generate_password_hash(password)

		if self.user_exist:
			return False
		else:
			self.create_user(self.username, self.password_hash)

	def create_user(self, username, password_hash):
		pass