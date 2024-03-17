from django.db import models
import uuid

# Create your models here.


class User(models.Model):
    '''the user class
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

class Resource(models.Model):
    '''the resource class'''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    filepath = models.FileField(upload_to='files/', null=True, verbose_name='')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Flashcard(models.Model):
    '''the flashcard class'''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=4000)
    resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
