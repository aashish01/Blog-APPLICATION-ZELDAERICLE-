from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="indexPage"),
    path('celebrity',views.celebrity, name ='CelebrityPage'),
    path('search',views.search, name ='SearchPage'),
    path('article<int:myid>',views.article, name ='ArticlePage'),
    path('gadgets',views.gadgets, name ='TechnologyPage'),
    path('destination',views.destination, name ='TourDestination'),
    path('gallery',views.gallery, name ='GalleryPage'),
]