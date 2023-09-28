from django.conf import settings


class SetMimeTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path.startswith(settings.MEDIA_URL):
            response['Content-Type'] = 'application/octet-stream'
        return response
