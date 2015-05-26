from django.test import SimpleTestCase

from sessionprofile.backends.base import Base


class MockRequest(object):
    pass


class MockRequest2(object):
    session = 'foo'


class BaseTests(SimpleTestCase):

    def setUp(self):
        self.backend = Base()

    def test_base_methods(self):
        with self.assertRaises(NotImplementedError):
            self.backend.save_session(object())

        with self.assertRaises(NotImplementedError):
            self.backend.purge_for_user(object())

    def test_get_session_store(self):
        request1 = MockRequest()
        request2 = MockRequest2()

        store1 = self.backend.get_session_store(request1)
        self.assertIsNone(store1)

        store2 = self.backend.get_session_store(request2)
        self.assertEqual(store2, 'foo')
