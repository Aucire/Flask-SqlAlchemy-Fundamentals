from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Application(db.Model):
    __tablename__ = 'testing'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(25))

    def __repr__(self):
        return f' ---> {self.id} ~ {self.name}'

class Doctor(db.Model):
    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))

    def __repr__(self):
        return f' Role:  Doctor , Name: {self.name}'   