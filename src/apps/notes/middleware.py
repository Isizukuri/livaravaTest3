from django.core.urlresolvers import reverse
from django.conf import settings

from models import LastRequest


class RequestStoreMiddleware(object):
    """Middleware to store http requests in database"""
    def process_request(self, request):
        path_info = request.META['PATH_INFO']
        exclude_list = [
            reverse('admin:jsi18n'),
            settings.MEDIA_URL,
            settings.STATIC_URL,
        ]
        save_trigger = (path_info in exclude_list) or \
            (request.is_ajax() and path_info == reverse('last_requests'))
        last_request = LastRequest(
            url=request.META['PATH_INFO'],
            method=request.META['REQUEST_METHOD'],
            )
        if not save_trigger:
            last_request.save()
