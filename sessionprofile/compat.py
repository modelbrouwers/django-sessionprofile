from django import VERSION


def is_authenticated(user):
    if VERSION < (1, 10):
        return user.is_authenticated()
    return user.is_authenticated
