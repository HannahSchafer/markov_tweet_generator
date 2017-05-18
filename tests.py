from server import app
from unittest import TestCase
import markov



class MyAppUnitTestCase(TestCase):
    """Unit tests"""

    def setUp(self):
        print "(setUp ran)"
        self.client = app.test_client()
        app.config['SECRET_KEY'] = 'key'


    def test_splashpage(self):
        """Tests splashpage rendering."""

        result = self.client.get('/')
        self.assertIn(u'<h2>Markov Tweet Generator</h2>', result.data)



class TwitterAPITests(TestCase):
    """Tests that require a mock API call to Twitter API."""
    
    def setUp(self):
        print "(setUp ran)"
        self.client = app.test_client()
        app.config['SECRET_KEY'] = 'key'


        def _test_connect_twitter_api(twitter_handle):
            """Mocking out Twitter API."""

            connect_twitter_response = pickle.load(open("twitter_data.pickle", "rb"))

            return connect_twitter_response

            markov.connect_twitter_api = _test_connect_twitter_api 


    def test_show_markov_tweet(self):
        """Tests show_markov_tweet route & multiple functions from markov.py.
        """

        result = self.client.get('/show-markov-tweet')
        self.assertEqual(result.status_code, 200)










if __name__ == "__main__":

    import unittest

    unittest.main()
