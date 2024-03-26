from django.contrib import admin
from .models import Resource, Flashcard, User

# Register your models here.
admin.site.register(Resource)
admin.site.register(Flashcard)
#admin.site.register(User)