import importlib, pkgutil
import logging
from django.core.management.base import BaseCommand, CommandError
from bids.models import Bid, BidSource

class Command(BaseCommand):
    args = ''
    help = 'Closes the specified poll for voting'

    def p(self,m):
        self.stdout.write("%s" % m)

    def handle(self, *args, **options):
        if len(args) == 1:
            importlib.import_module("backend.crawlers.%s" % args[0])
        else:
            for p in pkgutil.walk_packages('backend.crawlers'):
                if 'backend.crawlers.' in str(p):
                    print "Crawling %s" % p[1]
                    importlib.import_module(str(p[1]))
