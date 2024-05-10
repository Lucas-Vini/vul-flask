from flask_sqlalchemy import SQLAlchemy
from app.vulapp.database.config import DatabaseConfig
import os
from pymysql.constants.CLIENT import MULTI_STATEMENTS

db = SQLAlchemy()

def init_db(app):

	from app.vulapp.database.models.user import User
	
	config = DatabaseConfig()

	connection_string = f"{config.mysql_user}:{config.mysql_password}@{config.mysql_endpoint}/{config.mysql_database}?client_flag={MULTI_STATEMENTS}"

	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}'.format(connection_string)

	db.init_app(app)

	with app.app_context():
		db.create_all()