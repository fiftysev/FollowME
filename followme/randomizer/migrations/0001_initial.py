# Generated by Django 3.2.4 on 2021-06-07 13:35

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=120)),
                ('place_photo', models.URLField(blank=True, max_length=300)),
                ('place_address', models.CharField(max_length=300)),
                ('place_station', models.CharField(max_length=120)),
                ('place_description', models.TextField()),
                ('place_rating', models.FloatField()),
                ('place_url', models.URLField(blank=True, max_length=300)),
                ('place_tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
