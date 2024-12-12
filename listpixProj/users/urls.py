# core/urls.py

from django.urls import path, re_path
from . import views

from django.shortcuts import redirect

def redirect_to_feed(request):
    return redirect('feed')

urlpatterns = [
    # Redirecting to Home Page to Feed Page
    path('', redirect_to_feed),
    # Signup Page
    path('signup/', views.signup, name='signup'),
    # Login
    path('login/', views.login_view, name='login'),
    # Logout
    path('logout/', views.logout_view, name='logout'),
    # Feed Page
    path('feed/', views.feed, name='feed'),
    # Post Create
    path('post/create/', views.post_create, name='post_create'),
    # Post Delete
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    # Comment on Posts
    path('post/<int:pk>/comment/', views.comment_create, name='comment_create'),
    # Delete Comment
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    # Like Post
    path('post/<int:pk>/like/', views.like, name='like'),
    # For fetching user the username on posts
    path('guest/profile/<str:username>/', views.guest_feed, name='guest_profile'),
    # Change Username
    path('profile/change-username/', views.change_username, name='change_username'),
    # Search Users
    path('search/', views.search_users, name='search_users'),
    # Other User's Profile
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    # User Profile Page
    path('user_profile/', views.user_profile, name='user_profile'),
    # Update User Screen
    path('update_user/', views.update_u, name='update_user'),
    # User Liked Posts
    path('user_liked/', views.user_liked, name='user_liked'),
]
