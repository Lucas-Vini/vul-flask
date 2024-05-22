from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

class PasswordComplexity():
    def __init__(self, message=None):
        if not message:
            message = ''
        self.message = message

    def __call__(self, form, field):
        text = field.data

        if not any((not char.isalnum()) for char in text):
            raise ValidationError('A senha precisa conter ao menos um caracter especial')

        if not any(char.isdigit() for char in text):
            raise ValidationError('A senha precisa conter ao menos um número')

        if text.isupper():
            raise ValidationError('A senha precisa conter ao menos uma letra minúscula')


        if text.islower():
            raise ValidationError('A senha precisa conter ao menos uma letra maiúscula')

        if len(text) < 8 or len(text) > 20:
            raise ValidationError('Senha deve ter entre 8 e 20 caracteres')


username_validators = [
    DataRequired("Usuário não pode ser nulo")
]

password_validators = [
    DataRequired("Senha não pode ser nula"),
    PasswordComplexity()
]

password_confirmation_validators = [
    DataRequired("Repita a senha"),
    EqualTo('password', "As senhas não coincidem")
]

class SignUpForm(FlaskForm):
    username = StringField('Usuário', validators=username_validators)
    password = PasswordField('Senha', validators=password_validators)
    password_confirmation = PasswordField('Confirme a senha', validators=password_confirmation_validators)
    submit = SubmitField('Cadastrar')

class LoginForm(FlaskForm):
    username = StringField('Usuário')
    password = PasswordField('Senha')
    submit = SubmitField('Entrar')

