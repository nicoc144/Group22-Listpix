from django.contrib.auth.models import User #import user objects from django (this will manage the list of users)
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #1 to 1 relationship of the profile model with the user model
                                                                #when the parent (user) is deleted, the child (profile) is also deleted
    bio = models.TextField(blank=True)
    profilePic = models.ImageField(null = True, blank = True, upload_to='profile_pics', height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return str(self.user)

class Post(models.Model): #maybe move this class into a separate post app 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=55)
    image = models.ImageField(null = True, blank = True, upload_to='post_images', height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(auto_now_add=True) #save time and date for each post
    
    def __str__(self):
        return self.caption + ' | ' + self.author
    

#this is the data corresponding to the data in the database (ie user table would have username, password, maybe email)
