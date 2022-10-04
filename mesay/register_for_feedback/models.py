from distutils.command.upload import upload
from tokenize import String
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Registration(models.Model):
    Fname = models.CharField(max_length=100)
    Lname = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    PhoneNo = models.IntegerField()
    Feedback = models.TextField()
    Img = models.ImageField(upload_to='pics') 