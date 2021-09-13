from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime(timezone=True), default=datetime.utcnow())
    email_address = db.Column(db.String(128))
    username = db.Column(db.String(128))
    password = db.Column(db.String(128))

def _create_tables():
    from app import create_app
    app = create_app('development')
    with app.app_context():
        db.create_all()