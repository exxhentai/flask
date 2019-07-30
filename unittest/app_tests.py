import app
import unittest


class AppTestCase(unittest.TestCase):

    def setUp(self):
        application = app.create_app()
        application.config['TESTING'] = True
        self.app = application.test_client()

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
