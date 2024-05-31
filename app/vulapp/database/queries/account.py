from app.vulapp.database.models.account import Account
from app.vulapp.database.db import db

def get_score(user_id):
	return Account.query.filter_by(user=user_id).first().score

def create_user_account(user_id):
	new_account = Account(
		score=100,
		user=user_id)
	db.session.add(new_account)
	db.session.commit()

def change_score(user_id, delta):
	account = Account.query.filter_by(user=user_id).first()
	account.score += delta
	db.session.add(account)
	db.session.commit()