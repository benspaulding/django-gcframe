from functools import wraps

from django.utils.decorators import available_attrs
from django.utils.decorators import decorator_from_middleware_with_args

from gcframe.middleware import GoogleChromeFrameIEMiddleware
from gcframe.settings import IE_COMPATIBILITY_MODE, IE_ACTIVATION_METHOD


def gcframe(compat_mode=IE_COMPATIBILITY_MODE, act_method=IE_ACTIVATION_METHOD):
    """
    Decorator that adds ``X-UA-Compatible`` header to a view function.

    E.g.::

        @gcframe()
        def some_view(request):
            ...

    Optionally accepts ``compat_mode`` and ``act_method`` arguments. See
    the documentation for how these modify behavior.

    If GoogleChromeFrameIEMiddleware is installed, the arguments given
    to this decorator will take precedence.

    """

    return decorator_from_middleware_with_args(GoogleChromeFrameIEMiddleware)(compat_mode=compat_mode, act_method=act_method)


def gcframe_exempt(view_func):
    """
    Decorator that sets a ``gcframe_exempt`` response variable in a view function.

    This instructs ``GoogleChromeFrameIEMiddleware`` to **not** set the
    ``X-UA-Compatible`` HTTP header. E.g.::

        @gcframe_exempt
        def some_view(request):
            ...

    """

    # This code modeled after django.views.decorators.clickjacking.xframe_options_exempt
    def wrapped_view(*args, **kwargs):
        response = view_func(*args, **kwargs)
        response.gcframe_exempt = True
        return response

    return wraps(view_func, assigned=available_attrs(view_func))(wrapped_view)
