from django.contrib import admin
from tree.models import PlantedTree, Tree
@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    ...

@admin.register(PlantedTree)
class PlantedTreeAdmin(admin.ModelAdmin):
    ...