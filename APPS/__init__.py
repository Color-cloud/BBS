from flask import Flask

from APPS.ext import init_db
from APPS.urls import init_api


def create_app():
    app = Flask(__name__)
    app.debug = True
    init_api(app)
    init_db(app)
    return app
