from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):

    # custom Model Manager

    class CelebrityObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(category='celebrity')

    class GadgetsObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(category='gadgets')
    
    class DestinationsObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(category='destinations')

    options =(
        ('celebrity','Celebrity'),
        ('gadgets','Gadgets'),
        ('destinations','Destinations'),
    )
    postedby = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    author = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=False)
    category= models.CharField(max_length=15, choices=options, default='celibrity')
    heading = models.CharField(max_length=200)
    title1 = models.CharField(max_length=200, blank=False)
    title1_Description = models.TextField(blank=False)
    title2 = models.CharField(max_length=200, blank=False)
    title2_Description = models.TextField(blank=False)
    title3 = models.CharField(max_length=200, blank=False)
    title3_Description = models.TextField(blank=False)
    title4 = models.CharField(max_length=200, blank=True)
    title4_Description = models.TextField(blank=True)
    title5 = models.CharField(max_length=200, blank=True)
    title5_Description = models.TextField(blank=True)
    read = models.IntegerField(default=0)
    img1 =  models.ImageField(upload_to='Images')
    img2 =  models.ImageField(upload_to='Images')
    img3 =  models.ImageField(upload_to='Images')
    QuickFact1 = models.CharField(max_length=30, blank=False)
    QuickFact1Ans = models.CharField(max_length=50, blank=False)
    QuickFact2 = models.CharField(max_length=30, blank=False)
    QuickFact2Ans = models.CharField(max_length=50, blank=False)
    QuickFact3 = models.CharField(max_length=30, blank=False)
    QuickFact3Ans = models.CharField(max_length=50, blank=False)
    objects = models.Manager()# defualt Manager
    celebrityObjects = CelebrityObject() #Custom Manager
    gadgetsObjects = GadgetsObject()# custom Manager
    destinationsObject = DestinationsObject()# custom Manager
    
    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.heading

class Gallery(models.Model):
    title = models.CharField(max_length=100, blank=True, default='Gallery')
    img = models.ImageField(upload_to='Gallery')

    def __str__(self):
        return self.title