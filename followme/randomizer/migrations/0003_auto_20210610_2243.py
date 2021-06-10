# Generated by Django 3.2.4 on 2021-06-10 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomizer', '0002_auto_20210610_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_rating',
            field=models.FloatField(default=0),
        ),
    ]
