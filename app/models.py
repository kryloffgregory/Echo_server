from app import db

class Message(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	msg = db.Column(db.String)
	def __init__(self, msg):
		self.msg = msg

	def __repr__(self):
		return "<User('%s')>" % (self.msg)
