#!/usr/bin/env python3
'''this module contains urls/endpoints for the flash app'''
from django.urls import path
from . import views

urlpatterns = [
    #path to the home page
    path('', views.home, name='home'),

    path('about', views.about, name='about'),

    #path to sign up
    path('sign_up', views.sign_up, name='sign_up'),

    #path to log in
     path('log_in', views.log_in, name='log_in'),

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

    #update a resource
    path('resource/<id>', views.get_resource, name='update_resource'),

    #delete a resource
    path('resource/<id>', views.get_resource, name='delete_resource'),

    #create and view flashcards
    path('resource/<fk>/create_flashcards', views.create_flashcards, name='create_flashcards'),

    #get  a flashcard
    #path('flashcard/<int:pk>', views.get_flashcard)

    #update a flashcard
    #path('flashcard/<int:pk>', views.update_flashcards)

    #delete a flashcard
    #path('flashcard/<int:pk>', views.delete_flashcards)

]