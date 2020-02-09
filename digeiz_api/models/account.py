from .db import db, BaseModel


class Account(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    malls = db.relationship('Mall', backref='account', lazy=True, cascade="all,delete,delete-orphan")
