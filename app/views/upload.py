from flask import Blueprint, request, jsonify
from app.ipfs_hash import IPFSHash
from app.request_error import RequestError
from bson.objectid import ObjectId

upload = Blueprint('upload', __name__)


# Authentication Required
@upload.route('/upload/setIPFSFolderHash', methods=['POST'])
def set_IPFS_folder_hash_by_gid():
    request_json = request.get_json(force=True, silent=True) or {}
    ipfs_hash = request_json.get('ipfs_hash', '')
    #: 需要添加的 IPFS Hash 资料夹
    gid = request_json.get('gid', '')
    #: 作品的Ex Gid
    if gid:
        result = IPFSHash().update_hash_folder('ex.gid', gid, ipfs_hash)
        return result
    hash_id = request_json.get('id', '')
    #: 作品的数据库Hash id
    if hash_id:
        hash_id = ObjectId(hash_id)
        result = IPFSHash().update_hash_folder('_id', hash_id, ipfs_hash)
        return result
    return jsonify({'msg': RequestError().no_unique_parameter()}), 400


# Authentication Required
@upload.route('/upload/setIPFSImageHash', methods=['POST'])
def set_IPFS_image_hash_by_gid():
    request_json = request.get_json(force=True, silent=True) or {}
    ipfs_hash_list = request_json.get('ipfs_hash_list', None)
    #: 需要添加的 IPFS Hash 列表, list 格式
    gid = request_json.get('gid', '')
    #: 作品的Ex Gid
    if gid:
        result = IPFSHash().update_image_hash('ex.gid', gid, ipfs_hash_list)
        return result
    hash_id = request_json.get('id', '')
    #: 作品的数据库Hash id
    if hash_id:
        hash_id = ObjectId(hash_id)
        result = IPFSHash().update_image_hash('_id', hash_id, ipfs_hash_list)
        return result
    return jsonify({'msg': RequestError().no_unique_parameter()}), 400
