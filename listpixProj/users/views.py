from django.shortcuts import render

# Create your views here.

#this is where the logic is handled

def profile(request): 
    context={}
    return render(request, "users/profile.html", context)
