from src.database import db

# from src.database.bookmark import Bookmark
from src.database.movie import Movie

from datetime import datetime

class User(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    username    = db.Column(db.String(80), unique=True, nullable=False)
    email       = db.Column(db.String(120), unique=True, nullable=False)
    password    = db.Column(db.String(120), nullable=False)
    created_at  = db.Column(db.DateTime, default=datetime.now())
    updated_at  = db.Column(db.DateTime, onupdate=datetime.now())
    movie       = db.relationship(Movie, backref="user")

    def __repr__(self) -> str:
        return 'User>>>{self.username}'
