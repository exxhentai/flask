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


    @app.route('/api/searchByWords')
    def search_by_words():
        """ 主要搜索API """
        words = request.args.get('wd')
        #: (optional) 搜索的关键字，如果为空则返回所有结果
        limit = request.args.get('lim')
        #: (optional) 搜索的结果数，默认25
        page = request.args.get('pg')
        #: (optional) 第几页的内容，默认1
        filtered_category = request.args.get('fc')
        #: (optional) 不包含的分类
        minimum_rating = request.args.get('mr')
        #: (optional) 最低评分
        return search.search(words, limit, page, filtered_category, minimum_rating)

    return app
