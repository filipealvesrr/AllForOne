from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.http import HttpResponseForbidden


class DisableCSRFMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Check if the request is for the Django admin
        if reverse('admin:index') in request.path:
            setattr(request, '_dont_enforce_csrf_checks', True)
        else:
            setattr(request, '_dont_enforce_csrf_checks', False)
