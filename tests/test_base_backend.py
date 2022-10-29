import pytest

from sessionprofile.backends.base import Base


class MockRequest:
    pass


class MockRequest2:
    session = "foo"


def test_base_methods():
    backend = Base()

    with pytest.raises(NotImplementedError):
        backend.save_session(object())

    with pytest.raises(NotImplementedError):
        backend.purge_for_user(object())

    with pytest.raises(NotImplementedError):
        backend.clear_expired()


def test_get_session_store():
    backend = Base()

    request1 = MockRequest()
    store1 = backend.get_session_store(request1)
    assert store1 is None

    request2 = MockRequest2()
    store2 = backend.get_session_store(request2)
    assert store2 == "foo"
