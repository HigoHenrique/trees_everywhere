# Generated by Django 5.0.2 on 2024-02-18 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0002_plantedtree_location_lat_plantedtree_location_long'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tree',
            name='plantedTree',
        ),
        migrations.AddField(
            model_name='plantedtree',
            name='tree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tree.tree'),
        ),
    ]
