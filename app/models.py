from . import db
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager



class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key =True)
    data = db.Column(db.String (1000))
    date = db.Column(db.DateTime(timezone = True),default=func.now)
    users_id = db.Column(db.Integer,db.ForeignKey('users.id'))

#     def __repr__(self):
#         return f'User {self.users_id}'

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key =True)
    email = db.Column(db.String (225),unique =True)
    password = db.Column(db.String (225))
    first_name = db.Column(db.String (225))
    pitches = db.relationship('Pitch')
    pass_secure = db.Column(db.String(255))
     # def __repr__(self):
    #     return f'User {self.first_name}'
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
        
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

   




   
