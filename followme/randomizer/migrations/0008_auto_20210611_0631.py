# Generated by Django 3.2.4 on 2021-06-11 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomizer', '0007_auto_20210611_0631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='value',
        ),
        migrations.AddField(
            model_name='tag',
            name='tag_value',
            field=models.CharField(default='None', max_length=30),
        ),
    ]