from . import views
from django.urls import path

urlpatterns = [
    path("profile", views.profile, name="profile"),
    path('update_user', views.update_u, name='update_user'),
]