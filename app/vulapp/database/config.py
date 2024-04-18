import os

basedir = os.getcwd()

class DatabaseConfig:
	def __init__(self):
		self.sqlite_file_path = basedir + '/app/vulapp/database/vul.db'