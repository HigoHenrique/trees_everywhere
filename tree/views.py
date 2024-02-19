from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from tree.models import Tree, PlantedTree

@login_required(login_url='account:login')
def index(req):
    user = req.user
    print(user.id)
    trees = PlantedTree.get_all_tree_for_user(user)
    paginator = Paginator(trees, 1)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(
        req,
        'tree/index.html',
        context
    )

@login_required(login_url='account:login')
def search(req):
    # trees = Tree.objects.filter(plantedTree_id=1).values()
    search_value = req.GET.get('q', '').strip()
    if search_value == '':
        return redirect('tree:index')

    trees = Tree.get_tree(search_value)
    paginator = Paginator(trees, 1)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'search_value':search_value,
    }
    return render(
        req,
        'tree/index.html',
        context,
    )

@login_required(login_url='account:login')
def tree(req, tree_id):
    single_tree = get_object_or_404(Tree, pk=tree_id)
    page_title = f'{single_tree.name} - '
    context = {
        'tree': single_tree,
        'page_title': page_title
    }
    return render(
        req,
        'tree/tree.html',
        context
    )
