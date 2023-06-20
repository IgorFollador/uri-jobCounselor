from api import db

class Sentence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sentence = db.Column(db.String, index=True, unique=False)
    
    
    def __repr__(self):
        return f'<Sentence {self.username}>'
    