from django.utils import timezone
from django.conf import settings
from bids.models import FrontendSite

class FrontendMiddleware(object):
    def process_request(self, request):
        request_url = request.build_absolute_uri(request.get_full_path())
        host = request.META.get('HTTP_HOST').replace("www.","")
        if settings.DEBUG:
            request.site_name = FrontendSite.objects.all()[0]
            request.state_filter = request.site_name.state.id
        else:
            request.site_name = FrontendSite.objects.get(url=host)
            request.state_filter = request.site_filter.state.id


class TimezoneMiddleware(object):
    def process_request(self, request):
        tz = request.session.get('django_timezone')
        if tz:
            timezone.activate(tz)
        else:
            timezone.activate("US/Eastern")
