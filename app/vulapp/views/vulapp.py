from flask import Blueprint
from flask import render_template, redirect
from app.vulapp.forms.auth import SignUpForm

vulapp = Blueprint("vulapp", __name__)

@vulapp.route("/")
def home():
	return render_template('index.html')

@vulapp.route("/signup", methods = ['GET', 'POST'])
def signup():
	form = SignUpForm()

	if form.validate_on_submit():
		return redirect('/')

	return render_template('signup.html', form=form)