from flask import Flask
import config
from app import search, get_detail_using_gid
from app.views.api import api
# from flask_pymongo import PyMongo


def create_app(config_file=config.Config):
    app = Flask(__name__)
    app.config.from_object(config_file)
    # mongo = PyMongo(app)
    app.register_blueprint(api)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    return app
