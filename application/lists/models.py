from application import db

class Lists(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp())
	onupdate=db.func.current_timestamp()

	name = db.Column(db.String(144), nullable=False)
	type = db.Column(db.Integer, nullable=False)

	account_id = db.Column(db.Integer, db.ForeignKey('account.id'),nullable=False)
	jobs = db.relationship("Jobs", cascade='all, delete-orphan', backref='lists', lazy=True) #delete orphan poistaa listan työt kun lista poistetaan

	def __init__(self, name, type):
		self.name = name
		self.type = 1


