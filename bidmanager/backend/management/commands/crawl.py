from django.core.management.base import BaseCommand, CommandError
from bids.models import Bid, BidSource

class Command(BaseCommand):
    args = ''
    help = 'Closes the specified poll for voting'

    def p(self,m):
        self.stdout.write(m)

    def handle(self, *args, **options):
        for b in Bid.objects.all():
            self.p("%s" % b)