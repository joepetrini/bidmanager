from urlparse import urlparse
from helpers import printDict, dumpObj
from StringIO import StringIO
from pprint import pprint
import requests
from bs4 import BeautifulSoup
from lxml import etree
from bids.models import *

try:
	source = BidSource.objects.get(slug='little-silver')
except BidSource.DoesNotExist:
	source = BidSource(
						name="Little Silver", 
						slug="little-silver", 
						url="http://littlesilver.org/ls/Bid%20Notifications/",
						county=County.objects.get(id=1)
					   	).save()

parser = etree.HTMLParser()	
html = requests.get(source.url).text
tree = etree.parse(StringIO(html), parser)
bidlist = tree.xpath('//ul')[0]


def get_url(li):
	return li.xpath('a')[0].get('href')
	#return tr.xpath('td')[2][0][0].get('href')

def get_title(li):
	return li.xpath('a/nobr')[0].text[:1000].replace('(pdf)','')

u = urlparse(source.url)
base_url = "%s://%s" % (u.scheme, u.netloc)


for li in bidlist.xpath('li'):
	url = base_url + get_url(li)
	#print url
	title = get_title(li)
	bid = Bid.objects.filter(source=source,orig_id=title)
	if len(bid) == 0:
		Bid(source=source,orig_id=title,title=title,url=url).save()
	#print title
