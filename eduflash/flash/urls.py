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

    path('log_out', views.log_out, name='log_out'),

    #path to welcome a user
    path('profile/<int:pk>', views.profile, name='profile'),

    
    #retrieve all resources of a user
    #path('profile/<int:fk>/resources', views.resources, name='resources'),
    path('resources', views.resources, name='resources'),
    
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

    #path('get_flashcard/<int:pk>', views.get_flashcard, name='get_flashcard'),

    #update a flashcard
    path('update_flashcard/<int:pk>', views.update_flashcard, name='update_flashcard'),

    #delete a flashcard
    path('delete_flashcard/<int:pk>', views.delete_flashcard, name='delete_flashcard'),

]