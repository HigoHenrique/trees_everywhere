from django.contrib import admin
from account.models import Account, User, Profile

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = 'id','name','created','active',
    list_display_links= 'id','name','created',
    list_editable= 'active',

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = 'id','user', 'profile',
    list_display_links= 'id','user', 'profile',

    

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...