from django.shortcuts import render, redirect
from tree.models import Tree, PlantedTree
from account.models import User
from django import forms
from django.contrib.auth.decorators import login_required
class TreeForm(forms.ModelForm):
    class Meta:
        model = Tree
        fields = ('name', 'scientific_name')
        exclude = ('plantedTree',)

class PlantedTreeForm(forms.ModelForm):
    class Meta:
        model = PlantedTree
        fields = ('age', 'location_lat', 'location_long', 'account', 'user')
        exclude = ('user','planted_at',)

@login_required(login_url='account:login')
def create_tree(request):
    user = request.user.user
    form = PlantedTreeForm()
    formset = TreeForm()
    if request.method == 'POST':
        form = PlantedTreeForm(request.POST or None)
        formset = TreeForm(request.POST)
        if form.is_valid():
            planted_tree = form.save(commit=False)
            planted_tree.user = user
            planted_tree.save()
            if formset.is_valid():
                tree = formset.save(commit=False)
                tree.plantedTree = planted_tree
                tree.save()
            return redirect('tree:index')
        
        form = PlantedTreeForm()
        formset = TreeForm()

        context = {
            'form': form,
            'formset': formset,
            'user': user
        }
        return render(
            request,
            'tree/create_tree.html',
            context
        )

    context = {
         'form': form,
        'formset':formset,
    }
    return render(
        request,
        'tree/create_tree.html',
        context
    )