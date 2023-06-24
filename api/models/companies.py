from app import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    visibility = db.Column(db.Boolean, default = True)
    grade = db.Column(db.Numeric, default = 0)

    def __repr__(self):
        return '<Id %r>' % self.id

    def json(self):
        return {'id': self.id, 'name': self.name, 'visibility': self.visibility, 'grade': float(self.grade)}
