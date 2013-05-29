from StringIO import StringIO
import requests
from bs4 import BeautifulSoup
from lxml import etree
from models import *


def crawl(source):
	parser = etree.HTMLParser()	
	if source.crawl_code is not None:
		with open('tmp.py','w') as f:
			f.write
			f.write(source.crawl_code)
		try:
			from tmp import a
			bids = []
			html = requests.get(source.url).text
			tree   = etree.parse(StringIO(html), parser)
			result = a(tree)
		except:
			pass

		#bids = a(bids,tree)
		##for b in bids:
		#	print b
	# Page lvl crawled sites
	