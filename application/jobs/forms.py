from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField

class JobForm(FlaskForm):
	name = StringField("Job", [validators.Length(min=3)])
	status = IntegerField("1")

	class Meta:
		csrf = False
