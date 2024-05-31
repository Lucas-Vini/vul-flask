from app.vulapp.database.models.user import User
from app.vulapp.database.db import db
from app.vulapp.extensions.flask_login import login_manager

def add_new_user(username, password_hash):	
	new_user = User(
		username=username,
		password_hash=password_hash
		)
	db.session.add(new_user)
	db.session.commit()
	return new_user

def get_user(username):
	return User.query.filter_by(username=username).first()

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))