from django import forms
from .models import BidCategory, County

class SearchForm(forms.Form):
	counties = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=County.choices())
	categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=BidCategory.choices())
