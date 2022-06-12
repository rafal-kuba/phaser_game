from enum import unique
# from app import login_manager
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import uuid

db = SQLAlchemy()

# class User(UserMixin, db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     timestamp = db.Column(db.DateTime(timezone=True), default=datetime.utcnow())
#     email = db.Column(db.String(128), unique=True, index=True)
#     username = db.Column(db.String(128), unique=True, index=True)
#     password = db.Column(db.String(128))
#     password_hash = db.Column(db.String(128))
#     user_session_id = db.String(64) # Unique to each session. Destroyed when user log out. 
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

#     @property
#     def password(self):
#         raise AttributeError("Can't read your password attribute")

#     @password.setter
#     def password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def verify_password(self, password):
#         return check_password_hash(self.password_hash, password)

#     def get_id(self):
#         return self.user_session_id

#     def update_session(self):
#         self.user_session_id = str(uuid.uuid4())
#         db.session.commit()

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     default = db.Column(db.Boolean, default=False, index=True)
#     permissions = db.Column(db.Integer)
#     users = db.relationship('User', backref='role', lazy='dynamic')

#     def __init__(self, **kwargs):
#         super(Role, self).__init__(**kwargs)
#         if self.permissions is None:
#             self.permissions = 0

# def _create_tables():
#     from app import create_app
#     app = create_app('development')
#     with app.app_context():
#         db.create_all()