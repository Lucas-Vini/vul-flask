from app.vulapp.database.db import db

class Product(db.Model):
	__tablename__ = 'product'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(64))
	price = db.Column(db.Float)
	stock = db.Column(db.Integer)