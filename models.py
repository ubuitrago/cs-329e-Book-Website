# beginning of models.py
# note that at this point you should have created "bookdb" database (see install_postgres.txt).
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:asd123@localhost:5432/bookdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)


class Book(db.Model):
	__tablename__ = 'book'
	
	title = db.Column(db.String(300), nullable = True)
	id = db.Column(db.Integer, primary_key = True)
	author = db.Column(db.String(300), nullable = True)
	isbn = db.Column(db.String(300), nullable = True)
	pubDate = db.Column(db.String(300), nullable = True)
	publisher = db.Column(db.String(300), nullable = True)
	imageURL = db.Column(db.String(1000), nullable = True)
	pubID = db.Column(db.String(300), nullable = True)
	authorID = db.Column(db.String(300), nullable = True)

class Author(db.Model):
	__tablename__ = 'author'

	name = db.Column(db.String(300), nullable = True)
	id = db.Column(db.Integer, primary_key = True)
	nationality = db.Column(db.String(300), nullable = True)
	yearOfBirth = db.Column(db.String(300), nullable = True)
	website = db.Column(db.String(1000), nullable = True)
	almaMater = db.Column(db.String(300), nullable = True)
	education = db.Column(db.String(300), nullable = True)
	imageURL = db.Column(db.String(1000), nullable = True)


class Publisher(db.Model):
	__tablename__ = 'publisher'

	name = db.Column(db.String(300), nullable = True)
	id = db.Column(db.Integer, primary_key = True)
	location = db.Column(db.String(300), nullable = True)
	founding = db.Column(db.String(300), nullable = True)
	parentCompany = db.Column(db.String(300), nullable = True)
	website = db.Column(db.String(1000), nullable = True)
	imageURL = db.Column(db.String(1000), nullable = True)


db.drop_all()
db.create_all()
# End of models.py

