from flask import Blueprint
from flask import render_template, request, redirect
from app.vulapp.handlers.cross_site_request_forgery import TransferHandler
from flask_login import current_user
from app.vulapp.forms.cross_site_request_forgery import TransferForm

cross_site_request_forgery = Blueprint("cross_site_request_forgery", __name__)


@cross_site_request_forgery.route("/cross_site_request_forgery_select", methods = ['GET'])
def transfer():
		return render_template('cross_site_request_forgery_select.html', title="Transferir")

@cross_site_request_forgery.route("/cross_site_request_forgery_safe", methods = ['GET', 'POST'])
def safe_transfer():
	if not current_user.is_authenticated:
		return redirect('/cross_site_request_forgery_select')

	form = TransferForm()
	message = None
	transfered = None

	if form.validate_on_submit():
		transfer = TransferHandler(value=form.value.data,
						from_user=current_user.get_id(),
						to_user=form.send_to.data)
		message = transfer.message
		transfered = transfer.transfered

	return render_template('cross_site_request_forgery_safe.html',
							title="Transferir",
							form=form,
							message=message,
							transfered=transfered)

@cross_site_request_forgery.route("/cross_site_request_forgery_vulnerable", methods = ['GET', 'POST'])
def vul_transfer():
	if not current_user.is_authenticated:
		return redirect('/cross_site_request_forgery_select')

	message = None
	transfered = None
	value = request.form.get('value')
	send_to = request.form.get('send_to')

	if value and send_to:
		transfer = TransferHandler(value=value,
						from_user=current_user.get_id(),
						to_user=send_to)
		message = transfer.message
		transfered = transfer.transfered


	return render_template('cross_site_request_forgery_vulnerable.html',
							title="Transferir",
							message=message,
							transfered=transfered)