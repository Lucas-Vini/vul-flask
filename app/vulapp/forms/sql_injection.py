from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
    search = StringField('Buscar produtos', validators=[DataRequired(), Length(0, 128)])
    sql_injection = BooleanField('SQLi')
    submit = SubmitField('Buscar')