from flask import Flask
from .. import config


def create_app(config_file=config.Config):
    app = Flask(__name__)
    app.config.from_object(config_file)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

