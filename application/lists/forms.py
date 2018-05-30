from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ListForm(FlaskForm):
	name = StringField("List name", [validators.Length(min=2)])

	class Meta:
		csrf = False
