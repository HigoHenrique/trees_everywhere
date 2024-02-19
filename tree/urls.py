from django.urls import path
from tree import forms, views

app_name = 'tree'

urlpatterns = [
    path('<int:tree_id>/detail/', views.tree, name='tree'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    path('create/', forms.create_tree, name='create_tree')
    
]
