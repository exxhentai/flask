from app.connect_database import Connect
from flask import jsonify
from app.request_error import RequestError


class IPFSHash(object):
    def __init__(self):
        self.connection = Connect.get_connection()

    def update_hash_folder_from_gid(self, gid, ipfs_hash):
        # 测试参数是否合法
        if gid == '':
            # 如果没有相应参数则返回错误，JSON 格式
            request_error = RequestError('gid').required_parameter_not_found()
            return jsonify({'success': False, 'error': request_error})
        elif ipfs_hash == '':
            request_error = RequestError('ipfs_hash').required_parameter_not_found()
            return jsonify({'success': False, 'error': request_error})
        if isinstance(gid,int):
            gid = str(gid)

        result = self.connection.Gallery.update_one(
            {"ex.gid": gid},
            {"$set": {"ipfs_url": ipfs_hash}})

        if result.get('matchedCount', 0) == 0:  # 如果没有找到相应记录则返回错误，JSON 格式
            request_error = RequestError().record_not_found()
            return jsonify({'success': False, 'error': request_error})

        return jsonify({'success': True})
