from .db import db, BaseModel


class Mall(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey("account.id", ondelete="CASCADE"), nullable=False)
    units = db.relationship('Unit', backref='mall', lazy=True, cascade="all,delete,delete-orphan")
