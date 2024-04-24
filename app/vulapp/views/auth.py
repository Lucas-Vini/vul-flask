from flask import Blueprint
from flask import render_template, redirect, flash
from app.vulapp.forms.auth import SignUpForm
from app.vulapp.handlers.auth import SignUpHandler

auth = Blueprint("auth", __name__)

@auth.route("/")
def home():
	return render_template('index.html')

@auth.route("/signup", methods = ['GET', 'POST'])
def signup():
	form = SignUpForm()

	if form.validate_on_submit():
		sign_up_result = SignUpHandler(form.username.data, form.password.data)
		return redirect('/')
	return render_template('signup.html', title="Cadastrar", form=form)