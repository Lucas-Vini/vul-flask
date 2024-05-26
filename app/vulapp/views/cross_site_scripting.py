from flask import Blueprint
from flask import render_template, make_response
from app.vulapp.forms.cross_site_scripting import BetForm
from app.vulapp.handlers.cross_site_scripting import BetHandler
cross_site_scripting = Blueprint("cross_site_scripting", __name__)


@cross_site_scripting.route("/cross_site_scripting", methods = ['GET', 'POST'])
def bet():
	form = BetForm()
	result = None
	animal = None
	user_bet = None

	if form.validate_on_submit():
		bet = BetHandler()
		animal = bet.draw_an_animal().lower()
		user_bet = form.bet.data.lower()
		result = BetHandler().bet_checker(user_bet, animal)

	response = make_response(render_template('cross_site_scripting.html',
							title="Cross-Site Scripting",
							form=form,
							result=result,
							bet=user_bet,
							animal=animal,
							xss=form.xss.data))
	return response
