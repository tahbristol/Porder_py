from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from porder.models import User


class SignupForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	password_confirmation = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')
	
	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email has already been taken.')
			
			
class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class ItemForm(FlaskForm):
	name = StringField('Name')
	quantity = IntegerField('Qty')
	price = FloatField('Price')
	vendor = StringField('Vendor')
	submit = SubmitField('Save')
	