from django.shortcuts import render
from django.contrib.auth.models import User
from . import forms

# Create your views here.

#this is where the logic is handled

def profile(request): 
    context={}
    return render(request, "users/profile.html", context)

def update_u(request):
    current_user = User.objects.get(id = 1) #TODO: admin account is id 1, change this to request user id so other users can update 
    
    #TODO: add logic here if user user is not logged they cant view the update page
    return render(request, "users/update_user.html", {})