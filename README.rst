======================
TinyMCE4 for Mezzanine
======================

This app enables the latest TinyMCE4 for Mezzanine, including integration with Mezzanine's filebrowser.

To use it, you need to make these three simple changes to your settings.py:

1. Add ``tinymezzce4`` to INSTALLED_APPS. ``tinymezzce4`` *must appear before filebrowser_safe*, because it overrides some of filebrowser's templates and static files - if you put it at the top, you'll be fine.
2. Add the line ``RICHTEXT_WIDGET_CLASS = 'tinymezzce4.widgets.TinyMceWidget'``
3. Add the line ``TINYMCE_SETUP_JS = '/static/js/tinymce_setup.js'``

Restart your app, and you're done!

Note: TinyMezzCE4 doesn't actually ship with TinyMCE, instead opting to use the CDN-hosted version.

