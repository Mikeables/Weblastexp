from flask import Blueprint
from flask_restful import Api

#创建蓝图对象
user = Blueprint('user',__name__,url_prefix='/user')

user_api = Api(user)

from flask_shopping.user import view