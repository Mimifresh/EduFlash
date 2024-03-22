from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from .forms import ResourceForm, UserForm, LogInForm
import re
from . import utils
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
'''this module contains views for the eduflash aoi endpoints'''
# Create your views here.
# get user flashcards 


def home(request):
    '''view for the home page'''
    return render(request, 'flash/main.html')
    #return  HttpResponse('hello world')

def about(request):
    '''view for the about page'''
    return render(request, 'flash/about.html')

def sign_up(request):
    '''register a user'''
    form = UserForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            try:
                dict_ = {'username': request.POST['username'],
                'first_name': request.POST['first_name'],
                'last_name': request.POST['last_name'],
                'email': request.POST['email']
                }
                password = form.clean_password()
                user = models.User.objects.create_user(**dict_)
                user.set_password(password)
                user.save()
                return redirect('log_in')
            except Exception as e:
                messages.error(request, e)
                return redirect('sign_up')
        else:
            messages.error(request, 'invalid form parameters')
            return redirect('sign_up')
    context = {'form': form, 'value': 'sign up', 'title': 'Sign up'}
    return render(request, 'flash/upload.html', context)
            



def log_in(request):
    '''log a user in'''
    form = LogInForm(request, request.POST or None)
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        if form.is_valid():
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(user)
                context = {'user': user}
                return render(request, 'flash/dashboard.html', context)
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('log_in')
    context = {'form': form, 'value': 'log in', 'title': 'log in'}
    return render(request, 'flash/upload.html', context)

def log_out(request):
    '''log a user out'''
    logout(request)


def resources(request, fk):
    '''get resources based on user_id
    return all resources that belong to a user'''
    resources = models.Resource.objects.filter(user=request.user)
    context = {'rsources': resources}
    return render(request, 'flash/resources.html', context)



def upload_resource(request):
    '''upload a resource for flashcard creation'''
    form = ResourceForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            if request.user.is_authenticated:
                form.save()
                resources = models.Resource.objects.all()
                context = {'resources': resources}
            else:
                resource = form.save(commit=False)
                context = {'resource: resource'}
                return render(request, 'flash/resources.html', context )

        return render(request, 'flash/resources.html', context )
    context = {'form': form, 'value': 'upload', 'title': 'File uploader'}
    return render(request, 'flash/upload.html', context)


def delete_resource(request, pk):
    '''delete resource specified by pk'''
    resource =  models.Resource.object.get(id=int(pk))
    form = ResourceForm(instance = resource)


def update_resource(request, pk):
    '''update resource specified by pk'''
    resource =  models.Resource.object.get(id=int(pk))
    form = ResourceForm(instance=resource)
    if request.method == "POST":
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('flash/resources.html')
    context = {"form": form, 'value': 'update', 'title': 'Update file info'}
    return render(request, 'flash/upload.html', context)



def get_resource(request, pk):
    '''get a particular resource'''
    resource = models.Resource.object.get(id= int(pk))
    context = {'resource': resource}
    return redirect('create_flashcards')


def create_flashcards(request, fk):
    '''create flashcards from a resource'''
    resource = models.Resource.objects.get(id = int(fk))
    file_ = f'media/{resource.filepath.name}'
    text = ''
    with open(file_, 'r') as rse:
        for line in rse:
            text += line
    text_array =  re.split("\.\s", text)
    for text in text_array:
        flash_dict = utils.main(text)
        for key, value in flash_dict.items():
            flash = models.Flashcard(resource=resource, question=key, answer=value)
            flash.save()
    flashcards = models.Flashcard.objects.filter(resource=resource)
    context = {'flashcards': flashcards}
    return render(request, 'flash/flashcards.html', context)

    

def register(request):
    '''view for the register endpoint get and post
    if method is post create a new user with the info
    if method is get return the register page'''
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    context = {'form': form}
    return render(request, 'flash/register.html', context)


def login(request):
    '''view for the login endpoint get and post
    if method is post call a method user.authenticate
    if true return the user dashboard
    if method is get return login page'''





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

