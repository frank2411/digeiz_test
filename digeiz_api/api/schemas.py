from digeiz_api.models import Account, Mall, Unit
from digeiz_api.models.db import db
from marshmallow_sqlalchemy import ModelSchema


class AccountSchema(ModelSchema):
    class Meta:
        model = Account
        sqla_session = db.session


class MallSchema(ModelSchema):
    class Meta:
        model = Mall
        sqla_session = db.session


class UnitSchema(ModelSchema):
    class Meta:
        model = Unit
        sqla_session = db.session
