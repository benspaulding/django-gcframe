"""
Settings that define behavior of the middleware and decorators.

The settings here can be overridden by setting the corresponding
attribute in your settings.py

See the documentation for further details.

"""

try:
    from django.conf import settings
    # Because settings are magical LazySettings objects, it can be
    # imported even if the DJANGO_SETTINGS_MODULE environment variable
    # has not been set. But attempting to access an attribute will
    # cause the import, and throw an exception if the variable has not
    # been set, which is what we want.
    getattr(settings, 'DEBUG')
except ImportError:
    # This allows our defaults below to be used even when settings are
    # not importable.
    settings = {}


# By default the header will include the ``IE=Edge`` parameter/value pair.
# A value of ``None`` will exclude the pair.
# See possible values at http://msdn.microsoft.com/library/cc817574.aspx
IE_COMPATIBILITY_MODE = getattr(settings, 'GCF_IE_COMPATIBILITY_MODE', 'Edge')

# For possible values see Conditional Google Chrome Frame Activation in
# http://www.chromium.org/developers/how-tos/chrome-frame-getting-started
IE_ACTIVATION_METHOD = getattr(settings, 'GCF_IE_ACTIVATION_METHOD', '1')
