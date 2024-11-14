from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UpdateUserForm, UpdateProfileForm
from .models import Profile

# Create your views here.

#this is where the logic is handled

def profile(request): 
    context={}
    return render(request, "users/profile.html", context)

@login_required #only logged in users can access
def update_u(request):
    current_user = request.user #get the current user and save it as obj User
    
    profile = Profile.objects.get(user=current_user) #each profile instance is 1 to 1 with a user, so set profile here
    
    if request.method == "POST": #check if user submitted a form to update profile
        user_form = UpdateUserForm(request.POST, instance=current_user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile) #need to request FILES for this form, because it handles images
        if user_form.is_valid() and profile_form.is_valid(): 
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else: #not a post request, just fill out the forms with the user data (this is why you see the text boxes already filled out)
        user_form = UpdateUserForm(instance = current_user)
        profile_form = UpdateProfileForm(instance = profile)
    
    context = { #context is needed to pass forms into template
        'user_form': user_form,
        'profile_form': profile_form, 
    }
    
    return render(request, "users/update_user.html", context)