from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/animalfacts.db'
db = SQLAlchemy(app)


class Facts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal = db.Column(db.String(20))
    fact = db.Column(db.String(), unique=True)

    def __init__(self, animal, fact):
    	self.animal = animal
        self.fact = fact

    def __repr__(self):
        return '<Fact %r>' % self.fact