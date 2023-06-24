from app import db


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    visibility = db.Column(db.Boolean)
    grade = db.Column(db.Numeric)
    sentences = db.relationship('Sentence', backref='company')

    def __repr__(self):
        return '<Id %r>' % self.id

    def json(self):
        return {'id': self.id, 'name': self.name, 'visibility': self.visibility, 'grade': float(self.grade)}
