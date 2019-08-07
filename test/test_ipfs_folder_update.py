import uwsgi
import unittest
from app.request_error import RequestError
import random
from werkzeug.exceptions import HTTPException


class AppTestCase(unittest.TestCase):

    def setUp(self):
        uwsgi.app.config['TESTING'] = True
        self.app = uwsgi.app.test_client()

    def tearDown(self):
        pass

    def test_update_ipfs_folder_hash_via_gid(self):
        # 上传 IPFS 资料夹 Hash
        # 测试一个存在的Gid
        valid_gid = '1452710'
        ipfs_hash = hex(random.getrandbits(128))
        rv = self.app.post('/upload/setIPFSFolderHash', json={'gid': valid_gid, 'ipfs_hash': ipfs_hash})
        json_response = rv.json
        assert json_response['success'] is True

        verify_record_json = self.app.get('/api/getDetail?gid=' + valid_gid).json
        assert verify_record_json['ipfs_url'] == ipfs_hash

    def test_update_ipfs_folder_hash_via_hash_id(self):
        # 上传 IPFS 资料夹 Hash
        # 测试一个存在的Hash ID
        valid_hash_id = '5d43fcd769ada8455ce26774'
        ipfs_hash = hex(random.getrandbits(128))
        rv = self.app.post('/upload/setIPFSFolderHash', json={'id': valid_hash_id, 'ipfs_hash': ipfs_hash})
        json_response = rv.json
        assert json_response['success'] is True

        verify_record_json = self.app.get('/api/getDetail?id=' + valid_hash_id).json
        assert verify_record_json['ipfs_url'] == ipfs_hash

    def test_update_ipfs_folder_hash_via_invalid_hash_id(self):
        # 上传 IPFS 资料夹 Hash
        # 测试一个不存在的Hash ID
        valid_hash_id = '9d43fcd769ada8455ce26774'
        ipfs_hash = hex(random.getrandbits(128))
        rv = self.app.post('/upload/setIPFSFolderHash', json={'id': valid_hash_id, 'ipfs_hash': ipfs_hash})
        json_response = rv.json
        assert self.assertRaises(HTTPException)
        assert json_response['msg'] == RequestError().record_not_found()

    def test_update_ipfs_folder_hash_via_illegal_hash_id(self):
        # 上传 IPFS 资料夹 Hash
        # 测试一个非法的Hash ID
        valid_hash_id = '2333'
        ipfs_hash = hex(random.getrandbits(128))
        rv = self.app.post('/upload/setIPFSFolderHash', json={'id': valid_hash_id, 'ipfs_hash': ipfs_hash})
        json_response = rv.json
        assert self.assertRaises(HTTPException)
        assert json_response['msg'] == RequestError().invalid_hash_id()

    def test_update_ipfs_folder_hash_non_exist_gid(self):
        # 上传 IPFS 资料夹 Hash
        # 测试一个不存在的Gid
        invalid_gid = '99999999999'
        ipfs_hash = hex(random.getrandbits(128))
        rv = self.app.post('/upload/setIPFSFolderHash', json={'gid': invalid_gid, 'ipfs_hash': ipfs_hash})
        json_response = rv.json
        assert self.assertRaises(HTTPException)
        assert json_response['msg'] == RequestError().record_not_found()

    def test_update_ipfs_folder_hash_no_gid(self):
        # 上传 IPFS 资料夹 Hash
        # 测试不提供 Gid
        ipfs_hash = hex(random.getrandbits(128))
        rv = self.app.post('/upload/setIPFSFolderHash', json={'ipfs_hash': ipfs_hash})
        json_response = rv.json
        assert self.assertRaises(HTTPException)
        assert json_response['msg'] == RequestError().no_unique_parameter()  # 必须返回"参数未找到"

    def test_update_ipfs_folder_hash_no_hash(self):
        # 上传 IPFS 图片 Hash 列表
        # 测试不提供 IPFS Hash
        invalid_gid = '99999999999'
        rv = self.app.post('/upload/setIPFSFolderHash', json={'gid': invalid_gid})
        json_response = rv.json
        assert self.assertRaises(HTTPException)
        assert json_response['msg'] == RequestError('ipfs_hash').required_parameter_not_found()  # 必须返回"参数未找到"


if __name__ == '__main__':
    unittest.main()
