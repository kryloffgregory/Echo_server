from app import db, models
messages = models.Message.query.all()
for m in messages:
	print(m.id, m.msg)
