from flask_login import UserMixin
from App import db, login_manager


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(150))
    firstName = db.Column(db.String(100))
    middleName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    emailAddress = db.Column(db.String(200))
    phoneNo = db.Column(db.String(20))
    password = db.Column(db.String(150))

    credentialNo = db.Column(db.Integer)
    recordNo = db.Column(db.Integer)
    galleryNo = db.Column(db.Integer)
    fileNo = db.Column(db.Integer)

    verification = db.relationship("Verfication")


class Verfication(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200))
    answer = db.Column(db.String(200))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


