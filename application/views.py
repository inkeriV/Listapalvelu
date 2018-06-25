from flask import render_template
from application import app
from application.auth.models import User  #yhteenvetokysely
from flask_login import current_user, login_required

@app.route("/")
def index():
	return render_template("index.html", lazy_users=User.users_with_no_started_jobs())
