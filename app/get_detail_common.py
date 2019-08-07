from app.connect_database import Connect
from flask import jsonify, abort
from app.request_error import RequestError


def get_detail_common(variable_name, variable_value):
    if isinstance(variable_value, int):
        variable_value = str(variable_value)

    connection = Connect.get_connection()
    query_result: dict = connection.Gallery.find_one({variable_name: variable_value})
    if not query_result:
        return jsonify({})
    query_result['_id'] = str(query_result['_id'])
    return jsonify(query_result)
