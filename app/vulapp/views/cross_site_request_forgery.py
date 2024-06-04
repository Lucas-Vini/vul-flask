from flask import Blueprint
from flask import render_template
from app.vulapp.handlers.cross_site_request_forgery import TransferHandler
from flask_login import current_user
from app.vulapp.forms.cross_site_request_forgery import TransferForm

cross_site_request_forgery = Blueprint("cross_site_request_forgery", __name__)


@cross_site_request_forgery.route("/cross_site_request_forgery", methods = ['GET', 'POST'])
def transfer():

	form = TransferForm()

	if form.validate_on_submit():
		pass
	
	return render_template('cross_site_request_forgery.html', title="Transferir", form=form)