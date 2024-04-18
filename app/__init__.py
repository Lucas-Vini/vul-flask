from flask import Flask
from app.ping import ping
from app.vulapp import vulapp
import os
from app.vulapp.database.db import init_db, db

ACTIVE_ENDPOINTS = (
	("/", ping),
	("/", vulapp )
	)

def create_app():
	app = Flask(__name__)
	#use a stored secret key to keep sessions in application reload
	app.config['SECRET_KEY'] = os.urandom(50) 

	# accepts both /endpoint and /endpoint/ as valid URLs
	app.url_map.strict_slashes = False

	for url, blueprint in ACTIVE_ENDPOINTS:
		app.register_blueprint(blueprint, url_prefix=url)

	init_db(app=app)

	return app