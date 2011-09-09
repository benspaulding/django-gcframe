from gcframe.settings import IE_COMPATIBILITY_MODE, IE_ACTIVATION_METHOD


class GoogleChromeFrameIEMiddleware(object):
    """
    Middleware that sets the X-UA-Compatible HTTP header in HTTP responses.

    Does not set the header if the response contains a `gcframe_exempt`
    value set to `True`.

    This header (conditionally) activates Google Chrome Frame in
    Internet Explorer, if it is installed. Otherwise, IE will use the
    highest compatibility mode that it has.

    The ``GCF_IE_COMPATIBILITY_MODE`` setting or a ``compat_mode``
    keyword argument can alter the behavior of compatibility mode. See
    the following URL for an example.

    See http://msdn.microsoft.com/library/cc817574.aspx for further
    details.

    The ``GCF_IE_ACTIVATION_METHOD`` setting or an ``act_method``
    keyword argument can alter the behavior of GCF activation. See
    the following URL for an example.

    See http://www.chromium.org/developers/how-tos/chrome-frame-getting-started

    """

    def __init__(self, compat_mode=IE_COMPATIBILITY_MODE, act_method=IE_ACTIVATION_METHOD):
        self.compat_mode = compat_mode
        self.act_method = act_method

    def process_response(self, request, response):

        # Don't set the header if the @gcframe_exempt decorator was used,
        # or if it has already been set. (The @gcframe decorator may
        # have been used to set a custom act_method value.)
        if not getattr(response, 'gcframe_exempt', False) \
        and not response.has_header('X-UA-Compatible'):

            # At this point we know they are activating GCF.
            content = 'chrome=%s' % self.act_method

            # Now prepend the compatibility mode parameter/value pair if
            # they want it. (They do by default.) Note that this pair
            # must be first in the content. See
            # http://www.chromium.org/developers/how-tos/chrome-frame-getting-started
            if not self.compat_mode == None:
                content = 'IE=%s,%s' % (self.compat_mode, content)

            response['X-UA-Compatible'] = content

        return response
