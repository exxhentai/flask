from flask import Blueprint, request, jsonify
from app.update_ipfs_hash import IPFSHash
from app.request_error import RequestError

upload = Blueprint('upload', __name__)


@upload.route('/upload/setIPFSFolderHashByGid', methods=['POST'])
def set_IPFS_folder_hash_by_gid():
    request_json = request.get_json(force=True, silent=True) or {}
    gid = request_json.get('gid', '')
    #: 作品的Ex Gid
    ipfs_hash = request_json.get('ipfs_hash', '')
    #: 需要添加的 IPFS Hash 资料夹

    print(request_json)

    result = IPFSHash().update_hash_folder_from_gid(gid, ipfs_hash)
    return result
