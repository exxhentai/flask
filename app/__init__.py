from flask import Flask
from app import search, get_detail_using_gid
import config
from app.views.api import api


def create_app(config_file=config.Config):
    app = Flask(__name__)
    app.config.from_object(config_file)
    app.register_blueprint(api)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    return app

