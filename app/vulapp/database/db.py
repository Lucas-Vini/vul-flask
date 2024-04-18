from flask_sqlalchemy import SQLAlchemy
from app.vulapp.database.config import DatabaseConfig
import os

db = SQLAlchemy()

def init_db(app):

	from app.vulapp.database.models.user import User
	
	config = DatabaseConfig()

	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + config.sqlite_file_path

	db.init_app(app)

	with app.app_context():
		db.create_all()