from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bids.models import *
#from crawl import crawl

@login_required
def dashboard(request):
    #sources = BidSource.objects.all()
    new_bids = Bid.objects.filter(status=Bid.STATUS.new).order_by('-created')
    return render(request, 'backend/dashboard.html', {'bids': new_bids})


def editcrawl(request, source_id):
    source = BidSource.objects.get(id=source_id)
    # If post save
    if request.POST:
        source.crawl_code = request.POST['code']
        source.save()
    # Run crawl
    #result = crawl(source)
    result = ""
    return render(request, 'backend/editcrawl.html', {'source': source, 'result': result})
