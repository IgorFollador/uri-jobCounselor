from app import db


class Sentence(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    grade = db.Column(db.Numeric, nullable=False)
    sentence = db.Column(db.String(600), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Id %r>' % self.id

    def json(self):
        return {'id': self.id, 'grade': float(self.grade), 'sentence': self.sentence, 'date': self.date.isoformat()}
