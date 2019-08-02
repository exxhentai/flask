from flask import Blueprint, request
from app import search, get_detail_using_gid, get_tag_list

api = Blueprint('api', __name__)


@api.route('/api/searchByWords', methods=['POST'])
def search_by_words():
    """ 主要搜索API """
    input_json = request.get_json(force=True, silent=True) or {}
    words = input_json.get('word', '')
    #: (optional) 搜索的关键字，如果为空则返回所有结果
    tag_list = input_json.get('tags', [])
    #: (optional) 搜索的Tags，格式为List<Str>
    limit = input_json.get('limit', 25)
    #: (optional) 搜索的结果数，默认25
    page = input_json.get('page', 0)
    #: (optional) 第几页的内容，默认0
    filtered_category = input_json.get('filtered', [])
    #: (optional) 不包含的分类，格式为List<Str>
    minimum_rating = input_json.get('minimum', 0.0)
    #: (optional) 最低评分
    return search.search(words, limit, page, filtered_category, minimum_rating, tag_list)


@api.route('/api/getDetail')
def get_detail():
    gid = request.args.get('gid')
    return get_detail_using_gid.get_detail_using_gid(gid)


@api.route('/api/getFullTagList')
def get_full_tag_list():
    return get_tag_list.get_tag_list()
