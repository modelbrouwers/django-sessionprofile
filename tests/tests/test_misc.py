import unittest


class MiscTests(unittest.TestCase):

    def test_get_version(self):
        from sessionprofile import VERSION, get_version
        self.assertIsInstance(VERSION, tuple)
        get_version()
