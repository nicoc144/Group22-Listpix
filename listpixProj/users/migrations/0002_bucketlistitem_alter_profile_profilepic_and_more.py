# Generated by Django 5.1.2 on 2024-11-11 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BucketListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='assigned_tasks',
            field=models.ManyToManyField(blank=True, to='users.bucketlistitem'),
        ),
    ]