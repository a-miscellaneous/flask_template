from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import relationship


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    password_hash = db.Column(db.String(150))
    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())
