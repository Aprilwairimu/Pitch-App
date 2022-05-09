from . import db
from sqlalchemy.sql import func
# from werkzeug.security import generate_password_hash,check_password_hash


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key =True)
    data = db.Column(db.String (1000))
    date = db.Column(db.DateTime(timezone = True),default=func.now)
    users_id = db.Column(db.Integer,db.ForeignKey('users.id'))

#     def __repr__(self):
#         return f'User {self.users_id}'

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key =True)
    email = db.Column(db.String (225),unique =True)
    password = db.Column(db.String (225))
    first_name = db.Column(db.String (225))
    pitches = db.relationship('Pitch')

    # def __repr__(self):
    #     return f'User {self.first_name}'
