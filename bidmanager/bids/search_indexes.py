#import datetime
from haystack import indexes
from .models import Bid, BidSource, BidCategory, County


class BidIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    category = indexes.CharField(model_attr='category')
    source = indexes.CharField(model_attr='source')

    def get_model(self):
        return Bid

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class BidSourceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name =indexes.CharField(model_attr='name')

    def get_model(self):
        return BidSource

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class BidCategoryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name =indexes.CharField(model_attr='name')

    def get_model(self):
        return BidCategory

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class CountyIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name =indexes.CharField(model_attr='name')

    def get_model(self):
        return County

    def index_queryset(self, using=None):
        return self.get_model().objects.all()        