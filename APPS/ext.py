# 第三方扩展插件的配置文件


# ======================数据库配置===================
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


# 配置数据库的参数
def config_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:wwwwwwww1@127.0.0.1:3306/flask_bbs'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 设置请求结束之后自动提交
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


# 配置数据库连接
def init_db(app):
    config_db(app)
    db.init_app(app=app)
    migrate.init_app(app, db)
