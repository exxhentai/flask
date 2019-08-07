import uwsgi
import unittest
from app.request_error import RequestError
import random
from werkzeug.exceptions import HTTPException


# TODO: Write more tests for this.
class AppTestCase(unittest.TestCase):

    def setUp(self):
        uwsgi.app.config['TESTING'] = True
        self.app = uwsgi.app.test_client()

    def tearDown(self):
        pass

    def test_update_ipfs_image_list_hash(self):
        # 上传 IPFS 图片 Hash 列表
        # 测试一个存在的Gid
        valid_gid = '1452710'
        ipfs_hash_list = [hex(random.getrandbits(128)) for _ in range(1, 10)]
        rv = self.app.post('/upload/setIPFSImageHash', json={'gid': valid_gid, 'ipfs_hash_list': ipfs_hash_list})
        json_response = rv.json
        assert json_response['success'] is True

        verify_record_json = self.app.get('/api/getDetail?gid=' + valid_gid).json
        assert verify_record_json['ipfs_image_list'] == ipfs_hash_list


if __name__ == '__main__':
    unittest.main()