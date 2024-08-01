from app.vulapp.database.queries import auth as auth_queries
from app.vulapp.database.queries import account as account_queries

class TransferHandler():
	def __init__(self, value, from_user, to_user):
		self.value = float(value)
		self.from_user = from_user
		self.to_user = to_user
		self.transfered = False
		self.message = self.transfer()

	def transfer(self):
		if not self.user_exist():
			return "Erro ao tentar tranferir para este usuário"
		if not self.enough_score():
			return "Saldo insuficiente"
		self.transfered = self.execute_transfer()
		if self.transfered:
			return "Transferência realizada com sucesso"
		else:
			return "Algo de errado aconteceu ao tentar fazer a transferência"

	def user_exist(self):
		user = auth_queries.get_user(self.to_user)
		if user:
			self.to_user = user.id
			return True
		return False

	def enough_score(self):
		if float(account_queries.get_score(self.from_user)) > self.value:
			return True
		return False

	def execute_transfer(self):
		try:
			account_queries.transfer_score(self.value, self.from_user, self.to_user)
			return True
		except:
			return False


