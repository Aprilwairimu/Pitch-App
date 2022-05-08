from . import db


class User(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    email = db.Column(db.String (225),unique =True)
    password = db.Column(db.String (225))
    first_name = db.Column(db.String (225))
    notes = db.relationship('Note')

    def __repr__(self):
        return f'User {self.username}'
