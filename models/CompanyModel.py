from api import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    visibility = db.Column(db.Boolean)
    grade = db.Column(db.Numeric)
    
    
    def __repr__(self):
        return f'<Sentence {self.username}>'
    