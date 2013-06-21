#from django import forms
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Submit
import floppyforms as forms
from .models import BidCategory, County


class SearchForm(forms.Form):
    counties = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=County.choices())
    categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=BidCategory.choices())


class ContactForm(forms.Form):

    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        #self.helper = FormHelper()
        #self.helper.add_input(Submit('submit', 'Submit'))
        super(ContactForm, self).__init__(*args, **kwargs)