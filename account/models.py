from django.db import models
from django.contrib.auth.models import User as User_django_model
from django.utils import timezone
from tree.models import Tree

class Profile(models.Model):
    about = models.TextField(max_length=250, blank=True)
    joined = models.DateTimeField(default=timezone.now)

class User(models.Model):
    user = models.OneToOneField(User_django_model, on_delete=models.CASCADE)
    profile = models.OneToOneField(
        'Profile',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    account = models.ManyToManyField(
        'Account',
        blank=True,
        related_name='accounts'
    )

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
    

    def plant_tree(tree:Tree, location):
        ...
    
    def plant_trees(plants):
        ...

class Account(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name} - Active: {self.active}'
