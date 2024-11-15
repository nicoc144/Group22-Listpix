from django.contrib.auth.models import User #import user objects from django (this will manage the list of users)
from django.db import models
import random

class Post(models.Model): #maybe move this class into a separate post app 
    content = models.CharField(max_length=55)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(null = True, blank = True, upload_to='post_images', height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username + ' | ' + self.content}..."
    

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.content[:20]}..."

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"{self.user.username} liked {self.post.content[:20]}..."

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #1 to 1 relationship of the profile model with the user model
                                                                #when the parent (user) is deleted, the child (profile) is also deleted
    bio = models.TextField(blank=True)
    profilePic = models.ImageField(null = True, blank = True, upload_to='profile_pics', height_field=None, width_field=None, max_length=None)
    
    assigned_tasks = models.ManyToManyField('BucketListItem', blank=True)

    def __str__(self):
        return str(self.user)

#this is the data corresponding to the data in the database (ie user table would have username, password, maybe email)
    
class BucketListItem(models.Model):
    task_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.task_name
    
#data of bucket list items/tasks
