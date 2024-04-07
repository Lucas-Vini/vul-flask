from flask import Blueprint

vulapp = Blueprint("vulapp", __name__)

@vulapp.route("/vulapp")
def main():
	'''Ping endpoint, used to know if the app is up'''
	return "vulapp"