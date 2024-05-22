from app.vulapp.database.models.user import User
from app.vulapp.database.db import db
from app import login_manager

def add_new_user(username, password_hash):	
	new_user = User(
		username=username,
		password_hash=password_hash
		)
	db.session.add(new_user)
	db.session.commit()

def get_user(username):
	return User.query.filter_by(username=username).first()

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)