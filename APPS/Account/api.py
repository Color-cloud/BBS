from flask_restful import Resource, fields, marshal_with

# 数据json数据格式
# 第一步定义数据格式
from APPS.Account.models import User

stu_fields = {
    's_id': fields.Integer,
    's_age': fields.Integer,
    's_name': fields.String,
}
cou_fields = {
    's_id_id': fields.Integer,
    'c_name': fields.String,
}
wwww = {
    'stus': fields.List(fields.Nested(stu_fields)),
    'cous': fields.List(fields.Nested(cou_fields)),
}
result = {
    'status': fields.Integer(),
    'msg': fields.String,
    # "data": fields.List(fields.Nested(wwww)),
    'data':fields.List(fields.Nested(cou_fields)),
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
        cous = User.query.filter(User.u_id==1).first()
        qw = cous.students
        print(123)
        return {'status': 200, 'msg': 'success', 'data': qw}
