from django.forms import models
from .models import Resource

class ResourceForm(models.ModelForm):
    '''this class represents a form foe getting
    information about a resource
    to be uploaded
    '''
    class Meta:
        model = Resource
        fields = ['name', 'filepath']
