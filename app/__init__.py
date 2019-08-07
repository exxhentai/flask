from flask import Flask, request
from app import search, get_detail_using_gid
import config
from app.views.api import api
from app.views.upload import upload


def create_app(config_file=config.Config):
    app = Flask(__name__)
    app.config.from_object(config_file)
    app.register_blueprint(api)
    app.register_blueprint(upload)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        if request.method == 'OPTIONS':
            response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
            headers = request.headers.get('Access-Control-Request-Headers')
            if headers:
                response.headers['Access-Control-Allow-Headers'] = headers
        return response

    return app

