from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path('', views.index, name='index'),
    path('user/login', views.login_view, name='login'),
    path('user/logout', views.logout_view, name='logout'),
]
