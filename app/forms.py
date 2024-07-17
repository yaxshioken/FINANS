from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,EmailField,DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    card_number = StringField('Card Number', validators=[DataRequired(), Length(min=16, max=16)])
    card_date = DateField('Card Expiry Date', validators=[DataRequired()])
    submit = SubmitField('Register')
