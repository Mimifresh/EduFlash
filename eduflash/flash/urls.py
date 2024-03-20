#!/usr/bin/env python3
'''this module contains urls/endpoints for the flash app'''
from django.urls import path
from . import views

urlpatterns = [
    #path to the home page
    path('', views.home, name='home'),
    # path('register', views.register, name='register'),
    # path('resource', views.resource, name='resource'),

    # #register user
    # path('register', views.register, name='register'),
    
    # #retrieve all resources of a user
    # path('users/<int:user_id>/resources', views.resources, name='resources'),
    
    # #retrive or delete a resource by id
    # path('resources/<int:resource_id>', views.resource, name='resource'),
    
    # #create resource object for specified user
    # path('users/<int:user_id>/resource', views.create_resource, name='resource'),

    #create a resource
    path('upload_resource', views.upload_resource, name='upload_resource'),

    #get a particular resource by id 
    path('resource/<id>', views.get_resource, name='get_resource'),

    #create and view flashcards
    path('resource/<fk>/create_flashcards', views.create_flashcards, name='create_flashcards'),

    # # if get retrive all flashcards made from a resource
    # # if post create flashcards from resource
    # path('resources/<int:resource_id>/flashcards', views.flashcards, name='flashcards'),

    # #retrive, delete, update a flashcard
    # path('flashcards/<int:flashcard_id>', views.flashcard, name='flashcard')
]