from run import db

class Queens(db.Model):

    __tablename__ = 'queens'

    solution = db.Column(db.Integer, primary_key=True)
    positions = db.Column(db.String(15))