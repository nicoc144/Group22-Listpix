# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, BucketListItem
import random

@receiver(post_save, sender=User)
def assign_random_tasks(sender, instance, created, **kwargs):
    if created:
        # Create the user's profile
        profile = Profile.objects.create(user=instance)

        # Define the number of tasks to assign
        task_count = 25  # Adjust the number of tasks you want to assign

        # Select a random sample of tasks
        all_tasks = BucketListItem.objects.all()
        assigned_tasks = random.sample(list(all_tasks), min(task_count, all_tasks.count()))

        # Add the selected tasks to the user's profile
        profile.assigned_tasks.set(assigned_tasks)
