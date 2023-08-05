from src.database import db

import random
from datetime import datetime

class Movie(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'))
    name        = db.Column(db.Text, nullable=False)
    slug        = db.Column(db.Text, nullable=False)
    short_desc  = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    release_date = db.Column(db.String(20), nullable=False)
    rating      = db.Column(db.Integer, nullable=True)
    created_at  = db.Column(db.DateTime, default=datetime.now())
    updated_at  = db.Column(db.DateTime, onupdate=datetime.now())

    def generate_slug(self):
        name = self.query.filter_by(name=self.name).first()  # Get value from the Query
        sorting_name    = self.name.replace(' ', '-')    # segregration from the space and replay by dash [ - ]
        random_number   = str(random.randint(0, 9999999999)) # The random number generated of the length of 0 to 999999999
        # new_sorting_name  = '-'.join(name)
        slug            = sorting_name + '-' + random_number # join to both name by dash and random number all in together eg : ram-krishna-93242345
        
        return slug

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.slug = self.generate_slug()

    def __repr__(self) -> str:
        return 'Movie>>>{self.name}'
