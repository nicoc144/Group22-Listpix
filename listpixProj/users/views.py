# core/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Post, Comment, Like
from .forms import PostForm, CommentForm, UsernameChangeForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .models import Profile

# Signup View
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

# Login View 
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('feed')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# Logout View 
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

# View for Logged In User Feed and Logged Out User Feed
def feed(request):        
    posts = Post.objects.select_related('task', 'user').prefetch_related('comments', 'likes').all().order_by('-created_at')
    if request.user.is_authenticated:
        current_user = request.user
        likes = Like.objects.filter(user=current_user).values_list('post_id', flat=True)
        return render(request, 'users/feed.html', {'posts': posts, 'likes' : likes})
    
    else:
        return render(request, 'users/guest_feed.html', {'posts': posts})
    
# View for Creating a Post
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            selected_task = form.cleaned_data.get('task')

            if selected_task:
                # Move task from assigned to completed
                request.user.profile.assigned_tasks.remove(selected_task)
                request.user.profile.completed_tasks.add(selected_task)
                post.task = selected_task

            post.save()
            return redirect('feed')
    else:
        form = PostForm(user=request.user)
    return render(request, 'users/post_create.html', {'form': form})

# View for Deleting a Post
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)
    
    if post.task:
        # Move the task from CompletedTask back to AssignedTask
        profile = request.user.profile
        profile.completed_tasks.remove(post.task)
        profile.assigned_tasks.add(post.task)

    post.delete()
    next_url = request.GET.get('next', 'feed')
    return redirect(next_url)

# View for Commenting on a Post
@login_required
def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            next_url = request.GET.get('next', 'feed')
            return redirect(next_url)
    else:
        form = CommentForm()
    return render(request, 'users/comment_create.html', {'form': form, 'post': post})

# View for Deleting a Comment
@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    comment.delete()
    next_url = request.GET.get('next', 'feed')
    return redirect(next_url)

# View for Liking a Post
@login_required
def like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like_obj, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like_obj.delete()
    like_count = Like.objects.filter(post=post).count()
    next_url = request.GET.get('next', 'feed')
    return redirect(next_url)

# View for showing a other user's profile for logged out users
def guest_feed(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user)
    return render(request, 'users/guest_profile.html', {'profile_user': user, 'posts': posts})

# View for changing a user's username
@login_required
def change_username(request):
    if request.method == 'POST':
        form = UsernameChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Update session to keep user logged in
            messages.success(request, 'Your username has been updated.')
            return redirect('user_profile', user.username)
    else:
        form = UsernameChangeForm(instance=request.user)
    return render(request, 'users/change_username.html', {'form': form})

# View for searching users
def search_users(request):
    query = request.GET.get('q', '')
    users = User.objects.filter(username__icontains=query) if query else []
    return render(request, 'users/search_users.html', {'users': users, 'query': query})

@login_required
def user_profile(request, username): 
    profile_user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(Profile, user=profile_user)
    posts = Post.objects.filter(user=profile_user).order_by('-created_at')
    user_form = UpdateUserForm(instance=profile_user)
    profile_form = UpdateProfileForm(instance=user_profile)
    likes = Like.objects.filter(user=profile_user)
    assigned_tasks = user_profile.assigned_tasks.all()
    completed_tasks = user_profile.completed_tasks.all()
    context = {
        'profile_user': profile_user,  
        'user_form': user_form,
        'profile_form': profile_form, 
        'posts': posts,
        'likes': likes,
        'assigned_tasks': assigned_tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, "users/user_profile.html", context)

@login_required
def user_liked(request): 
    current_user = request.user
    posts = Post.objects.all().order_by('-created_at')
    profile = Profile.objects.get(user=current_user)
    user_form = UpdateUserForm(instance = current_user)
    profile_form = UpdateProfileForm(instance = profile)
    likes = Like.objects.filter(user=current_user)
    context = {
        'user_form': user_form,
        'profile_form': profile_form, 
        'posts': posts,
        'likes' : likes
    }
    return render(request, "users/user_liked.html", context)

@login_required 
def update_u(request):
    current_user = request.user #get the current user and save it as obj User
    
    profile = Profile.objects.get(user=current_user) #each profile instance is 1 to 1 with a user, so set profile here
    
    if request.method == "POST": #check if user submitted a form to update profile
        user_form = UpdateUserForm(request.POST, instance=current_user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile) #need to request FILES for this form, because it handles images
        if user_form.is_valid() and profile_form.is_valid(): 
            user_form.save()
            profile_form.save()
            return redirect('user_profile', username=current_user.username)
    else: #not a post request, just fill out the forms with the user data (this is why you see the text boxes already filled out)
        user_form = UpdateUserForm(instance = current_user)
        profile_form = UpdateProfileForm(instance = profile)
    
    context = { #context is needed to pass forms into template
        'user_form': user_form,
        'profile_form': profile_form, 
    }
    
    return render(request, "users/update_user.html", context)
