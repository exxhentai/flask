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

    def test_search(self):
        rv = self.app.post('/api/searchByWords')
        assert b'Not Implemented' in rv.data

    def test_get_full_tag_list(self):
        rv = self.app.get('/api/getFullTagList')
        assert b'Not Implemented' in rv.data


if __name__ == '__main__':
    unittest.main()
