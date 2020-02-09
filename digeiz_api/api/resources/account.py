from flask import request
from flask_restful import Resource

from digeiz_api.api.schemas import AccountSchema
from digeiz_api.models import Account

from marshmallow import ValidationError


class Accounts(Resource):

    def get(self):
        schema = AccountSchema(many=True)
        accounts = Account.query.all()
        return {"accounts": schema.dump(accounts)}, 200

    def post(self):
        schema = AccountSchema()

        try:
            account = schema.load(request.json)
        except ValidationError as err:
            return err.messages, 422

        account.save()
        return {'message': 'Account created', 'account': schema.dump(account)}, 201


class AccountsDetail(Resource):

    def get(self, account_id):
        schema = AccountSchema()
        account = Account.query.filter_by(id=account_id).one_or_none()

        # For better readibility I could move this logic inside a staticmethod in the model
        if not account:
            return {"message": "Account not found"}, 404

        return {"account": schema.dump(account)}, 200

    def delete(self, account_id):
        account = Account.query.filter_by(id=account_id).one_or_none()

        if not account:
            return {"message": "Account not found"}, 404

        account.delete()

        return {"message": "Account deleted"}, 204
