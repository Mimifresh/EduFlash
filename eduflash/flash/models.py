from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid


# Create your models here.

class User(AbstractUser):
  """Custom User model with additional fields and password hashing"""
  username = models.CharField(max_length=200)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(auto_now=True)
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)


#class User(models.Model):
#     '''the user class
#     '''
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     username = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)

class Resource(models.Model):
    '''the resource class'''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    filepath = models.FileField(upload_to='files/', verbose_name='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Flashcard(models.Model):
    '''the flashcard class'''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    question = models.TextField()
    answer = models.TextField()
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

