from api import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    grade = db.Column(db.Numeric, nullable=False)
    
    
    def __repr__(self):
        return f'<Sentence {self.username}>'
    