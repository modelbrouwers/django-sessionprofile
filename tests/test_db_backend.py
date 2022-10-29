from datetime import timedelta

from django.contrib.sessions.models import Session
from django.db import models
from django.utils import timezone

import pytest

from sessionprofile.backends import get_backend
from sessionprofile.backends.db import SessionProfileStore
from sessionprofile.models import SessionProfile

from .factories import (
    SessionFactory,
    SessionProfileFactory,
    SuperUserFactory,
    UserFactory,
)

pytestmark = pytest.mark.django_db


def test_backend(sp_settings):
    """
    Test that the model `sessionprofile.SessionProfile` is installed.
    """
    backend = get_backend()

    assert backend == SessionProfileStore
    assert issubclass(SessionProfile, models.Model), "SessionProfile is not a model"
    assert SessionProfile.objects.count() == 0


def test_sessionprofile_created_anon(client, sp_settings):
    """
    Test that an instance is saved in the database for an anonymous user.
    """
    sps = SessionProfile.objects.all()
    assert not sps.exists()

    # fetch the page as an anonymous user
    client.get("/session/")

    assert "sessionid" in client.cookies
    session_key = client.cookies["sessionid"].value
    sps = SessionProfile.objects.filter(session_key=session_key)
    assert sps.count() == 1
    sp = sps.get()
    assert sp.user is None


def test_sessionprofile_created(client, sp_settings):
    """
    Test that an instance is saved in the database for an authenticated user.
    """
    # superuser (logged in)
    user = SuperUserFactory.create()
    client.force_login(user)
    sps = SessionProfile.objects.all()
    assert not sps.exists()

    client.get("/session/")

    assert "sessionid" in client.cookies
    session_key = client.cookies["sessionid"].value
    sps = SessionProfile.objects.filter(session_key=session_key)
    assert sps.count() == 1
    sp = sps.get()
    assert sp.user == user


def test_delete_user(client, sp_settings):
    """
    If the user is deleted, the associated sessionprofile must be deleted
    too.
    """
    SessionProfileFactory.create_batch(2)
    user = SuperUserFactory.create()
    client.force_login(user)
    sps = SessionProfile.objects.all()

    client.get("/session/")

    assert sps.count() == 3
    session_key = client.cookies["sessionid"].value

    sp = sps.get(session_key=session_key)
    assert sp.user == user

    user.delete()

    assert sps.count() == 2
    assert not sps.filter(session_key=session_key).exists()


def test_deactivate_user(client, sp_settings):
    """
    If the user is deactivated, the associated sessionprofile must be
    deleted.
    """
    SessionProfileFactory.create_batch(2)
    user = SuperUserFactory.create()
    client.force_login(user)
    sps = SessionProfile.objects.all()

    client.get("/session/")

    assert sps.count() == 3
    session_key = client.cookies["sessionid"].value

    sp = sps.get(session_key=session_key)
    assert sp.user == user

    user.is_active = False
    user.save()

    assert sps.count() == 2
    assert not sps.filter(session_key=session_key).exists()


def test_incorrect_user(client, sp_settings, django_assert_num_queries):
    """
    Test scenario's where an incorrect user is linked to a session id.
    """
    user = SuperUserFactory.create()
    user2 = UserFactory.create()
    client.force_login(user)

    client.get("/session/")

    session_key = client.cookies["sessionid"].value
    SessionProfile.objects.filter(session_key=session_key).update(user=user2)

    assert not SessionProfile.objects.filter(user=user).exists()

    with django_assert_num_queries(8):
        client.get("/session/")

    sp = SessionProfile.objects.get(session_key=session_key)
    assert sp.user == user

    # check that nothing is done when the same user makes a request again
    with django_assert_num_queries(7):
        client.get("/session/")


def test_incorrect_user_anon(client, sp_settings):
    """
    Test scenario's where an incorrect user is linked to a session id.
    """
    user = UserFactory.create()
    client.get("/session/")
    session_key = client.cookies["sessionid"].value
    SessionProfile.objects.filter(session_key=session_key).update(user=user)

    client.get("/session/")

    sp = SessionProfile.objects.get(session_key=session_key)
    assert sp.user is None


def test_clear_expired(client, sp_settings):
    sp_settings.SESSION_ENGINE = "django.contrib.sessions.backends.db"
    past = timezone.now() - timedelta(seconds=60)
    session1 = SessionFactory.create(expire_date=past)
    session2 = SessionFactory.create(expire_date=past + timedelta(seconds=2 * 60))

    SessionProfileFactory.create(session_key=session1.session_key)
    SessionProfileFactory.create(session_key=session2.session_key)
    SessionProfileFactory.create()  # has no matching session record

    assert Session.objects.count() == 2
    assert SessionProfile.objects.count() == 3

    store = SessionProfileStore()
    store.clear_expired()

    assert Session.objects.count() == 2
    assert SessionProfile.objects.count() == 1
