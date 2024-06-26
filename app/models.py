from app import db

# from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    marks = db.Column(db.Integer, index=True)

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class TopikQuestions(db.Model):
    t_id = db.Column(db.Integer, primary_key=True)
    ques = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<TopikQuestion {self.t_id}: {self.ques}>"


class Questions(db.Model):
    q_id = db.Column(db.Integer, primary_key=True)
    ques = db.Column(db.String(350), unique=True)
    a = db.Column(db.String(100))
    b = db.Column(db.String(100))
    c = db.Column(db.String(100))
    d = db.Column(db.String(100))
    ans = db.Column(db.String(100))
    t_id = db.Column(db.Integer, db.ForeignKey("topik_questions.t_id"))
    t_ques = db.relationship("TopikQuestions", backref="questions")

    def __repr__(self):
        return "<Question: {}>".format(self.ques)
