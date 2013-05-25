from bs4 import BeautifulSoup
from lxml import etree

from bids.models import *

sources = BidSource.objects.all()
for s in sources:
	if s.crawl_code is not None:
		with open('tmp.py','w') as f:
			f.write(s.crawl_code)
		from tmp import a
		a()