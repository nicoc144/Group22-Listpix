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
    current_user = request.user 
    
    profile = Profile.objects.get(user=current_user)
    
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=current_user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance = current_user)
        profile_form = UpdateProfileForm(instance = profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form, 
    }
    
    #TODO: add logic here if user user is not logged they cant view the update page
    return render(request, "users/update_user.html", context)