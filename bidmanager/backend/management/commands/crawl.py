from pprint import pprint
import urlparse
import importlib
from StringIO import StringIO
import requests
from bs4 import BeautifulSoup
from lxml import etree
from django.core.management.base import BaseCommand, CommandError
from bids.models import Bid, BidSource

class Command(BaseCommand):
    args = ''
    help = 'Closes the specified poll for voting'

    def p(self,m):
        self.stdout.write("%s" % m)

    def handle(self, *args, **options):
        parser = etree.HTMLParser()	    	
        for source in BidSource.objects.all():
            #self.p("%s" % source)
            if source.crawl_code <> "":
                self.p(source)
                r1 = urlparse.urlsplit(source.url)
                base_url = r1.scheme + '://' + r1.netloc
                html = requests.get(source.url).text
                tree   = etree.parse(StringIO(html), parser)
                soup = BeautifulSoup(html)
                with open('tmp.py','w') as f:
                    f.write
                    f.write(source.crawl_code)
                mymod = importlib.import_module('tmp')
                #res = mymod.a(tree)
                #self.p("Result: %s" % res)

                for tr in soup.find_all('table')[3].find_all('tr')[1:]:
                    #self.p(tr)
                    tds = tr.find_all('td')
                    title = tds[0].contents[0].string
                    opendate = tds[1].contents[0].string
                    link = base_url + tds[2].find_all('a')[0].get('href')
                    self.p(link)
            """
            if source.crawl_code is not None:
            #with open('tmp.py','w') as f:
            #    f.write
            #    f.write(source.crawl_code)
            try:
                #from tmp import crawlsite
                bids = []
                #html = requests.get(source.url).text
                #tree   = etree.parse(StringIO(html), parser)
                #result = crawlsite(tree)
                #return result
            except:
                self.p("error")
            """