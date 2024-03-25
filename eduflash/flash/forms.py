from django.forms import models, fields
from django.forms import ModelForm, TextInput, FileInput, EmailInput, PasswordInput, ValidationError
from .models import Resource, Flashcard, User
from django.contrib.auth.forms import AuthenticationForm

class ResourceForm(models.ModelForm):
    '''this class represents a form foe getting
    information about a resource
    to be uploaded
    '''
    class Meta:
        model = Resource
        fields = ['filename', 'filepath']
        widgets = {
            'filename': TextInput(attrs={
                'class': "value",
                }),
            'filepath': FileInput(attrs={
                'class': "value", 
                })
        }

class FlashcardForm(models.ModelForm):
    '''this class represents a form foe getting
    information about a flashcard
    to be updated
    '''
    class Meta:
        model = Flashcard
        fields = ['question', 'answer']
        # widgets = {
        #     'question': TextInput(attrs={
        #         'class': "value",
        #         }),
        #     'answer': FileInput(attrs={
        #         'class': "value", 
        #         })
        # }


class LogInForm(AuthenticationForm):
    '''log in form'''
    username = fields.CharField(label='username', 
        widget=TextInput(attrs={'class': 'value'})
    )
    password = fields.CharField(label='password', 
        widget=PasswordInput(attrs={'class': 'value'})
    )
    

class UserForm(models.ModelForm):
    '''this class represents a form for getting
    information about user
    to be uploaded
    '''
    password1 = fields.CharField(label='Password', widget=PasswordInput(attrs={'class': 'value'}))
    password2 = fields.CharField(label='Confirm Password', widget=PasswordInput(attrs={'class': 'value'}))
    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        #fields = '__all__'
        widgets = {
             'username': TextInput(attrs={
                'class': "value",
                }),
            'first_name': TextInput(attrs={
                'class': "value", 
                }),
            'last_name': TextInput(attrs={
                'class': "value",
                }),
            'email': EmailInput(attrs={
                'class': "value", 
                }),
             'password1': PasswordInput(attrs={
                'class': "value",
                }),
            'password2': PasswordInput(attrs={
                'class': "value",
                }),
            
        }

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and (password1 != password2):
            raise ValidationError('Passwords don\'t match.')
        return password2
    
    # def password_validator = RegexValidator(
    # regex="^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$",
    # message="Password must have at least 8 characters, including an uppercase letter, a lowercase letter, a number, and a special symbol."
    # )

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data['password1'])  # Hash password before saving
    #     if commit:
    #         user.save()
    #     return user