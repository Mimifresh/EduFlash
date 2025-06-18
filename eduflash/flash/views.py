from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from .forms import ResourceForm, UserForm, LogInForm, FlashcardForm
import re
from . import utils
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
'''this module contains views for the eduflash aoi endpoints'''
# Create your views here.
# get user flashcards 


def home(request):
    '''view for the home page'''
    if request.user.is_authenticated:
        return redirect(f'profile/{request.user.id}')
    return render(request, 'flash/home.html')
    #return  HttpResponse('hello world')

def about(request):
    '''view for the about page'''
    return render(request, 'flash/about.html')

def sign_up(request):
    '''register a user'''
    if request.user.is_authenticated:
        return redirect('profile')
    else:
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
    # if request.user.is_authenticated:
    #     return redirect('profile')
    # else:
    form = LogInForm(request, request.POST or None)
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        if form.is_valid():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(f'profile/{request.user.id}')
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('log_in')
    context = {'form': form, 'value': 'log in', 'title': 'log in'}
    return render(request, 'flash/upload.html', context)


def profile(request, pk):
    '''view that handles logic for when a user is logged in'''
    # user_id = int(pk)
    # resources = models.Resource.objects.filter(user=user_id)
    # context = {'resources': resources}
    return render(request, 'flash/profile.html')



def log_out(request):
    '''log a user out'''
    logout(request)
    return redirect('home')


def resources(request):
    '''get resources based on user_id
    return all resources that belong to a user'''
    resources = models.Resource.objects.filter(user=request.user.id)
    print(resources)
    context = {'resources': resources}
    return render(request, 'flash/resources.html', context)



def upload_resource(request):
    '''upload a resource for flashcard creation'''
    form = ResourceForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            if request.user.is_authenticated:
                resource = form.save(commit=False)
                resource.user = request.user
                resource.save()
                resources = models.Resource.objects.filter(user=request.user.id)
                context = {'resources': resources}                
            else:
                resource = form.save()
                context = {'resources': [resource]}
            return render(request, 'flash/resources.html', context )   
    context = {'form': form, 'value': 'upload', 'title': 'File uploader'}
    return render(request, 'flash/upload.html', context)


# def create_flashcards_temp(resource):
#     '''create flashcards from a resource uploades by anonymous'''
#     file_ = f'media/{resource.filepath.name}'
#     text = ''
#     with open(file_, 'r') as rse:
#         for line in rse:
#             text += line
#     text_array =  re.split("\.\s", text)
#     flashcards = []
#     for text in text_array:
#         flash_dict = utils.main(text)
#         for key, value in flash_dict.items():
#             flash = models.Flashcard(resource=resource, question=key, answer=value)
#             flashcards.append(flash)
#     return flashcards
#     # context = {'flashcards': flashcards, 'resource': [resource]}
#     # return render(request, 'flash/flashcards.html', context)



def delete_resource(request, pk):
    '''delete resource specified by pk'''
    resource =  models.Resource.objects.get(id=pk)
    if resource:
        resource.delete()
    return redirect('resources')


def update_resource(request, pk):
    '''update resource specified by pk'''
    resource =  models.Resource.objects.get(id=int(pk))
    form = ResourceForm(instance=resource)
    if request.method == "POST":
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('resources')
    context = {"form": form, 'value': 'update', 'title': 'Update file info'}
    return render(request, 'flash/upload.html', context)



def get_resource(request, pk):
    '''get a particular resource'''
    resource = models.Resource.objects.get(id= int(pk))
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
    print(text_array)
    for text in text_array:
        flash_dict = utils.main(text)
        for key, value in flash_dict.items():
            flash = models.Flashcard(resource=resource, question=key, answer=value)
            flash.save()
    flashcards = models.Flashcard.objects.filter(resource=fk)
    length = len(flashcards)
    indexed_flashcards = dict(enumerate(flashcards, start=1))
    context = {'flashcards': indexed_flashcards, 'resource': resource, 'length': length}
    return render(request, 'flash/flashcards.html', context)


def view_flashcards(request, fk):
    '''view available flashcards'''
    resource = models.Resource.objects.get(id = int(fk))
    flashcards = models.Flashcard.objects.filter(resource=fk)
    length = len(flashcards)
    indexed_flashcards = dict(enumerate(flashcards, start=1))
    context = {'flashcards': indexed_flashcards, 'resource': resource, 'length': length}
    return render(request, 'flash/flashcards.html', context)

    

# def register(request):
#     '''view for the register endpoint get and post
#     if method is post create a new user with the info
#     if method is get return the register page'''
#     form = UserForm()
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
    
#     context = {'form': form}
#     return render(request, 'flash/register.html', context)

def update_flashcard(request, pk):
    '''update flashcard specified by pk'''
    flashcard =  models.Flashcard.objects.get(id=pk)
    form = FlashcardForm(instance=flashcard)
    if request.method == "POST":
        form = FlashcardForm(request.POST, instance=flashcard)
        if form.is_valid():
            a = form.save()
            re_id = a.resource.id
            return redirect(f'{re_id}/view_flashcards')
    context = {"form": form, 'value': 'update', 'title': 'Update flashcard'}
    return render(request, 'flash/upload.html', context)

def delete_flashcard(request, pk):
    '''delete flashcard specified by pk'''
    flashcard =  models.Flashcard.objects.get(id=pk)
    re_id = flashcard.resource.id
    if flashcard:
        flashcard.delete()
    return redirect(f'{re_id}/view_flashcards')

