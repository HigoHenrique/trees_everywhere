from django.db import models
from django.utils import timezone

class PlantedTree(models.Model):
    age = models.IntegerField(verbose_name='Ano')
    planted_at = models.DateTimeField(default=timezone.now)
    location_lat = models.DecimalField(verbose_name='latitude', max_digits=25, decimal_places=16,)
    location_long = models.DecimalField(verbose_name='longitude', max_digits=25, decimal_places=16,)
    account = models.ForeignKey(
        'account.Account',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'account.User',
        on_delete=models.SET_NULL,
        null=True
    )

    def get_all_tree_for_user(user):
        planted = PlantedTree.objects.filter(user=user)
        trees = Tree.objects.filter(plantedTree_id__in=[tree.id for tree in planted])
        return trees

    def __str__(self) -> str:
        return f'{self.account} - {self.user}'

class Tree(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    scientific_name = models.CharField(max_length=150, verbose_name='Nome Científico')
    plantedTree = models.ForeignKey(
        PlantedTree,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def get_list_tree(search_value):
        return Tree.objects.filter(models.Q(name__icontains=search_value) | models.Q(scientific_name__icontains=search_value))
    
    def __str__(self) -> str:
        return f'{self.name}'