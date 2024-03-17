from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .forms import ResourceForm
'''this module contains views for the eduflash aoi endpoints'''
# Create your views here.
# get user flashcards 


def home(request):
    '''view for the home page'''
    return  HttpResponse('hello world')


def register(request):
    '''view for the register endpoint get and post
    if method is post create a new user with the info
    if method is get return the register page'''
    return render(request, 'flash/register.html')


def login(request):
    '''view for the login endpoint get and post
    if method is post call a method user.authenticate
    if true return the user dashboard
    if method is get return login page'''


def resources(request, fk):
    '''get resources based on user_id
    return all resources that belong to a user'''


def resource(request):
    '''get post delete
    if method is get retrive a resource based on id
    if method id post, create a resource object and save it to databaase
    then render a page that gives the client a flashcard creation option
    if method is delete delete the resource specified by user from database,
    also delete flashcards created from resource, inform user of this action'''
    form = ResourceForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form,
    }
    return render(request, 'flash/re_form.html', context)


def flashcards(request, fk):
    '''if method is get retrieves all flashcard created from a resource specified by fk
    the fk being the resource id
    if method is post create flashcards from the resource specified in by fk
    save it to database
    render a page that gives the users options to view the flashcards
     '''


def flashcard(request, pk):
    '''get put delete
    if method is get retrive a particular flashcard
    if method is put update flashcard infomation
    if method is delete delete a flashcard'''

