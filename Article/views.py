from django.shortcuts import render, HttpResponse
from .models import Gallery, Article
from django.views.generic.base import TemplateView
from django_filters import filters
from django.contrib import messages
import datetime

# Create your views here.

def index(request):
    article = Article.objects.all()
    week = datetime.date.today()-datetime.timedelta(days=7)
    articleObj = Article.objects.filter(date__gte = week).order_by('-read')[:3]
    popularObj = Article.objects.order_by('-read')[:4]
    params = {'article': article, 'articleObj': articleObj, 'popularObj':popularObj}
    return render(request, 'index.html', params)

def search(request):
    query = request.GET['query']
    if len(query)>78:
        search = Article.objects.none()

    else:
        search = Article.objects.filter(heading__icontains=query)
    params = {'search': search, 'query':query}
    return render(request, 'search.html', params)

def article(request, myid):
    articleObj = Article.objects.filter(id = myid)
    articleObj = Article.objects.get(id = myid)
    articleObj.read = articleObj.read + 1
    articleObj.save()
    params = {'articleObj':articleObj}
    return render(request, 'article.html',params)

def celebrity(request):
    celebrityObj = Article.celebrityObjects.all()
    params = {'celebrityObj':celebrityObj}
    return render(request, 'celebrity.html', params)

def gadgets(request):
    gadgetsObj = Article.gadgetsObjects.all()
    params = {'gadgetsObj':gadgetsObj}
    return render(request, 'technology.html', params)

def destination(request):
    destinationObj = Article.destinationsObject.all()
    params = {'destinationObj':destinationObj}
    return render(request, 'destination.html', params)

def gallery(request):
    galleryObj = Gallery.objects.all()
    params = {'galleryObj':galleryObj}
    return render(request, 'gallery.html', params)


