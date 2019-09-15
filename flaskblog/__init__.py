from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '5001bcb5b4c8439cee67d9964c03c6d2'
app.config['SQLACHEMY_DATABASE_URI'] = ''
db = SQLAlchemy(app)

from flaskblog import routes 