from django.template import Context
from django.conf import settings


def bids_context(request):
    return {
            'debug': settings.DEBUG, 
        }