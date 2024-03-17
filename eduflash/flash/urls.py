#!/usr/bin/env python3
'''this module contains urls/endpoints for the flash app'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('resource', views.resource, name='resource'),
]