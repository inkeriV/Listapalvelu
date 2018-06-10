from application import db

from sqlalchemy.sql import text

class User(db.Model):
	__tablename__="account"

	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

	name = db.Column(db.String(144), nullable=False)
	username = db.Column(db.String(144), nullable=False)
	password = db.Column(db.String(144), nullable=False)

	#alla olevasta rivistä tuli virhe, sillä olin kirjoittanut "lists" enkä "Lists".
	#Lists viittaa luokkaan ja lists viittaa tauluun !! tässä piti viitata luokkaan.
	lists = db.relationship("Lists", backref='account', lazy=True)



	#tässä oli parametreinä ennen(self, name, username, password)
	#ja sisällä selfin lisäksi self.username=username, self.password=password
	#tästä mahdollisesti virhe-kokeilua
	def __init__(self, name):
		self.name=name


	def get_id(self):
	        return self.id

	def is_active(self):
	        return True

	def is_anonymous(self):
	       	return False

	def is_authenticated(self):
	        return True


	#yhteenvetokysely. muista sisentää!
	@staticmethod
	def users_with_no_started_jobs():
		stmt = 	text(	"SELECT Account.id FROM Account, Lists, Jobs" #count(account.id) 
		              	" WHERE Account.id = Lists.account_id AND Lists.id = Jobs.list_id"
		                " AND Jobs.id NOT IN(SELECT Jobs.id FROM Jobs WHERE"
		                " Jobs.status=2 OR Jobs.status=3)")
		tulos=db.engine.execute(stmt)
		#print(tulos.fetchall())
		#for row in tulos: #toinen vaihtoehto, kyselyssä vika..
		#	print(row[0])
		lista=[]
		for row in tulos:
			lista.append({"id":row[0]})
		return lista
