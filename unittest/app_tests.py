import uwsgi
import unittest


class AppTestCase(unittest.TestCase):

    def setUp(self):
        uwsgi.app.config['TESTING'] = True
        self.app = uwsgi.app.test_client()

    def tearDown(self):
        pass

    def test_search(self):
        rv = self.app.post('/api/searchByWords')
        assert b'Not Implemented' in rv.data


if __name__ == '__main__':
    unittest.main()
