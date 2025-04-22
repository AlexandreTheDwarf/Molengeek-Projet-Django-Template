from django.db import models

# Create your models here.

class Blog(models.Model):
    image = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=254)
    url = models.CharField(max_length=64)

class Group(models.Model):
    name = models.CharField(max_length=64)

class Portfolio(models.Model):
    img = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=254)
    groups = models.ManyToManyField(Group)

class Contact(models.Model):
    title = models.CharField(max_length=64) 
    description = models.TextField()  
    company = models.CharField(max_length=64)  
    phone = models.CharField(max_length=20)  
    fax = models.CharField(max_length=20, blank=True, null=True) 
    email = models.EmailField()  