from urlparse import urlparse
#from helpers import printDict, dumpObj
#from StringIO import StringIO
#from pprint import pprint
import requests
from bs4 import BeautifulSoup
from lxml import etree
from bids.models import *

"""
source = BidSource.objects.get(slug='barrington')
parser = etree.HTMLParser()	
html = requests.get(source.url).text
tree = etree.parse(StringIO(html), parser)
table = tree.xpath('//table[@width="98%"]')[0]

def get_url(tr):
	return tr.xpath('td')[2][0][0].get('href')

def get_date(tr):
	return tr.xpath('td')[1][0].text

def get_title(tr):
	return tr.xpath('td')[0][0].text[:1000]

u = urlparse(source.url)
base_url = "%s://%s" % (u.scheme, u.netloc)

for tr in table.xpath('tr')[1:]:
	title = get_title(tr)
	date = get_date(tr)
	url = base_url +  get_url(tr)
	bid = Bid.objects.filter(source=source,orig_id=title)
	if len(bid) == 0:
		Bid(source=source,orig_id=title,title=title,url=url).save()
	#print "title %s" % url

"""