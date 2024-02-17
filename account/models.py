from django.db import models
from django.contrib.auth.models import User as User_django_model
from django.utils import timezone
from tree.models import Tree

class Profile(models.Model):
    about = models.TextField(max_length=250, blank=True)
    joined = models.DateTimeField(default=timezone.now)

class User(models.Model):
    user = models.OneToOneField(User_django_model, on_delete=models.CASCADE)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    def plant_tree(tree:Tree, location):
        ...
    
    def plant_trees(plants):
        ...

class Account(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    users = models.ManyToManyField(User)
