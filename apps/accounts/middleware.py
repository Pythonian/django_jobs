from apps.accounts.views.auth import update_last_seen


class UpdateLastSeenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        update_last_seen(request)
        return response
