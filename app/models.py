from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

list_of_pitches = [[12,'pitch tweleve'],[14,'pitch 14']]
class Pitch:
    '''
    Pitch class to define Pitch Objects
    '''

    def __init__(self,id,pitch):
        self.id =id
        self.pitch = pitch

class Comment:
    all_comments = []

    def __init__(self,pitch_id,pitch,comment):
        self.pitch_id= pitch_id
        self.pitch = pitch
        self.comment = comment

    def save_comment(self):
        Comment.all_comments.append(self)

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

    @classmethod
    def get_comments(cls,id):
        results=[]

        for comment in cls.all_comments:
            if comment.pitch_id == id:
                results.append(comment)

        return results

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'



class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic") 

    def __repr__(self):
        return f'User {self.name}'  