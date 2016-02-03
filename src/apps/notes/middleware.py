from django.core.urlresolvers import reverse

from models import LastRequest


class RequestStoreMiddleware(object):
    """Middleware to store http requests in database"""
    def process_request(self, request):
        last_request = LastRequest(
            url=request.META['PATH_INFO'],
            method=request.META['REQUEST_METHOD'],
            )
#        if  request.META['PATH_INFO'] != reverse('request-count'):
        last_request.save()
