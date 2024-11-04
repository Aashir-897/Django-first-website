from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    body = models.TextField()
    submit = models.TextField(default="No submission provided")
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.name
    
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128) 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.username
    
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=100)
    github_url = models.URLField(blank=True, null=True)
    code_snippet = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)  # Add this line

    def __str__(self):
        return self.title

    
