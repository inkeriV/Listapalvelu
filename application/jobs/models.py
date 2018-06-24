from application import db

class Jobs(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp())
	onupdate=db.func.current_timestamp()

	name = db.Column(db.String(144), nullable=False)
	status = db.Column(db.Integer, nullable=False)

	list_id = db.Column(db.Integer, db.ForeignKey('lists.id'), nullable=False)

	def __init__(self, name, status):
		self.name = name
		self.status = 1

