from django.conf import settings
from django.db import models


class SessionProfile(models.Model):
    """
    We need to be able to get the username of the current logged-in
    user from PHP.  Our starting point is the sessionid, which
    is send in every request as a cookie.  We cannot go from this to
    the username in PHP, because the session data (for example,
    _auth_user_id) is stored in a pickled/json serialized dictionary,
    and I don't even want to think about unpickling Python dictionaries
    from PHP.
    So, we use our own authentication middleware to store a separate
    model object which has the same kind of association with the
    session as the UserProfile does with the user.  Doing this means
    that we're maintaining a DB table from which PHP can read the
    user ID, by going via the Users table.
    """

    session_key = models.CharField(max_length=40, primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE
    )
