# Generated by Django 5.0.2 on 2024-02-18 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_user_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account',
            field=models.ManyToManyField(blank=True, related_name='teste', to='account.account'),
        ),
    ]