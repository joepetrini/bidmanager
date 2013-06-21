from datetime import datetime
from django.db import models
from django.contrib import admin
from django.conf import settings
from django.forms import TextInput, Textarea
from django.utils.timezone import utc
from django.utils.translation import ugettext as _
from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.models import TimeStampedModel
from picklefield.fields import PickledObjectField


class State(TimeStampedModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'state'        


class FrontendSite(TimeStampedModel):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=50)
    state = models.ForeignKey('State')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'frontend'


class County(TimeStampedModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    state = models.ForeignKey('State')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'county'


    def get_absolute_url(self):
        return "/county/%s" % self.slug

    @staticmethod
    def choices():
        #return County.objects.all()
        return [(c.name, c.name) for c in County.objects.all()]


class BidCategory(TimeStampedModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'category'        

    @staticmethod
    def choices():
        #return BidCategory.objects.all()
        return [(c.slug, c.name) for c in BidCategory.objects.all()]        


class BidSource(TimeStampedModel):

    STATUS = Choices(
        ('new', _('New')),
        ('ok', _('Good')),
        ('review', _('Needs review')),        
        ('error', _('In Error')),
    )

    CRAWL_TYPE = Choices(
        ('notify', _('Notify')),
        ('import', _('Auto Import'))
    )

    LEVEL = Choices(
        ('county', _('County')),
        ('state', _('State')),
        ('federal', _('Federal')),
        ('muncipal', _('Municpal')),
    )

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    url = models.CharField(max_length=1000)
    level = models.CharField(choices=LEVEL, max_length=20, default=LEVEL.county)    
    last_crawled = models.DateTimeField(null=True, blank=True)
    crawl_message = models.CharField(max_length=1000, null=True, blank=True)
    crawl_status = StatusField()
    # Type: Notify - email if content changed, Import - crawl+import job set up for this source
    crawl_type = models.CharField(choices=CRAWL_TYPE, default=CRAWL_TYPE.notify, max_length=20)
    # CSS selector target used to tell if content has changed, leave blank for full page body
    crawl_target = models.CharField(max_length=1000, null=True, blank=True)
    crawl_hash = models.CharField(max_length=1000, null=True, blank=True)
    enabled = models.BooleanField(default=True)
    # Default contact info for bids on this site
    contact_name = models.CharField(max_length=1000, null=True, blank=True)
    contact_phone = models.CharField(max_length=1000, null=True, blank=True)
    county = models.ForeignKey('County', null=True, blank=True)
    crawl_code = models.TextField(null=True, blank=True)

    objects = models.Manager()

    class Meta:
        db_table = 'source'    

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/location/%s/%s-%s-%s" % (self.id, self.county.state.slug, self.county.slug, self.slug)

    def done_crawl(self, success, message, hash):
        now = datetime.utcnow().replace(tzinfo=utc)
        self.last_crawled = now
        self.content_hash = hash
        self.save()


class BidSourceAdmin(admin.ModelAdmin):
    exclude = ('last_crawled','crawl_hash','crawl_message','crawl_status',)


class BidManager(models.Manager):
    def published(self):
        if settings.DEBUG:
            return self.get_query_set()
        else:
            return self.get_query_set().filter(status=Bid.STATUS.published)

class Bid(TimeStampedModel):

    STATUS = Choices(
        ('new', _('New')),
        ('published', _('Published')),
        ('closed', _('Closed')),
        ('ignore', _('Ignore')),        
    )

    orig_id = models.CharField(max_length=1000, null=True, blank=True, 
                                help_text="Unique ID from src sys",)
    status = StatusField(default=STATUS.new)
    source = models.ForeignKey('BidSource')
    category = models.ForeignKey('BidCategory', blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True)
    description = models.TextField(blank=True, help_text=_("Use markdown syntax"))
    contact_name = models.CharField(max_length=1000, blank=True)
    contact_phone = models.CharField(max_length=1000, blank=True)
    open_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    content_hash = models.CharField(max_length=1000, blank=True)
    extra_info = PickledObjectField()
    view_count = models.IntegerField(default=0)
    url = models.CharField(max_length=1000)

    
    objects = BidManager()#models.Manager()

    class Meta:
        db_table = 'bid'

    def __unicode__(self):
        return "%s - %s - %s" % (self.source, self.title[:60], self.status)

    def get_absolute_url(self):
        return "/%s/bid/%s" % (self.source.county.slug, self.id)


class BidAdmin(admin.ModelAdmin):
    exclude = ('orig_id', 'content_hash',)
    readonly_fields = ('view_count', 'url', 'source', )
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'150'})},
        models.TextField: {'widget': Textarea(attrs={'rows':25, 'cols':120})},
    }



"""

class Attachment(TimeStampedModel):
    TYPE = Choices(
        ('spec', _('Spec')),
        ('results', _('Results')),
    )

    bid = models.ForeignKey('Bid')
    url = models.CharField(max_length=1000)
    kind = models.CharField(choices=TYPE, max_length=20)
"""

admin.site.register(State)
admin.site.register(County)
admin.site.register(BidCategory)
admin.site.register(BidSource, BidSourceAdmin)
admin.site.register(Bid, BidAdmin)
