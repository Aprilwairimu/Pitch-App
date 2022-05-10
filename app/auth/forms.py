from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, BooleanField
from wtforms.validators import InputRequired,Email,EqualTo
from ..models import User
from wtforms import ValidationError



class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[InputRequired(),Email()])
    username = StringField('Enter your username',validators = [InputRequired()])
    password = PasswordField('Password',validators = [InputRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [InputRequired()])
    submit = SubmitField('Sign Up')


def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

def validate_username(self,data_field):
    if User.query.filter_by(username = data_field.data).first():
        raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[InputRequired(),Email()])
    password = PasswordField('Password',validators =[InputRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
