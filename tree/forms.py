from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from tree.models import Tree, PlantedTree
from django import forms

class TreeForm(forms.ModelForm):
    class Meta:
        model = Tree
        fields = ('name', 'scientific_name', 'plantedTree')


class PlantedTreeForm(forms.ModelForm):
    class Meta:
        model = PlantedTree
        fields = ('age', 'planted_at', 'location_lat', 'location_long', 'account', 'user')



def create_plantedtree(req, pk):
    planted_tree = PlantedTree.objects.get(pk=pk)
    TreeFormSet = forms.inlineformset_factory(PlantedTree, Tree, form=TreeForm, extra=1)
    if req.method == 'POST':
        formset = TreeFormSet(req.POST, instance=planted_tree)
        context = {
            'formset': formset,
        }
        return render(
            req,
            'tree/create.html',
            context
        )

    context = {
        'formset': formset,
    }
    return render(
        req,
        'tree/create.html',
        context
    )

def create_tree(req):
    TreeFormSet = forms.inlineformset_factory(PlantedTree, Tree, form=TreeForm, extra=1)
    form = PlantedTreeForm(req.POST)
    formset = TreeFormSet(req.POST)
    if req.method == 'POST':
        context = {
            'form': form,
            'formset': formset,
        }
        return render(
            req,
            'tree/create.html',
            context
        )

    context = {
         'form': form,
        formset:formset,
    }
    return render(
        req,
        'tree/create_tree.html',
        context
    )