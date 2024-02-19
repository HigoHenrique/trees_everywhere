from django.contrib import admin
from tree.models import PlantedTree, Tree

@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'scientific_name', 'plantedTree',
    list_display_links = 'id', 'name', 'scientific_name', 'plantedTree',
    search_fields = 'id', 'name', 'scientific_name',

class TreeInline(admin.TabularInline):
    model = Tree

@admin.register(PlantedTree)
class PlantedTreeAdmin(admin.ModelAdmin):
    list_display =  'id', 'planted_at','age', 'location_lat', 'location_long', 'account', 'user',
    list_display_links = 'id','age', 'planted_at', 'location_lat', 'location_long', 'account', 'user',
    search_fields = 'id', 'location_lat', 'location_long',
    inlines = (TreeInline),