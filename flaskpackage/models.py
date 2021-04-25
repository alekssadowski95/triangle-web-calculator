from flaskpackage import db


class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Float, nullable=False)
    angle = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'Calculation("{self.height}","{self.angle}")'