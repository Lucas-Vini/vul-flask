from app.vulapp.database.db import db

class Account(db.Model):
	__tablename__ = 'account'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	score = db.Column(db.Float)
	user = db.Column(db.Integer, db.ForeignKey('user.id'))