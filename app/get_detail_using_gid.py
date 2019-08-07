from app.connect_database import Connect
from flask import jsonify, abort
from app.request_error import RequestError


def get_detail_using_gid(gid):
    if isinstance(gid, int):
        gid = str(gid)
    if gid == '':
        # 如果没有Gid 则返回错误，JSON 格式
        request_error = RequestError('gid').required_parameter_not_found()
        abort(400, request_error)

    connection = Connect.get_connection()
    query_result: dict = connection.Gallery.find_one({"ex.gid": gid})
    if not query_result:
        request_error = RequestError().record_not_found()
        abort(404, request_error)
    query_result['_id'] = str(query_result['_id'])
    return jsonify(query_result)
