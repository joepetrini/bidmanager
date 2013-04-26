from datetime import datetime
from django.db import models
from django.contrib import admin
from django.utils.timezone import utc
from django.utils.translation import ugettext as _
from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.models import TimeStampedModel
from picklefield.fields import PickledObjectField


class BidCategory(TimeStampedModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name


class BidSource(TimeStampedModel):

    STATUS = Choices(
        ('new', _('New')),
        ('ok', _('Good')),
        ('error', _('In Error')),
    )

    name = models.CharField(max_length=100)
    code = models.SlugField(max_length=100)
    url = models.CharField(max_length=1000)
    last_crawled = models.DateTimeField()
    crawl_message = models.CharField(max_length=1000)
    status = StatusField()
    content_hash = models.CharField(max_length=1000)
    enabled = models.BooleanField(default=True)
    contact_name = models.CharField(max_length=1000, blank=True)
    contact_phone = models.CharField(max_length=1000, blank=True)

    objects = models.Manager()

    def __unicode__(self):
        return self.name

    def done_crawl(self, success, message, hash):
        now = datetime.utcnow().replace(tzinfo=utc)
        self.last_crawled = now
        self.content_hash = hash
        self.save()


class Bid(TimeStampedModel):

    STATUS = Choices(
        ('new', _('New')),
        ('published', _('Published')),
        ('closed', _('Closed')),
    )

    orig_id = models.CharField(max_length=1000,
                               help_text="Unique ID from src sys")
    source = models.ForeignKey('BidSource')
    category = models.ForeignKey('BidCategory', blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True)
    description = models.TextField(blank=True)
    contact_name = models.CharField(max_length=1000, blank=True)
    contact_phone = models.CharField(max_length=1000, blank=True)
    open_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    content_hash = models.CharField(max_length=1000, blank=True)
    extra_info = PickledObjectField()
    view_count = models.IntegerField(default=0)
    url = models.CharField(max_length=1000)

    objects = models.Manager()

    def __unicode__(self):
        return "%s - %s" % (self.source, self.title[:60])

admin.site.register(BidCategory)
admin.site.register(BidSource)
admin.site.register(Bid)
