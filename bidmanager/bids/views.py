import logging
from django.shortcuts import render
from haystack.query import SearchQuerySet
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
    return render(request, 'bids/home.html', {'u': user})


def home(request):
    """Home page"""
    user = request.user if request.user.is_authenticated() else None
    return render(request, 'bids/home.html', {'u': user})


def howto(request):
    """HowTo page"""
    user = request.user if request.user.is_authenticated() else None
    return render(request, 'bids/home.html', {'u': user})


def search(request):
    results = SearchQuerySet().all()
    logging.debug("len qa %s" % len(results))
    #form = SearchForm()
    return render(request, 'bids/search.html', {'latest': True, 'results': results, 'cats': BidCategory.choices(), 'counties': County.choices() })