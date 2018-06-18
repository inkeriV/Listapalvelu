from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField
from wtforms.validators import DataRequired, Length

class ListForm(FlaskForm):
	name = StringField("List name", validators=[DataRequired("anna listalle nimi"), Length(min=1, max=30)])
	type = IntegerField("1")

	class Meta:
		csrf = False
