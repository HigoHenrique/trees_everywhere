# Generated by Django 5.0.2 on 2024-02-18 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_user_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='users',
        ),
        migrations.AlterField(
            model_name='user',
            name='account',
            field=models.ManyToManyField(blank=True, related_name='accounts', to='account.account'),
        ),
    ]