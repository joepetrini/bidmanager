import logging
from django.shortcuts import render
from haystack.query import SearchQuerySet
from haystack.inputs import AutoQuery, Exact, Clean
from django.http import HttpResponse
from .forms import SearchForm
from .models import *

#from django.contrib.auth import get_user_model


def about(request):
    """About Us page"""
    user = request.user if request.user.is_authenticated() else None
    return render(request, 'bids/home.html', {'u': user})


def contact(request):
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
    levels = ['state','county','municipal']
    return render(request, 'bids/search.html', 
        {'result_title': rtitle, 'results': results, 'cats': BidCategory.choices(),
         'counties': County.choices(), 'levels': levels })

def search_status(request):
    all = SearchQuerySet().all()
    out = ""
    for a in all:
        s = str(a.get_stored_fields())
        out += "%s" % s.replace(",","<br>")
        #for f in a.get_stored_fields():
        #    out += "%s %s<br>" % (f, f.value)
        out += "<br><br>"
    return HttpResponse("Total items: %s<br>" % len(all) + out)