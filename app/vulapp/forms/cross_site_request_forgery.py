from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

class TransferForm(FlaskForm):
    value = IntegerField('Quantidade de pontos que quer transferir', validators=[DataRequired(), Length(0, 128)])
    send_to = StringField('Usuário para quem quer transferir estes pontos')
    csrf = BooleanField('CSRF')
    submit = SubmitField('Transferir')