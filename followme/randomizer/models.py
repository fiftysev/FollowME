from django.db import models
from taggit.managers import TaggableManager


class Place(models.Model):
    place_name = models.CharField(max_length=120)
    place_photo = models.URLField(max_length=300)
    place_address = models.CharField(max_length=300, blank=True)
    place_station = models.CharField(max_length=120, blank=True)
    place_description = models.TextField()
    place_rating = models.FloatField()
    place_tags = TaggableManager()

    def __str__(self):
        return f'[{self.place_name}]'
