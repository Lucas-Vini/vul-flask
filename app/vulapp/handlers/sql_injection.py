from app.vulapp.database.queries import sql_injection as sqli_queries
import random

class SearchProductHandler():
	def __init__(self):

		if not self.product_table_populated():
			self.populate_product_table()


	def search_products_by_keyword(self, search, sql_injection):
		if sql_injection:
			return sqli_queries.search_products_by_keyword_with_sql_injection(search)
		return sqli_queries.search_products_by_keyword(search)

	def product_table_populated(self):
		if sqli_queries.get_first_product():
			return True
		return False

	def populate_product_table(self):
		items = [
			'Camisa', 'Blusa', 'Calça', 'Bermuda', 'Tênis', 'Meia', 'Cueca', 'Boné',
			'Touca', 'Óculos', 'Relógio', 'Saia', 'Vestido', 'Calcinha', 'Chinelo'
		]

		colors = ['Vermelha', 'Amarela', 'Azul', 'Verde', 'Roxo', 'Laranja', 'Branca', 'Preta']

		sizes = ['Muito Pequeno', 'Pequeno', 'Médio', 'Grande', 'Muito Grande']

		products = self.create_products(items, colors, sizes)

		sqli_queries.add_products(products) 

	def create_products(self, items, colors, sizes):
		products = []
		for item in items:
			for color in colors:
				for size in sizes:
					products.append({
						"name": item + ' Cor ' + color + ' Tamanho ' + size,
						"price": random.randint(1, 100),
						"stock": random.randint(1, 100)
						})
		return products

