from flask_restful import Api

from APPS.Account.api import  Test

api = Api()


def init_api(app):
    api.init_app(app)


# 注册路由系统
api.add_resource(Test, "/")
