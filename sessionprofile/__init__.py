VERSION = (0, 2, 0)


def get_version():
    return '.'.join([str(bit) for bit in VERSION])


default_app_config = 'sessionprofile.apps.SessionProfileConfig'
