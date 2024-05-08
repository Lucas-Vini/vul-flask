from app.vulapp.database.models.product import Product
from app.vulapp.database.db import db
from sqlalchemy.sql import text

def get_first_product():
	return Product.query.first()

def add_products(products):
	for product in products:		
		new_product = Product(
			name=product["name"],
			price=product["price"],
			stock=product["stock"]
			)
		db.session.add(new_product)
	db.session.commit()

def search_products_by_keyword(search):
	search = "%{}%".format(search)
	return Product.query.filter(Product.name.like(search)).all()

def search_products_by_keyword_with_sql_injection(search):
	query = "SELECT * FROM product WHERE name LIKE '%{}%';".format(search)
	result = db.session.execute(text(query)).all()
	return result