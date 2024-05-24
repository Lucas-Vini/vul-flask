from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

class BetForm(FlaskForm):
    bet = StringField('Escreva sua aposta', validators=[DataRequired(), Length(0, 128)])
    xss = BooleanField('XSS')
    submit = SubmitField('Apostar')