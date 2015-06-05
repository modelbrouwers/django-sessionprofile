========
Examples
========

phpBB3
======

Installing the authentication plugin
------------------------------------

It's fairly easy to authenticate from phpBB3 with Django, although some
minor modifications are needed in the phpBB3 source.

Two files should be included in the ``<phpBB3 root>/includes/auth`` folder.
Keeping these files in version control is possible, you can symlink to them.

The code snippets are fairly long and can be found in the
:ref:`phpbb3-code-snippets`.

.. note:: phpBB 3.1.x supports extensions now, which is radically different
   from the way that 3.0.x mods are installed. This code will not work on 3.1.x
   or higher versions.

Local phpBB3 install modifications
----------------------------------

A few modifications are required to keep the users from getting confused.

Templates
~~~~~~~~~
Templates in phpBB3 live in ``<phpBB3 root>/styles/<theme>/template``

* You'll want to modify ``login_body.html``. Logging in directly is
  usually not possible due to the CSRF protection.

  An example replace file could be:

  .. code-block:: html

     <!-- INCLUDE overall_header.html -->

     <div class="panel">
     <div class="inner"><span class="corners-top"><span></span></span>

     <div class="content">
       <h2><!-- IF LOGIN_EXPLAIN -->{LOGIN_EXPLAIN}<!-- ELSE -->{L_LOGIN}<!-- ENDIF --></h2>

       <p>
       Only registered users on our site can post in these forums.  If you have registered
       already, you can <a href="/login/">log in</a>; if not you can
       <a href="/register/">register</a> - it only takes a few minutes.

     </div>
     <span class="corners-bottom"><span></span></span></div>
     </div>

     </form>

     <!-- INCLUDE overall_footer.html -->

* ``overal_header.html`` has some checks and links to the
  login/register pages. You should modify this and set it to your own.

* **IMPORTANT** You'll need to edit ``adm/index.php`` and remove an the
  lines that make you login again to go to the admin panel.

  They look like this:

  .. code-block:: php
     :lineno-start: 30

     if (!isset($user->data['session_admin']) || !$user->data['session_admin'])
     {
        login_box('', $user->lang['LOGIN_ADMIN_CONFIRM'], $user->   lang['LOGIN_ADMIN_SUCCESS'], true, false);
     }

Enabling auth_django
--------------------
Make sure you have Django user who was the same username as an admin of the
phpBB forum, and log in as that user in Django and phpBB.

You can now go into the phpBB admin panel and enable the auth_django authentication module.
