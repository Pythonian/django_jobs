from django.shortcuts import redirect


def anonymous_required(function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:home')
        return function(request, *args, **kwargs)
    return wrapper
