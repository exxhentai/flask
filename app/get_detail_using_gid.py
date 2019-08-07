from app.connect_database import Connect
from flask import jsonify, abort
from app.request_error import RequestError


def get_detail_using_gid(gid):
    if isinstance(gid, int):
        gid = str(gid)
    if gid == '':
        # 如果没有Gid 则返回错误，JSON 格式
        request_error = RequestError('gid').required_parameter_not_found()
        return jsonify({'msg': request_error}), 400

    connection = Connect.get_connection()
    query_result: dict = connection.Gallery.find_one({"ex.gid": gid})
    if not query_result:
        return jsonify({})
    query_result['_id'] = str(query_result['_id'])
    return jsonify(query_result)
