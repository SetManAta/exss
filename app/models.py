from app import db, bcrypt,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False,unique=True)
    password_hash = db.Column(db.String,nullable=False)

    def __repr__(self):
        return self.username
    
    @property
    def password(self):
        return None


    @password.setter
    def password(self,password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self,password):
        return bcrypt.check_password_hash(self.password_hash, password)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String)
    phone = db.Column(db.String)
    short_info = db.Column(db.String)
    experience = db.Column(db.Integer)
    preferred_position = db.Column(db.String)
    user = db.relationship(User, backref=db.backref('users', lazy='dynamic'))
    user_name = db.Column(db.String, db.ForeignKey('users.username'))