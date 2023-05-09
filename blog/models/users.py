from sqlalchemy import Column, Integer, String, Boolean
from blog.app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)
    password = db.Column(db.String(255))

    # def __repr__(self):
    #     return f'<User #{self.id} {self.username}'
