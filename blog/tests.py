"""
Unit test our blog app.
"""

from django.test import TestCase

class SmokeTest(TestCase):
    """
    Deliberately failing test to initiate our testing.
    """

    def test_smoke_failure(self):
        """
        Test that deliberately fails.
        """
        self.fail("We must write our tests!")
