"""Importing the flask_wtf library from FlaskForm"""
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    """Enables registered users to login"""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    """Form for creating account"""
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=5, max=80)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=5, max=80)])
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=25)])
    email = StringField('Email',
        validators=[DataRequired(), Email(message='Enter a valid email'), Length(min=6, max=40)]
    )
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=25)])
    confirm_password = PasswordField('Repeat password',
        validators=[
            DataRequired(), EqualTo('password', message='The passwords need to match. Try again.')
        ]
    )
    remember = BooleanField('remember me')
    submit = SubmitField('Register')
    