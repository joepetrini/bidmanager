import logging
from django.shortcuts import render
from haystack.query import SearchQuerySet
from django.http import HttpResponse

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
    qall = SearchQuerySet().exclude(content="hellO00")
    logging.debug("len qa %s" % len(qall))
    return HttpResponse(len(qall))