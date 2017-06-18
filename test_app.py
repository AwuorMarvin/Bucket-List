"""Importing the python unittest library"""
import unittest
from app import app

class BucketListTestCase(unittest.TestCase):
    """Testcases for the different aspects of the app"""
    def test_if_index_page_loads(self):
        """Testing the actual page rendered is the home page"""
        actual = app.test_client(self)
        expected = actual.get('/', content_type='html/text')
        self.assertTrue(b'Welcome to the Bucket' in expected.data, msg="Check home page")

    def test_response_from_login(self):
        """Testing response from rendering login page"""
        actual = app.test_client(self)
        expected = actual.get('/login', content_type='html/text')
        self.assertEqual(expected.status_code, 200)

    def test_if_login_page_loads(self):
        """Testing the actual page rendered is the login page"""
        actual = app.test_client(self)
        expected = actual.get('/login', content_type='html/text')
        self.assertTrue(b'Log In' in expected.data, msg="The login page does not load correctly")

    def test_missing_templates_status(self):
        """Testing if the custom 404 page loads for non-existent paths"""
        actual = app.test_client(self)
        expected = actual.get('/missing_view', content_type='html/text')
        self.assertEqual(expected.status_code, 404)

    def test_custom_404_page_loads(self):
        """Testing if the custom 404 page loads for non-existent paths"""
        actual = app.test_client(self)
        expected = actual.get('/missing_view', content_type='html/text')
        self.assertTrue(b'Oh no...' in expected.data, msg="Check custom 404 page")
