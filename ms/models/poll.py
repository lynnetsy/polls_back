import datetime
import uuid
from ms.db import db


class Poll(db.Model):
    __tablename__ = 'polls'

    _fillable = (
        "email",
        "range_age",
        "gender",
        "favsn",
        "tfb",
        "twa",
        "ttw",
        "tins",
        "ttik",
    )

    id = db.Column(
        db.String(length=36),
        default=lambda: str(uuid.uuid4()),
        primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    range_age = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    favsn = db.Column(db.String(20), nullable=False)
    tfb = db.Column(db.Integer, nullable=False)
    twa = db.Column(db.Integer, nullable=False)
    ttw = db.Column(db.Integer, nullable=False)
    tins = db.Column(db.Integer, nullable=False)
    ttik = twa = db.Column(db.Integer, nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False)

    def __init__(self, data):
        self.setAttrs(data)

    def __repr__(self):
        return f"<Poll {self.id} {self.email}>"
