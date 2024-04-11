from flask import Blueprint
from flask import render_template

vulapp = Blueprint("vulapp", __name__)

@vulapp.route("/")
def main():
	return render_template('index.html')