from flask import Blueprint
from flask_restful import Api

from digeiz_api.api.resources import Accounts, AccountsDetail, Malls, MallsDetail, Units, UnitsDetail

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(api_blueprint)
api.add_resource(Accounts, '/accounts')
api.add_resource(AccountsDetail, '/accounts/<int:account_id>')
api.add_resource(Malls, '/malls')
api.add_resource(MallsDetail, '/malls/<int:mall_id>')
api.add_resource(Units, '/units')
api.add_resource(UnitsDetail, '/units/<int:unit_id>')
