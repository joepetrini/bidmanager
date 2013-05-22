import datetime
from haystack import indexes
from .models import Bid

class BidIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(model_attr='title')

	def get_model(self):
		return Bid

	def index_queryset(self, using=None):
		return self.get_model().objects.all()
