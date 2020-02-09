from digeiz_api.models import Account, Mall, Unit
from marshmallow_sqlalchemy import ModelSchema


class AccountSchema(ModelSchema):
    class Meta:
        model = Account


class MallSchema(ModelSchema):
    class Meta:
        model = Mall


class UnitSchema(ModelSchema):
    class Meta:
        model = Unit
