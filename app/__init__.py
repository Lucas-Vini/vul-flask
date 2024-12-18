from flask import Flask
from app.ping import ping
from app.vulapp import auth, profile
from app.vulapp import sql_injection, cross_site_scripting, cross_site_request_forgery
import os
from app.vulapp.database.db import init_db, db
from app.vulapp.extensions.flask_login import init_login


ACTIVE_ENDPOINTS = (
	("/", ping),
	("/", auth ),
	("/", sql_injection),
	("/", cross_site_scripting),
	("/", profile),
	("/", cross_site_request_forgery)
	)

def create_app():
	app = Flask(__name__)

	#use a stored secret key to keep sessions in application reload
	app.config['SECRET_KEY'] = os.urandom(50)
	app.config['REMEMBER_COOKIE_HTTPONLY'] = False
	app.config['SESSION_COOKIE_HTTPONLY'] = False
	app.config['SESSION_COOKIE_SAMESITE'] = None
	
	# accepts both /endpoint and /endpoint/ as valid URLs
	app.url_map.strict_slashes = False

	for url, blueprint in ACTIVE_ENDPOINTS:
		app.register_blueprint(blueprint, url_prefix=url)

	init_db(app=app)
	init_login(app=app)

	return app