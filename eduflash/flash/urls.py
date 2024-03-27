#!/usr/bin/env python3
'''this module contains urls/endpoints for the flash app'''
from django.urls import path
from . import views

#app_name = 'flash'

urlpatterns = [
    #path to the home page
    path('', views.home, name='home'),

    path('about', views.about, name='about'),

    #path to sign up
    path('sign_up', views.sign_up, name='sign_up'),

    #path to log in
    path('log_in', views.log_in, name='log_in'),

    path('log_out', views.log_out, name='log_out'),

    #path to welcome a user
    path('profile/<int:pk>', views.profile, name='profile'),

    # path('register', views.register, name='register'),
    # path('resource', views.resource, name='resource'),

    # #register user
    # path('register', views.register, name='register'),
    
    # #retrieve all resources of a user
    #path('profile/<int:fk>/resources', views.resources, name='resources'),
    path('resources', views.resources, name='resources'),
    
    # #retrive or delete a resource by id
    # path('resources/<int:resource_id>', views.resource, name='resource'),
    
    # #create resource object for specified user
    # path('users/<int:user_id>/resource', views.create_resource, name='resource'),

    #create a resource
    path('upload_resource', views.upload_resource, name='upload_resource'),

    #get a particular resource by id 
    path('get_resource/<int:pk>', views.get_resource, name='get_resource'),

    #update a resource
    path('update_resource/<int:pk>', views.update_resource, name='update_resource'),

    #delete a resource
    path('delete_resource/<int:pk>', views.delete_resource, name='delete_resource'),

    #create and view flashcards
    path('get_resource/<int:fk>/create_flashcards', views.create_flashcards, name='create_flashcards'),
    
    #view flashcards
    path('get_resource/<int:fk>/view_flashcards', views.view_flashcards, name='view_flashcards'),

    #get  a flashcard

    #path('flashcard/<int:pk>', views.get_flashcard)

    #update a flashcard
    #path('flashcard/<int:pk>', views.update_flashcards)

    #delete a flashcard
    #path('flashcard/<int:pk>', views.delete_flashcards)

]