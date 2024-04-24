from flask import Blueprint
from flask import render_template
from app.vulapp.forms.sql_injection import SearchForm

sql_injection = Blueprint("sql_injection", __name__)


@sql_injection.route("/sql_injection", methods = ['GET', 'POST'])
def search():
	form = SearchForm()

	if form.validate_on_submit():
		result = SearchHandler(form.search.data, form.sql_injection.data)

	return render_template('sql_injection.html', title="SQL Injection", form=form)