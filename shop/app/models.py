from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

# Create your models here.
class Fruits(models.Model):
    name=models.CharField(max_length=20)
    about=models.TextField(max_length=500)
    slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)


class Contact(models.Model):
    name=models.CharField(max_length=50)
    number=models.IntegerField()
    email=models.EmailField(max_length=254)
    message=models.CharField(max_length=250)
class Oders(models.Model):
    User

