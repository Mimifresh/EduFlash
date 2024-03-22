#!/usr/bin/env python3
'''this module contains urls/endpoints for the flash app'''
from django.urls import path, include
from . import views
from django.contrib import admin

app_name = "flash"

urlpatterns = [
    #path to the home page
    path('', views.home, name='home'),
	path('resource/<fk>/create_flashcards', views.create_flashcards, name='create_flashcards'),
	
	path('login', views.login, name='login'),
	  
    path('about', views.about, name='about'),
	
	path('upload_resource', views.upload_resource, name='upload_resource'),
	path('resource/<id>', views.get_resource, name='get_resource'),
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
    

    #get a particular resource by id 
    

    #create and view flashcards
    

	#path('accounts/', include('django.contrib.auth.urls')),
    # # if get retrive all flashcards made from a resource
    # # if post create flashcards from resource
    # path('resources/<int:resource_id>/flashcards', views.flashcards, name='flashcards'),

    # #retrive, delete, update a flashcard
    # path('flashcards/<int:flashcard_id>', views.flashcard, name='flashcard')
]