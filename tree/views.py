from django.shortcuts import render
from tree.models import Tree, PlantedTree

def index(req):
    trees = Tree.objects.filter(plantedTree_id=1).values()

    context = {
        'trees': trees,
    }
    return render(
        req,
        'tree/index.html',
        context
    )
