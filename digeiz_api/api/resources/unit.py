from flask import request
from flask_restful import Resource

from digeiz_api.api.schemas import UnitSchema
from digeiz_api.models import Unit

from marshmallow import ValidationError


class Units(Resource):

    def get(self):
        schema = UnitSchema(many=True)
        units = Unit.query.all()
        return {"units": schema.dump(units)}, 200

    def post(self):
        schema = UnitSchema(many=True)

        try:
            units = schema.load(request.json)
        except ValidationError as err:
            return err.messages, 422

        schema.session.add_all(units)
        schema.session.commit()

        return {'message': 'Unit created', 'units': schema.dump(units)}, 201


class UnitsDetail(Resource):

    def get(self, unit_id):
        schema = UnitSchema()
        unit = Unit.query.filter_by(id=unit_id).one_or_none()

        # For better readibility I could move this logic inside a staticmethod in the model
        if not unit:
            return {"message": "Unit not found"}, 404

        return {"unit": schema.dump(unit)}, 200

    def delete(self, unit_id):
        unit = Unit.query.filter_by(id=unit_id).one_or_none()

        if not unit:
            return {"message": "Unit not found"}, 404

        unit.delete()

        return {"message": "Unit deleted"}, 204
