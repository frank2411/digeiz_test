from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise

    def delete(self):
        db.session.delete(self)
        db.session.commit()
