from . import db
from sqlalchemy.sql import func


class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer,primary_key =True)
    data = db.Column(db.String (1000))
    date = db.Column(db.DateTime(timezone = True),default=func.now)
    users_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
        return f'User {self.user_id}'

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key =True)
    email = db.Column(db.String (225),unique =True)
    password = db.Column(db.String (225))
    first_name = db.Column(db.String (225))
    notes = db.relationship('Note')

    def __repr__(self):
        return f'User {self.first_name}'
