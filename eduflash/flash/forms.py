from django.forms import models
from .models import Resource, Flashcard, User

class ResourceForm(models.ModelForm):
    '''this class represents a form foe getting
    information about a resource
    to be uploaded
    '''
    class Meta:
        model = Resource
        fields = ['name', 'filepath']

class UserForm(models.ModelForm):
    '''this class represents a form foe getting
    information about user
    to be uploaded
    '''
    class Meta:
        model = User
        fields = '__all__'