import inspect
from urlparse import urlparse
from StringIO import StringIO
import requests
from bs4 import BeautifulSoup
from lxml import etree
from bids.models import *

class Crawler():
	doctypes = ['pdf','doc','docx']

	def __init__(self, county="", url=""):
		# Get the calling module
		self.slug = inspect.currentframe().f_back.f_locals['__name__'].split('.')[-1:][0]

		# Get/create the bidsource
		try:
			self.source = BidSource.objects.get(slug=self.slug)
		except BidSource.DoesNotExist:
			unslug = self.slug.replace("-"," ").capitalize()
			self.source = BidSource.objects.create(
						name=unslug, 
						slug=self.slug, 
						url=url,
						county=County.objects.get(slug=county)
					   	)

		# Set the base url, used for building out relative links
		u = urlparse(self.source.url)
		self.base_url = "%s://%s" % (u.scheme, u.netloc)

		# Set up the crawler objects
		html = requests.get(self.source.url).text
		self.soup = BeautifulSoup(html)
		parser = etree.HTMLParser()	
		self.tree = etree.parse(StringIO(html), parser)


	def AddItem(self, title, url, orig_id=None):
		# If no id provided, use the url
		if orig_id is None:
			orig_id = url
		bid = Bid.objects.filter(source=self.source,orig_id=orig_id)
		if len(bid) == 0:
				Bid(source=self.source, orig_id=orig_id, title=title, url=url).save()