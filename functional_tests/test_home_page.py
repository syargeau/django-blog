"""
End to end functional tests that test the integration of the home page from the users viewpoint.
"""

from django.test import LiveServerTestCase
from selenium import webdriver


class BasicHomePageTest(LiveServerTestCase):
    """
    Tests that we can get a basic home page up and running.
    """

    def setUp(self):
        """
        Initiate every test by setting up the browser.
        """
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """
        Stop every test by quitting the browser.
        """
        self.browser.quit()

    def test_load_home_page(self):
        """
        Test that the home page loads as expected (i.e. with title and header).
        """
        self.browser.get(self.live_server_url)
        # Bob logs into Moto Now Blog, the best site ever! He notices it's title.
        desired_title = 'Moto Now Blog'
        self.assertEqual(self.browser.title, desired_title)
        # Continue testing...
        self.fail('Finish all tests first!')
