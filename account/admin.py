from django.contrib import admin
from account.models import Account, User, Profile

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name','active')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ...
    

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...