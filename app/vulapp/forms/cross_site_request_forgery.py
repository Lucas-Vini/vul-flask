from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired, NumberRange, Length

class TransferForm(FlaskForm):
    value = IntegerField('Quantidade de pontos que quer transferir', validators=[DataRequired("Valor não pode ser nulo"),
                                                                                 NumberRange(0, 10000000, "Valor fora do intervalo aceitável (0 < valor < 10000000)")])
    send_to = StringField('Usuário para quem quer transferir estes pontos', validators=[DataRequired("Usuário não pode ser nulo"),
                                                                                        Length(0, 34, "Usuário inválido")])
    submit = SubmitField('Transferir')