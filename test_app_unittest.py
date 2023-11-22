import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/hello')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'World!')

    def test_favorites_valid_topic(self):
        response = self.app.get('/favorites?topic=animal')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "Kevin's Favorite animal is 'dog'!")

    def test_favorites_invalid_topic(self):
        response = self.app.get('/favorites?topic=invalid_topic')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('error', data)

    def test_joke(self):
        response = self.app.get('/joke')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('joke', data)


if __name__ == '__main__':
    unittest.main()
