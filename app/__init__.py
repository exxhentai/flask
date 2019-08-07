from flask import Flask, request
from app import search, get_detail_using_gid
import config
from app.views.api import api
from app.views.upload import upload
from flask_cors import CORS


def create_app(config_file=config.Config):
    app = Flask(__name__)
    app.config.from_object(config_file)
    app.register_blueprint(api)
    app.register_blueprint(upload)
    CORS(app)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    return app

