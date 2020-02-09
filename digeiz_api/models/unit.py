from .db import db, BaseModel


class Unit(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    mall_id = db.Column(db.Integer, db.ForeignKey("mall.id", ondelete="CASCADE"), nullable=False)
