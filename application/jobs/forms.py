from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField
from wtforms.validators import DataRequired, Length

class JobForm(FlaskForm):
	name = StringField("Job", validators=[DataRequired("anna työlle nimi"), Length(min=1, max=100)])
	status = IntegerField("1")

	class Meta:
		csrf = False
