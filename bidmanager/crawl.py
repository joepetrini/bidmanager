from StringIO import StringIO
import requests
from bs4 import BeautifulSoup
from lxml import etree

from bids.models import *

parser = etree.HTMLParser()

def crawl(source):
	pass

sources = BidSource.objects.all()
for s in sources:
	# Custom coded bids
	if s.crawl_code is not None:
		with open('tmp.py','w') as f:
			f.write
			f.write(s.crawl_code)
		from tmp import a
		bids = []
		html = requests.get(s.url).text
		tree   = etree.parse(StringIO(html), parser)

		bids = a(bids,tree)
		for b in bids:
			print b
	# Page lvl crawled sites