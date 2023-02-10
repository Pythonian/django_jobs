from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required


def employer_required(function):
    @login_required
    def wrapper(request, *args, **kwargs):
        user = request.user
        if not user.is_company:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    wrapper.__doc__ = function.__doc__
    wrapper.__name__ = function.__name__
    return wrapper


def anonymous_required(function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:home')
        return function(request, *args, **kwargs)
    return wrapper
