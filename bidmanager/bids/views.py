import logging
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.views.generic import FormView
from haystack.query import SearchQuerySet
from haystack.inputs import AutoQuery, Exact, Clean
from django.http import HttpResponse
from django.conf import settings
from .forms import SearchForm, ContactForm
from .models import *
from profiles.models import BidsUser

#from django.contrib.auth import get_user_model


def about(request):
    """About Us page"""
    user = request.user if request.user.is_authenticated() else None
    #sources = BidSource.objects.filter(county__state__id=request.state_filter).order_by('county')
    counties = County.objects.select_related().filter(state__id=request.state_filter).order_by('name')
    return render(request, 'bids/about.html', {'counties': counties, 'u': user})


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "bids/contact_form.html"
    success_url = '/email-sent/'

    def form_valid(self, form):
        users = BidsUser.objects.filter(is_admin=True).values('email')
        mail_to = [u['email'] for u in users]
        message = "{name} / {email} said: ".format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'))
        message += "\n\n{0}".format(form.cleaned_data.get('message'))
        send_mail(
            subject="JerseyBids contact - %s " % form.cleaned_data.get('subject').strip(),
            message=message,
            from_email=settings.EMAIL_FROM,
            recipient_list=mail_to,
        )
        return super(ContactFormView, self).form_valid(form)

def email_sent(request):
    user = request.user if request.user.is_authenticated() else None
    return render(request, 'bids/email_sent.html', {'u': user})


def county(request, county_slug):
    """County page"""
    user = request.user if request.user.is_authenticated() else None    
    county = get_object_or_404(County, slug=county_slug)
    bids = Bid.objects.published().filter(source__county=county)
    print "LSDLNF : %s" % len(bids)
    return render(request, 'bids/county.html', {'u': user, 'county':county, 'bids':bids})

def location(request, location):
    """Location page"""
    #ser = request.user if request.user.is_authenticated() else None
    location = get_object_or_404(BidSource, pk=location)
    bids = Bid.objects.published().filter(source=location)
    return render(request, 'bids/location.html', {'location':location, 'bids': bids})

def home(request):
    """Home page"""
    user = request.user if request.user.is_authenticated() else None
    return render(request, 'bids/home.html', {'u': user})


def howto(request):
    """HowTo page"""
    user = request.user if request.user.is_authenticated() else None
    return render(request, 'bids/howto.html', {'u': user})


def bid_detail(request, bid_id):
    prev_url = request.session.get('prev_url')
    bid = get_object_or_404(Bid, pk=bid_id)
    return render(request, 'bids/bid_detail.html', {'bid': bid, 'prev_url': prev_url})


def search(request):
    request.session['prev_url'] = request.build_absolute_uri()
    q = request.GET.get('q')
    levels = request.GET.get('levels')
    counties = request.GET.get('counties')
    categories = request.GET.get('categories')

    # Text query
    if q is None:
        results = SearchQuerySet().all()
    else:
        results = SearchQuerySet().filter(content=AutoQuery(q))

    # Add filters
    results = results.filter(state=request.state_filter)
    if levels:
        levels = levels.split('-')
        results = results.filter(level__in=levels)
    if categories:
        categories = categories.split('-')
        results = results.filter(category__in=categories)
    if counties:
        counties = counties.split('-')
        results = results.filter(county__in=counties)

    rtitle = "Showing %s results" % len(results)
    levels = ['state', 'county', 'municipal']
    return render(request, 'bids/search.html',
        {'result_title': rtitle, 'results': results, 'cats': BidCategory.choices(),
         'counties': County.choices(), 'levels': levels })


def search_status(request):
    all = SearchQuerySet().all()
    out = ""
    for a in all:
        s = str(a.get_stored_fields())
        out += "%s" % s.replace(",", "<br>")
        #for f in a.get_stored_fields():
        #    out += "%s %s<br>" % (f, f.value)
        out += "<br><br>"
    return HttpResponse("Total items: %s<br>" % len(all) + out)
