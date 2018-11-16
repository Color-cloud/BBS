from flask_restful import Resource, fields, marshal_with

# 数据json数据格式
# 第一步定义数据格式
from APPS.Account.models import User, UserNext

user_fields = {
    'u_id': fields.Integer,
    'username': fields.String,
}
usernext_fields = {
    'n_uid': fields.Integer,
    'n_username': fields.String,
}
wwww = {
    'stus': fields.List(fields.Nested(user_fields)),
    'cous': fields.List(fields.Nested(usernext_fields)),
}
result = {
    'status': fields.Integer(),
    'msg': fields.String,
    # "data": fields.List(fields.Nested(wwww)),
    'data': fields.List(fields.Nested(user_fields)),
}

# 装饰 marshal_with

'''
{
    status:
    msg:
    data:[]
}
'''


class IndexApi(Resource):
    @marshal_with(result)
    def get(self):
        cous = UserNext.query.filter(UserNext.n_uid == 1).first()
        qw = cous.user
        return {'status': 200, 'msg': 'success', 'data': qw}
