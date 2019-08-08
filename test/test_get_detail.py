import uwsgi
import unittest
from app.request_error import RequestError
from werkzeug.exceptions import HTTPException


class GetDetailTestCase(unittest.TestCase):

    def setUp(self):
        uwsgi.app.config['TESTING'] = True
        self.app = uwsgi.app.test_client()

    def tearDown(self):
        pass

    def test_get_detail(self):
        # 获取作品详细信息
        # 测试一个存在的Gid
        valid_gid = '1452710'
        rv = self.app.get('/view/getDetail?gid=' + valid_gid)
        json_response = rv.json
        assert isinstance(json_response, dict)
        assert isinstance(json_response['title'], str)

    def test_get_detail_hash_id(self):
        # 获取作品详细信息
        # 测试一个存在的Hash ID
        valid_hash_id = '5d43fcd769ada8455ce26772'
        rv = self.app.get('/view/getDetail?id=' + valid_hash_id)
        json_response = rv.json
        assert isinstance(json_response, dict)
        assert isinstance(json_response['title'], str)

    def test_get_detail_title(self):
        # 获取作品详细信息
        # 测试一个存在的title
        title = '[Pixiv] Inoji | Inukami | Inu Hashiru (5992265) [PURGED]'
        rv = self.app.get('/view/getDetail?title=' + title)
        json_response = rv.json
        assert isinstance(json_response, dict)
        assert json_response['ex']['gid'] == '1452708'
        assert isinstance(json_response['title'], str)

    def test_get_detail_japan_title(self):
        # 获取作品详细信息
        # 测试一个存在的日文 title
        title = '[Pixiv] いの字 | 戌かみ | いぬかみ | Inu Hashiru (5992265) [PURGED]'
        rv = self.app.get('/view/getDetail?japanTitle=' + title)
        json_response = rv.json
        assert isinstance(json_response, dict)
        assert json_response['ex']['gid'] == '1452708'
        assert isinstance(json_response['title'], str)

    def test_get_detail_non_exist_gid(self):
        # 获取作品详细信息
        # 测试一个不存在的Gid
        invalid_gid = '99999999999'
        rv = self.app.get('/view/getDetail?gid=' + invalid_gid)
        json_response = rv.json
        assert json_response == {}  # 必须返回空List

    def test_get_detail_no_gid(self):
        # 获取作品详细信息
        # 测试不提供Gid
        invalid_gid = ''
        rv = self.app.get('/view/getDetail?gid=' + invalid_gid)
        json_response = rv.json
        assert self.assertRaises(HTTPException)
        assert json_response['msg'] == RequestError().no_unique_parameter()  # 必须返回"参数未找到"


if __name__ == '__main__':
    unittest.main()