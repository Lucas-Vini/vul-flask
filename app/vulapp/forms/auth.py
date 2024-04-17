from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    password_confirmation = PasswordField('Confirme a senha', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')