# Generated by Django 5.0.2 on 2024-02-18 03:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_profile_user_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='users',
        ),
        migrations.RemoveField(
            model_name='user',
            name='accounts',
        ),
        migrations.AddField(
            model_name='user',
            name='accounts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.account'),
        ),
    ]