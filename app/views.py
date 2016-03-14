from flask import render_template, redirect, flash
from flask import request, url_for
from app import app, db
from .forms import EnterForm
from .models import Message
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
@app.route('/sent', methods = ['POST'])
def sent():
	got_message = request.form["message"]
	F = open('messages.txt','a')
	F.write(got_message + '\n')
	F.close()

	db.session.add(Message(got_message))
	db.session.commit()
	
	return 'You sent to server: ' + got_message + '<br><a href = "/"> Send new message </a>'
	
@app.route('/', methods = ['GET', 'POST'])
def index():
	return render_template("base.html", title ="Message")

