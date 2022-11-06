from app import db

class Entry(db.Model):

	__tablename__ = "entry"

	id = db.Column(db.Integer, primary_key=True)
	teamname = db.Column(db.String(256), unique=False, nullable=False)
	username = db.Column(db.String(256), unique=False, nullable=False)
	password = db.Column(db.String(256), unique=False, nullable=False)
	website  = db.Column(db.String(256), unique=False, nullable=False)

	def __init__(self, teamname=None, username=None, password=None, website=None):

		self.teamname = teamname
		self.username = username
		self.password = password
		self.website  = website

