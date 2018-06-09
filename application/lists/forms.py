from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField

class ListForm(FlaskForm):
	name = StringField("List name", [validators.Length(min=2)])
	type = IntegerField("1")

	class Meta:
		csrf = False
