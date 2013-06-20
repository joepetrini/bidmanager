import logging
from django.shortcuts import render, get_object_or_404
from haystack.query import SearchQuerySet
from haystack.inputs import AutoQuery, Exact, Clean
from django.http import HttpResponse
from .forms import SearchForm
from .models import *

#from django.contrib.auth import get_user_model


def about(request):
    """About Us page"""
    user = request.user if request.user.is_authenticated() else None
    #sources = BidSource.objects.filter(county__state__id=request.state_filter).order_by('county')
    counties = County.objects.select_related().filter(state__id=request.state_filter).order_by('name')
    return render(request, 'bids/about.html', {'counties': counties, 'u': user})


def contact(request):
    """Contact page"""
    user = request.user if request.user.is_authenticated() else None
    return render(request, 'bids/contact.html', {'u': user})


def county(request, county_slug):
    """Contact page"""
    user = request.user if request.user.is_authenticated() else None
    return render(request, 'bids/contact.html', {'u': user})


def home(request):
    """Home page"""
    user = request.user if request.user.is_authenticated() else None
    return render(request, 'bids/home.html', {'u': user})


def howto(request):
    """HowTo page"""
    user = request.user if request.user.is_authenticated() else None
    return render(request, 'bids/howto.html', {'u': user})


def bid_detail(request, bid_id):
    bid = get_object_or_404(Bid, pk=bid_id)
    return render(request, 'bids/bid_detail.html', {'bid': bid})


def search(request):
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
