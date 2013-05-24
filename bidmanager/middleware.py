from django.utils import timezone
from django.conf import settings
from bids.models import FrontendSite

class FrontendMiddleware(object):
    def process_request(self, request):
        request_url = request.build_absolute_uri(request.get_full_path())
        host = request.META.get('HTTP_HOST').replace("www.","")
        if settings.DEBUG:
            request.state_filter = FrontendSite.objects.all()[0].state.id  
        else:
            request.state_filter = FrontendSite.objects.get(url=host).state.id


class TimezoneMiddleware(object):
    def process_request(self, request):
        tz = request.session.get('django_timezone')
        if tz:
            timezone.activate(tz)
        else:
            timezone.activate("US/Eastern")
