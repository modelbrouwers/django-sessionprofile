from django.db import models
from django.test import override_settings

from django_webtest import WebTest

from sessionprofile.backends import get_backend
from sessionprofile.backends.db import SessionProfileStore
from sessionprofile.models import SessionProfile
from .factories import UserFactory, SuperUserFactory, SessionProfileFactory


@override_settings(
    SESSIONPROFILE_BACKEND='sessionprofile.backends.db',
    SESSION_SAVE_EVERY_REQUEST=True
)
class DBTests(WebTest):

    def _request_page(self, user=None, status_code=200):
        response = self.app.get('/admin/', user=user)
        self.assertEqual(response.status_code, status_code)

    def test_backend(self):
        """
        Test that the model `sessionprofile.SessionProfile` is installed.
        """
        backend = get_backend()
        self.assertEqual(backend, SessionProfileStore)

        self.assertTrue(issubclass(SessionProfile, models.Model),
                        'SessionProfile is not a model')
        # test that we can query it
        self.assertEqual(SessionProfile.objects.count(), 0)

    def test_sessionprofile_created_anon(self):
        """
        Test that an instance is saved in the database for an anonymous user.
        """
        sps = SessionProfile.objects.all()
        self.assertEqual(sps.count(), 0)

        # anonymous
        self._request_page(status_code=302)
        self.assertIn('sessionid', self.app.cookies)

        sessionid = self.app.cookies.get('sessionid')
        sps = SessionProfile.objects.filter(session_key=sessionid)
        self.assertEqual(sps.count(), 1)
        sp = sps.get()
        self.assertIsNone(sp.user)

    def test_sessionprofile_created(self):
        """
        Test that an instance is saved in the database for an authenticated user.
        """
        sps = SessionProfile.objects.all()
        self.assertEqual(sps.count(), 0)

        # superuser (logged in)
        user = SuperUserFactory.create()
        self._request_page(user=user)
        self.assertIn('sessionid', self.app.cookies)

        sessionid = self.app.cookies.get('sessionid')
        sps = SessionProfile.objects.filter(session_key=sessionid)
        self.assertEqual(sps.count(), 1)
        sp = sps.get()
        self.assertEqual(sp.user, user)

    def test_delete_user(self):
        """
        If the user is deleted, the associated sessionprofile must be deleted
        too.
        """
        SessionProfileFactory.create_batch(2)
        sps = SessionProfile.objects.all()
        self.assertEqual(sps.count(), 2)

        user = SuperUserFactory.create()
        self._request_page(user=user)

        self.assertEqual(sps.count(), 3)

        sp = sps.get(session_key=self.app.cookies['sessionid'])
        self.assertEqual(sp.user, user)

        user.delete()

        self.assertEqual(sps.count(), 2)
        with self.assertRaises(SessionProfile.DoesNotExist):
            sps.get(session_key=self.app.cookies['sessionid'])

    def test_deactivate_user(self):
        """
        If the user is deactivated, the associated sessionprofile must be
        deleted.
        """
        SessionProfileFactory.create_batch(2)
        sps = SessionProfile.objects.all()
        self.assertEqual(sps.count(), 2)

        user = SuperUserFactory.create()
        self._request_page(user=user)

        self.assertEqual(sps.count(), 3)

        sp = sps.get(session_key=self.app.cookies['sessionid'])
        self.assertEqual(sp.user, user)

        user.is_active = False
        user.save()

        self.assertEqual(sps.count(), 2)
        with self.assertRaises(SessionProfile.DoesNotExist):
            sps.get(session_key=self.app.cookies['sessionid'])

    def test_incorrect_user(self):
        """
        Test scenario's where an incorrect user is linked to a session id.
        """
        user = SuperUserFactory.create()
        user2 = UserFactory.create()
        self._request_page(user=user)

        sessionid = self.app.cookies['sessionid']
        SessionProfile.objects.filter(session_key=sessionid).update(user=user2)

        self.assertFalse(SessionProfile.objects.filter(user=user).exists())

        with self.assertNumQueries(9):
            self._request_page(user=user)
        sp = SessionProfile.objects.get(session_key=sessionid)
        self.assertEqual(sp.user, user)

        # check that nothing is done when the same user makes a request again
        with self.assertNumQueries(8):
            self._request_page(user=user)

    def test_incorrect_user_anon(self):
        """
        Test scenario's where an incorrect user is linked to a session id.
        """
        user = UserFactory.create()
        self._request_page(status_code=302)
        sessionid = self.app.cookies['sessionid']

        SessionProfile.objects.filter(session_key=sessionid).update(user=user)
        self._request_page(status_code=302)
        sp = SessionProfile.objects.get(session_key=sessionid)
        self.assertIsNone(sp.user)
