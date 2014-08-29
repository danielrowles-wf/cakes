"""
Tests for `cakes.util`.
"""
import unittest
from cakes import util

class CakesTestCase(unittest.TestCase):
    """
    Base tests for the `cakes.util` script.
    """
    def test_no_crash(self):
        """
        We should be able to say hello and not crash
        """
        ret = cakes.say_hello()
        self.assertIsNone(ret)
