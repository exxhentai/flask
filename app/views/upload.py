from flask import Blueprint, request, jsonify
from app.update_ipfs_hash import IPFSHash
from app.request_error import RequestError
from bson.objectid import ObjectId

upload = Blueprint('upload', __name__)


# Authentication Required
@upload.route('/upload/setIPFSFolderHashByGid', methods=['POST'])
def set_IPFS_folder_hash_by_gid():
    request_json = request.get_json(force=True, silent=True) or {}
    gid = request_json.get('gid', '')
    #: 作品的Ex Gid
    ipfs_hash = request_json.get('ipfs_hash', '')
    #: 需要添加的 IPFS Hash 资料夹

    result = IPFSHash().update_hash_folder('ex.gid', gid, ipfs_hash)
    return result


# Authentication Required
@upload.route('/upload/setIPFSFolderHashByHashId', methods=['POST'])
def set_IPFS_folder_hash_by_hash_id():
    request_json = request.get_json(force=True, silent=True) or {}
    hash_id = ObjectId(request_json.get('id', ''))
    #: 作品的Ex Gid
    ipfs_hash = request_json.get('ipfs_hash', '')
    #: 需要添加的 IPFS Hash 资料夹

    result = IPFSHash().update_hash_folder('_id', hash_id, ipfs_hash)
    return result


# Authentication Required
@upload.route('/upload/setIPFSImageHashByGid', methods=['POST'])
def set_IPFS_image_hash_by_gid():
    request_json = request.get_json(force=True, silent=True) or {}
    gid = request_json.get('gid', '')
    #: 作品的Ex Gid
    ipfs_hash_list = request_json.get('ipfs_hash_list', None)
    #: 需要添加的 IPFS Hash 列表, list 格式

    result = IPFSHash().update_image_hash_from_gid(gid, ipfs_hash_list)
    return result
