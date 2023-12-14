from . import db

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    website = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Accounts {self.email}-{self.password}>'