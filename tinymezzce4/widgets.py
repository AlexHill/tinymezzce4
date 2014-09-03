from django import forms
from mezzanine.conf import settings


_tinymce_js = ()
if settings.GRAPPELLI_INSTALLED:
    _tinymce_js = ("//tinymce.cachefly.net/4.1/tinymce.min.js",
                   settings.TINYMCE_SETUP_JS)


class TinyMceWidget(forms.Textarea):
    """
    Setup the JS files and targetting CSS class for a textarea to
    use TinyMCE.
    """

    class Media:
        js = _tinymce_js
        css = {'all': ("tinymezzce4/css/tinymce.css",)}

    def __init__(self, *args, **kwargs):
        super(TinyMceWidget, self).__init__(*args, **kwargs)
        self.attrs["class"] = "mceEditor"
