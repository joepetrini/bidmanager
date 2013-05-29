from StringIO import StringIO
import requests
from bs4 import BeautifulSoup
from lxml import etree
from bids.models import *

source = BidSource.objects.get(slug='chatham')
parser = etree.HTMLParser()	
html = requests.get(source.url).text
tree   = etree.parse(StringIO(html), parser)
trs = tree.xpath('//table')[3]
for tr in trs.xpath('//tbody/tr'):
	print "row %s" % tr