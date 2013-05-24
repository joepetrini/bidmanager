#import datetime
from haystack import indexes
from .models import Bid, BidSource, BidCategory, County


class BidIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    description = indexes.CharField(model_attr='description')    
    category = indexes.CharField(indexed=True, model_attr='category')
    source = indexes.CharField(model_attr='source')
    county = indexes.CharField(model_attr='source__county')
    level = indexes.CharField(model_attr='source__level')    
    date = indexes.DateTimeField(model_attr='open_date')

    def get_model(self):
        return Bid

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
