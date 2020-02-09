from flask import request
from flask_restful import Resource

from digeiz_api.api.schemas import MallSchema
from digeiz_api.models import Mall

from marshmallow import ValidationError


class Malls(Resource):

    def get(self):
        schema = MallSchema(many=True)
        malls = Mall.query.all()
        return {"malls": schema.dump(malls)}, 200

    def post(self):
        schema = MallSchema()

        try:
            mall = schema.load(request.json)
        except ValidationError as err:
            return err.messages, 422

        mall.save()
        return {'message': 'Mall created', 'mall': schema.dump(mall)}, 201


class MallsDetail(Resource):

    def get(self, mall_id):
        schema = MallSchema()
        mall = Mall.query.filter_by(id=mall_id).one_or_none()

        # For better readibility I could move this logic inside a staticmethod in the model
        if not mall:
            return {"message": "Mall not found"}, 404

        return {"mall": schema.dump(mall)}, 200

    def delete(self, mall_id):
        mall = Mall.query.filter_by(id=mall_id).one_or_none()

        if not mall:
            return {"message": "Mall not found"}, 404

        mall.delete()

        return {"message": "Mall deleted"}, 204
