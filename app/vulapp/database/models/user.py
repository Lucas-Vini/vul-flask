from app.vulapp.database.db import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(32), unique=True)
	password_hash = db.Column(db.String(256))

