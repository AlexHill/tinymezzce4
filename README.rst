======================
TinyMCE4 for Mezzanine
======================

This app enables the latest TinyMCE4 for Mezzanine, including integration with Mezzanine's filebrowser_safe (just "filebrowser" from here on).

To use it, you need to make these three simple changes to your settings.py:

1. Add ``"tinymezzce4"`` to INSTALLED_APPS.
2. Add the line ``RICHTEXT_WIDGET_CLASS = 'tinymezzce4.widgets.TinyMceWidget'``
3. Add the line ``TINYMCE_SETUP_JS = '/static/tinymezzce4/js/tinymce_setup.js'``. To customise your TinyMCE4 setup, make your own modified copy of this file and change the ``TINYMCE_SETUP_JS`` to point to it.

Restart your app, and you're done!

Notes:

* TinyMezzCE4 doesn't actually ship with TinyMCE; it uses the CDN-hosted version.
* ``"tinymezzce4"`` must appear before ``"filebrowser_safe"`` in ``INSTALLED_APPS``, because it overrides some of filebrowser's templates and static files. In a normal Mezzanine installation, ``filebrowser_safe`` is added to ``INSTALLED_APPS`` at a later stage, so anywhere will be fine.

----------------------------------------------------
Warning: updates to filebrowser could break this app
----------------------------------------------------

To allow integration with filebrowser, TinyMezzCE4 overrides some of its templates. If the filebrowser templates are
updated, your app will still be using the templates provided with TinyMCE4. This is a problem, but I aim to get the
necessary modifications into Mezzanine's ``filebrowser_safe``, which would solve it permanently.