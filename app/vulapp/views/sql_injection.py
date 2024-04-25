from flask import Blueprint
from flask import render_template
from app.vulapp.forms.sql_injection import SearchForm
from app.vulapp.handlers.sql_injection import SearchProductHandler

sql_injection = Blueprint("sql_injection", __name__)


@sql_injection.route("/sql_injection", methods = ['GET', 'POST'])
def search():
	form = SearchForm()

	result = []
	if form.validate_on_submit():
		result = SearchProductHandler().search_products_by_keyword(form.search.data, form.sql_injection.data)

	return render_template('sql_injection.html', title="SQL Injection", form=form, result=result)