from flask import Blueprint
from flask import render_template, redirect, flash
from app.vulapp.forms.auth import SignUpForm, LoginForm
from app.vulapp.handlers.auth import SignUpHandler, LoginHandler
from flask_login import current_user, login_user

auth = Blueprint("auth", __name__)

@auth.route("/")
def home():
	return render_template('index.html')

@auth.route("/signup", methods = ['GET', 'POST'])
def signup():
	form = SignUpForm()

	if form.validate_on_submit():
		user_created = SignUpHandler(form.username.data, form.password.data).user_created
		if user_created:
			return redirect('/login')

	return render_template('signup.html', title="Cadastrar", form=form)

@auth.route("/login", methods = ['GET', 'POST'])
def login():

	if current_user.is_authenticated:
		return redirect('/')
		
	form = LoginForm()

	if form.validate_on_submit():
		user = LoginHandler().check_user(form.username.data, form.password.data)

		if user:
			login_user(user)
			return redirect('/')

	return render_template('login.html', title="Entrar", form=form)