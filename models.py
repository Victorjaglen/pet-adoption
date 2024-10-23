from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
db = SQLAlchemy(app)


class Pet(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('created', db.DateTime, default=datetime.datetime.now)
    name = db.Column('name', db.String())
    age = db.Column('age', db.String())
    breed = db.Column('breed', db.String())
    color = db.Column('color', db.String())
    size = db.Column('size', db.String())
    weight = db.Column('weight', db.String())
    url = db.Column('url', db.String())
    alt_tag = db.Column('alt_tag', db.String())
    pet_type = db.Column('pet_type', db.String())
    gender = db.Column('gender', db.String())
    spay = db.Column('spay', db.String())
    house_trained = db.Column('housetrained', db.String())
    description = db.Column('description', db.Text)

    def __repr__(self):
        return f'''<Pet (Name: {self.name}
                    Age: {self.age}
                    Breed: {self.breed}
                    Color: {self.color}
                    Size: {self.size}
                    Weight: {self.weight}
                    URL: {self.url}
                    Alt Tag: {self.alt_tag}
                    Gender: {self.gender}
                    Spay: {self.spay}
                    House Trained: {self.house_trained}
                    Description: {self.description})'''