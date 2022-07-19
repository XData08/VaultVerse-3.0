import email
from multiprocessing.sharedctypes import Value
from flask_login import UserMixin
from App import db, login_manager


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(150), unique=True, nullable=False)
    firstName = db.Column(db.String(100))
    middleName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    emailAddress = db.Column(db.String(200), unique=True, nullable=False)
    phoneNo = db.Column(db.String(20))
    address = db.Column(db.String(300)) 
    password = db.Column(db.String(150), nullable=False)
    publicKey = db.Column(db.Integer)

    credentialNo = db.Column(db.Integer)
    recordNo = db.Column(db.Integer)
    galleryNo = db.Column(db.Integer)
    fileNo = db.Column(db.Integer)

    verification = db.relationship("Verfication")
    credentialAccount = db.relationship("CredentialAccount")
    credentialAddress = db.relationship("CredentialAddress")
    CredentialBankAccount = db.relationship("CredentialBankAccount")
    CredentialDriversLicense = db.relationship("CredentialDriversLicense")

    def __init__(self, userName, emailAddress, password):
        self.userName = userName
        self.emailAddress = emailAddress
        self.password = password
        self.credentialNo = 0
        self.recordNo = 0
        self.galleryNo = 0
        self.fileNo = 0

    def __repr__(self):
        return "<Users %r>"%self.userName


class Verfication(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200))
    answer = db.Column(db.String(200))

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class CredentialAccount(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    privateKey = db.Column(db.Integer)
    title = db.Column(db.String(150), unique=True)
    accountApplicationName = db.Column(db.String(150))
    accountUserName = db.Column(db.String(150))
    accountEmailAddress = db.Column(db.String(200))
    accountPassword = db.Column(db.String(200))
    accountNotes = db.Column(db.Text)
    date = db.Column(db.String(50))

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class CredentialAddress(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    privateKey = db.Column(db.Integer)
    title = db.Column(db.String(150), unique=True)
    addressFirstName = db.Column(db.String(150))
    addressMiddleName = db.Column(db.String(150))
    addressLastName = db.Column(db.String(150))
    addressPhoneNo = db.Column(db.String(50))
    addressEmailAddress = db.Column(db.String(200))
    addressHomeAddress = db.Column(db.String(300))
    addressNotes = db.Column( db.Text)
    date = db.Column(db.String(50))

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class CredentialBankAccount(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    privateKey = db.Column(db.Integer)
    title = db.Column(db.String(150), unique=True)
    bankAccountName = db.Column(db.String(200))
    bankAccountType = db.Column(db.String(100))
    bankAccountNumber = db.Column(db.String(50))
    bankAccountPin = db.Column(db.String(50))
    bankAccountNotes = db.Column(db.Text)
    date = db.Column(db.String(50))

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class CredentialDriversLicense(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    privateKey = db.Column(db.Integer)
    title = db.Column(db.String(150), unique=True)
    driversLicenseFirstName = db.Column(db.String(150))
    driversLicenseMiddleName = db.Column(db.String(150))
    driversLicenseLastName = db.Column(db.String(150))
    driversLicenseNationality = db.Column(db.String(100))
    driversLicenseGender = db.Column(db.String(50))
    driversLicenseDateBirth = db.Column(db.String(50))
    driversLicenseHomeAddress = db.Column(db.String(300))
    driversLicenseExpirationDate = db.Column(db.String(50))
    driversLicenseNo = db.Column(db.String(100))
    driversLicenseNotes = db.Column(db.Text)
    date = db.Column(db.String(50))

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))