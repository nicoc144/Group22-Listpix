from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#forms are a way for the user to submit data for the web app

#post form

class UpdateUserForm(forms.ModelForm): 
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']

class UpdateProfileForm(forms.ModelForm):    
    class Meta:
        model = Profile
        fields = ['bio', 'profilePic']