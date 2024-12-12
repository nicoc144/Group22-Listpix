from django import forms
from .models import Post, Comment, Profile, BucketListItem
from django.contrib.auth.models import User

class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class PostForm(forms.ModelForm):
    task = forms.ModelChoiceField(
        queryset=BucketListItem.objects.none(),
        required=False,
        label="Select a Task"
    )
        
    class Meta:
        model = Post
        fields = ['content', 'image']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['task'].queryset = user.profile.assigned_tasks.all()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class UpdateUserForm(forms.ModelForm): 
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']

class UpdateProfileForm(forms.ModelForm):    
    class Meta:
        model = Profile
        fields = ['bio', 'profilePic']
