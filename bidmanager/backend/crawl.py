#from StringIO import StringIO
#import requests
#from bs4 import BeautifulSoup
#from lxml import etree
#from models import *
import sys, os
from pprint import pprint

from django.core.management import setup_environ
from django.conf import settings

# If you find a solution that does not need the two paths, please comment!
#sys.path.append('/Users/joepetrini/Projects/bidmanager/bidmanager')
#sys.path.append(os.path.abspath('../..'))
sys.path.append(os.path.abspath('..'))

#os.environ['DJANGO_SETTINGS_MODULE'] = '$project_name$.settings'
from django.conf import settings

from bids.models import *

#pprint(sys.path)
#setup_environ(settings)
#print os.path.abspath('..')
#print os.path.abspath('../..')
a = Bid.objects.all()
print settings.DATABASES

"""
def crawl(source):
	parser = etree.HTMLParser()	
	if source.crawl_code is not None:
		with open('tmp.py','w') as f:
			f.write
			f.write(source.crawl_code)
		try:
			from tmp import crawlsite
			bids = []
			html = requests.get(source.url).text
			tree   = etree.parse(StringIO(html), parser)
			result = crawlsite(tree)
			return result
		except Exception,e:
			print "Error! %s" % e
			return {'error':e}

		#bids = a(bids,tree)
		##for b in bids:
		#	print b
	# Page lvl crawled sites
	"""