from django.db import models
from django.utils import timezone

class PlantedTree(models.Model):
    age = models.IntegerField()
    planted_at = models.DateTimeField(default=timezone.now)
    location_lat = models.DecimalField(verbose_name='latitude', max_digits=25, decimal_places=16, blank=True, null=True)
    location_long = models.DecimalField(verbose_name='longitude', max_digits=25, decimal_places=16, blank=True, null=True)
    account = models.ForeignKey(
        'account.Account',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'account.User',
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f'{self.account} - {self.user}'

class Tree(models.Model):
    name = models.CharField(max_length=50)
    scientific_name = models.CharField(max_length=150)
    plantedTree = models.ForeignKey(
        'PlantedTree',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f'{self.name}'