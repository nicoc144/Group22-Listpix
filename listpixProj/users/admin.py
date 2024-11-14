from django.contrib import admin
from .models import Profile, Post, Comment, Like, BucketListItem

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(BucketListItem)
admin.site.register(Comment)
admin.site.register(Like)
