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

def transfer_score(value, from_user, to_user):
	from_user_db = Account.query.filter_by(user=from_user).first()
	to_user_db = Account.query.filter_by(user=to_user).first()
	from_user_db.score -= value
	to_user_db.score += value
	db.session.add(to_user_db)
	db.session.add(from_user_db)
	db.session.commit()