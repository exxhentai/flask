from app.connect_database import Connect
from flask import jsonify, abort
from app.request_error import RequestError


class IPFSHash(object):
    def __init__(self):
        self.connection = Connect.get_connection()

    def update_hash_folder_from_gid(self, gid, ipfs_hash):
        # 测试参数是否合法
        if gid == '':
            # 如果没有相应参数则返回错误，JSON 格式
            request_error = RequestError('gid').required_parameter_not_found()
            return jsonify({'msg': request_error}), 400
        elif ipfs_hash == '':
            request_error = RequestError('ipfs_hash').required_parameter_not_found()
            return jsonify({'msg': request_error}), 400
        if isinstance(gid, int):
            gid = str(gid)

        result = self.connection.Gallery.update_one(
            {"ex.gid": gid},
            {"$set": {"ipfs_url": ipfs_hash}})

        if result.matched_count == 0:  # 如果没有找到相应记录则返回错误，JSON 格式
            request_error = RequestError().record_not_found()
            return jsonify({'msg': request_error}), 400

        return jsonify({'success': True})

    def update_image_hash_from_gid(self, gid, ipfs_hash_list):
        # 测试参数是否合法
        if gid == '':
            # 如果没有相应参数则返回错误，JSON 格式
            request_error = RequestError('gid').required_parameter_not_found()
            return jsonify({'msg': request_error}), 400
        elif ipfs_hash_list is None:
            request_error = RequestError('ipfs_hash_list').required_parameter_not_found()
            return jsonify({'msg': request_error}), 400
        elif not all(isinstance(elem, str) for elem in ipfs_hash_list):
            request_error = RequestError('ipfs_hash_list').required_parameter_not_found()
            return jsonify({'msg': request_error}), 400
        if isinstance(gid, int):
            gid = str(gid)

        result = self.connection.Gallery.update_one(
            {"ex.gid": gid},
            {"$set": {"ipfs_image_list": ipfs_hash_list}})

        if result.matched_count == 0:  # 如果没有找到相应记录则返回错误，JSON 格式
            request_error = RequestError().record_not_found()
            return jsonify({'msg': request_error}), 400

        return jsonify({'success': True})
