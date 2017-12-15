from app.models import db


class Cpu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    c1 = db.Column(db.Integer, nullable=False)
