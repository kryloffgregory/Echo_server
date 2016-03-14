from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required
from wtforms.validators import DataRequired
class EnterForm(Form):
    message = TextField('message', validators = [DataRequired()])
