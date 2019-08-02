from flask import Blueprint, request
from app import search, get_detail_using_gid

api = Blueprint('api', __name__)


@api.route('/api/searchByWords', methods=['POST'])
def search_by_words():
    """ 主要搜索API """
    json = request.get_json()
    words = json['word']
    #: (optional) 搜索的关键字，如果为空则返回所有结果
    tag_list = json['tags']
    #: (optional) 搜索的Tags，格式为Array<Str>
    limit = json['lim']
    #: (optional) 搜索的结果数，默认25
    page = json['pg']
    #: (optional) 第几页的内容，默认1
    filtered_category = json['filtered']
    #: (optional) 不包含的分类
    minimum_rating = json['minimum']
    #: (optional) 最低评分
    return search.search(words, limit, page, filtered_category, minimum_rating, tag_list)


@api.route('/api/getDetail')
def get_detail():
    gid = request.args.get('gid')
    return get_detail_using_gid.get_detail_using_gid(gid)
