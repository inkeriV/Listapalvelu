from flask import render_template
from application import app
from application.auth.models import User  #yhteenvetokysely
from flask_login import current_user, login_required

@app.route("/")
def index():
	return render_template("index.html", lazy_users=User.users_with_no_started_jobs(),
				waiting_jobs=User.users_with_waiting_jobs(),
				no_lists=User.users_with_no_lists())
