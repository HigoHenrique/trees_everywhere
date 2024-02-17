from django.db import models
from django.utils import timezone

class PlantedTree(models.Model):
    age = models.IntegerField()
    planted_at = models.DateTimeField(default=timezone.now)
    account = models.ForeignKey(
        'account.Account',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'account.User',
        on_delete=models.CASCADE,
    )

class Tree(models.Model):
    name = models.CharField(max_length=50)
    scientific_name = models.CharField(max_length=150)
    plantedTree = models.ForeignKey(
        'PlantedTree',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )