from . import db 

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

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.name}'