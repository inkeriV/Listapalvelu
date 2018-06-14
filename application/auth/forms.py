from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from wtforms.validators import DataRequired, EqualTo, Length

#login
class LoginForm(FlaskForm):
	username = StringField("Username")
	password = PasswordField("Password")

	class Meta:
		csrf=False

#register
class RegisterForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired("enter name"), Length(min=2, max=30)])
	username = StringField("Username", validators=[DataRequired("enter username"), Length(min=2, max=20)])
	password = PasswordField("Password", validators=[DataRequired("enter password"),Length(min=4, max=20)])
	confirm = PasswordField("Confirm password", validators=[DataRequired("confirm password"), EqualTo("password")])

	class Meta:
		csrf=False #validointien tarkastaminen toimi vasta kun muistin lisätä tämän
