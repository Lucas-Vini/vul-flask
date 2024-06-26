from flask import Blueprint, current_app
from flask import render_template, make_response
from app.vulapp.forms.cross_site_scripting import BetForm
from app.vulapp.handlers.cross_site_scripting import BetHandler
from flask_login import current_user


cross_site_scripting = Blueprint("cross_site_scripting", __name__)

@cross_site_scripting.route("/cross_site_scripting", methods = ['GET', 'POST'])
def bet():
	form = BetForm()
	result = None
	animal = None
	user_bet = None

	if form.validate_on_submit():
		if not current_user.is_authenticated:
			return render_template('cross_site_scripting.html',
							title="Cross-Site Scripting",
							form=form,
							xss=form.xss.data,
							not_authenticated=True)

		bet = BetHandler()
		animal = bet.draw_an_animal().lower()
		user_bet = form.bet.data.lower()
		result = BetHandler().bet_checker(user_bet, animal, current_user.get_id())


	response = make_response(render_template('cross_site_scripting.html',
							title="Cross-Site Scripting",
							form=form,
							result=result,
							bet=user_bet,
							animal=animal,
							xss=form.xss.data))
	return response
