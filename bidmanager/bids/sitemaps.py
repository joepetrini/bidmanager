from django.contrib.sitemaps import Sitemap
from .models import Bid


class BidSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Bid.objects.published().all()

    def lastmod(self, obj):
        return obj.modified