from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail
from bids.models import Bid, BidSource
from profiles.models import BidsUser

class Command(BaseCommand):
    args = ''
    help = 'Send notifications'

    def p(self,m):
        self.stdout.write("%s" % m)

    def handle(self, *args, **options):
        newbids = Bid.objects.filter(status=Bid.STATUS.new).count()
        if newbids > 0:
            users = BidsUser.objects.filter(is_admin=True).values('email')
            to = [u['email'] for u in users]
            msg = "%s new bids waiting.  " % newbids
            subj = "New bids to process - %s" % newbids
            send_mail(subj, msg, 'noreply@jerseybids.com', to, fail_silently=False)
