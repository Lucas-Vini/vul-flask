from flask import Blueprint
from flask import render_template, redirect
from app.vulapp.handlers.profile import ProfileHandler
from flask_login import current_user

profile = Blueprint("profile", __name__)


@profile.route("/my_profile", methods = ['GET'])
def my_profile():
	
	if not current_user.is_authenticated:
		return redirect('/login')
	
	user_profile = ProfileHandler()
	user_score = user_profile.get_score(current_user.get_id())
	user_products = user_profile.get_products(current_user.get_id())

	return render_template('my_profile.html',
							title="Meu perfil",
							name=current_user.username,
							user_score=user_score,
							user_products=user_products)