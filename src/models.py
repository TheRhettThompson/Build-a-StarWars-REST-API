from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(120) , unique=True , nullable=False) #unique = only 1 character w/ the name, nullable =cannot be blank

#tells python how to print to the console under character
    def __repr__(self):
        return '<Character %r>' % self.name

#serialize = every single time we add item to the column, we are going to add the id and name to the columns.
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name 
        }

#start Planets here :)
class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120) , unique=True , nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }