# Generated by Django 3.2.4 on 2021-06-11 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomizer', '0009_rename_tag_value_tag_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='value',
            field=models.CharField(default='tag', max_length=30),
        ),
    ]