from flask import Blueprint
from flask import render_template, redirect, url_for, request
from app.vulapp.forms.auth import SignUpForm, LoginForm
from app.vulapp.handlers.auth import SignUpHandler, LoginHandler
from flask_login import current_user, login_user, logout_user

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
			return redirect(url_for('auth.login', user_created=True))
		else:
			return render_template('signup.html', title="Cadastrar", form=form, signup_failed=True)


	return render_template('signup.html', title="Cadastrar", form=form)

@auth.route("/login", methods = ['GET', 'POST'])
def login():

	if current_user.is_authenticated:
		return redirect('/')
		
	form = LoginForm()

	if form.validate_on_submit():
		user = LoginHandler().check_user(form.username.data, form.password.data)

		if user:
			login_user(user, remember=True)
			return redirect('/my_profile')
		else:
			return render_template('login.html', title="Entrar", form=form, login_failed=True)


	user_created = None
	if request.args.get('user_created'):
		user_created = request.args['user_created']

	return render_template('login.html', title="Entrar", form=form, user_created=user_created)

@auth.route("/logout", methods = ['GET'])
def logout():
	logout_user()
	return redirect('/')