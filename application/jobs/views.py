from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from application import app, db
from application.jobs.models import Jobs
from application.jobs.forms import JobForm

from application.lists.models import Lists
from application.lists.forms import ListForm

#työn statuksen vaihto
@app.route("/<list_name>/<list_id>/status/<job_id>", methods=["GET", "POST"])
@login_required
def change_status(job_id, list_name, list_id):
	j=Jobs.query.get(job_id)

	if j.status == 3:
		j.status="1"
		db.session().commit()
		return redirect(url_for("show_list", list_id=list_id, list_name=list_name))

	if j.status == 2:
		j.status = "3"
		db.session().commit()
		return redirect(url_for("show_list", list_id=list_id, list_name=list_name))

	if j.status == 1:
		j.status = "2"
		db.session().commit()
		return redirect(url_for("show_list", list_id=list_id, list_name=list_name))


#työn poisto
@app.route("/<list_name>/<list_id>/<job_id>/delete", methods=["GET", "POST"])
@login_required
def job_delete(job_id, list_name, list_id):
	db.session.delete(Jobs.query.get(job_id))
	db.session().commit()
	return redirect(url_for("show_list", list_id=list_id, list_name=list_name))
