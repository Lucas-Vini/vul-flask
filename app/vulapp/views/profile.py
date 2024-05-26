from flask import Blueprint
from flask import render_template, redirect
from app.vulapp.handlers.profile import ProfileHandler
from flask_login import current_user

profile = Blueprint("profile", __name__)


@profile.route("/my_profile", methods = ['GET'])
def my_profile():
	
	if not current_user.is_authenticated:
		return redirect('/login')

	return render_template('my_profile.html', title="Meu perfil", name=current_user.username)