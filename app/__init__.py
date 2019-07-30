from flask import Flask, request
import config
from app import search
from flask_pymongo import PyMongo


def create_app(config_file=config.Config):
    app = Flask(__name__)
    app.config.from_object(config_file)
    mongo = PyMongo(app)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    @app.route('/api/searchByWords', methods=['POST'])
    def search_by_words():
        form = request.form
        return search.search(form)

    return app
