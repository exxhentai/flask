import uwsgi
import unittest
from app.request_error import RequestError
import random


class AppTestCase(unittest.TestCase):

    def setUp(self):
        uwsgi.app.config['TESTING'] = True
        self.app = uwsgi.app.test_client()

    def tearDown(self):
        pass

    def test_search(self):
        rv = self.app.post('/api/searchByWords')
        assert b'Not Implemented' in rv.data

    def test_get_detail(self):
        # 测试一个存在的Gid
        valid_gid = '1452710'
        rv = self.app.get('/api/getDetail?gid=' + valid_gid)
        json_response = rv.json
        assert isinstance(json_response, dict)
        assert isinstance(json_response['title'], str)

    def test_get_detail_non_exist_gid(self):
        # 测试一个不存在的Gid
        invalid_gid = '99999999999'
        rv = self.app.get('/api/getDetail?gid=' + invalid_gid)
        json_response = rv.json
        assert json_response == RequestError().record_not_found()  # 必须返回"条目不存在"

    def test_get_detail_no_gid(self):
        # 测试不提供Gid
        invalid_gid = ''
        rv = self.app.get('/api/getDetail?gid=' + invalid_gid)
        json_response = rv.json
        assert json_response == RequestError('gid').required_parameter_not_found()  # 必须返回"参数未找到"

    def test_update_ipfs_folder_hash(self):
        # 测试一个存在的Gid
        valid_gid = '1452710'
        ipfs_hash = hex(random.getrandbits(128))
        rv = self.app.post('/upload/setIPFSFolderHashByGid', json={'gid': valid_gid, 'ipfs_hash': ipfs_hash})
        json_response = rv.json
        assert json_response['success'] is True

        verify_record_json = self.app.get('/api/getDetail?gid=' + valid_gid).json
        assert verify_record_json['ipfs_url'] == ipfs_hash

    def test_update_ipfs_folder_hash_non_exist_gid(self):
        # 测试一个不存在的Gid
        invalid_gid = '99999999999'
        ipfs_hash = hex(random.getrandbits(128))
        rv = self.app.post('/upload/setIPFSFolderHashByGid', json={'gid': invalid_gid, 'ipfs_hash': ipfs_hash})
        json_response = rv.json
        assert json_response['error'] == RequestError().record_not_found()  # 必须返回"条目不存在"

    def test_update_ipfs_folder_hash_no_gid(self):
        # 测试不提供 Gid
        ipfs_hash = hex(random.getrandbits(128))
        rv = self.app.post('/upload/setIPFSFolderHashByGid', json={'ipfs_hash': ipfs_hash})
        json_response = rv.json
        assert json_response['error'] == RequestError('gid').required_parameter_not_found()  # 必须返回"参数未找到"

    def test_update_ipfs_folder_hash_no_hash(self):
        # 测试不提供 IPFS Hash
        invalid_gid = '99999999999'
        rv = self.app.post('/upload/setIPFSFolderHashByGid', json={'gid': invalid_gid})
        json_response = rv.json
        assert json_response['error'] == RequestError('ipfs_hash').required_parameter_not_found()  # 必须返回"参数未找到"

    def test_get_full_tag_list(self):
        rv = self.app.get('/api/getFullTagList')
        assert b'Not Implemented' in rv.data


if __name__ == '__main__':
    unittest.main()
