# Generated by Django 3.2.4 on 2021-06-07 14:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('randomizer', '0003_auto_20210607_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='users',
            field=models.ManyToManyField(related_name='favorite_place', to=settings.AUTH_USER_MODEL),
        ),
    ]