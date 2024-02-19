from django.db import models
from django.contrib.auth.models import User as User_django_model
from django.utils import timezone

class Profile(models.Model):
    about = models.TextField(max_length=250, blank=True)
    joined = models.DateTimeField(default=timezone.now)

class User(models.Model):
    user = models.OneToOneField(User_django_model, on_delete=models.CASCADE,)
    profile = models.OneToOneField(
        'Profile',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    account = models.ManyToManyField(
        'Account',
        blank=True,
        through='UserAccount'
    )

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
    

    # def plant_tree(tree:Tree, location):
    #     ...
    
    def plant_trees(plants):
        ...

class Account(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    users = models.ManyToManyField('User', blank=True, related_name='users')

    # def get_user(id):
    #     return User.objects.find(id=User.user_id)
    
    # def get_all_users():
    #     return Account.users.all()

    def __str__(self) -> str:
        return f'{self.name} - Active: {self.active}'


class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)