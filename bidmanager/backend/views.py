from django.shortcuts import render
from bids.models import *
#from crawl import crawl


def sources(request):
	sources = BidSource.objects.all()
	return render(request, 'backend/sources.html', {'sources': sources})


def editcrawl(request, source_id):
	source = BidSource.objects.get(id = source_id)
	# If post save
	if request.POST:
		source.crawl_code = request.POST['code']
		source.save()
	# Run crawl
	#result = crawl(source)
	result = ""
	return render(request, 'backend/editcrawl.html', {'source': source, 'result': result})	
