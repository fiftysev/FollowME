from django.db import models


class Place(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=120)
    photo = models.URLField(max_length=300)
    address = models.CharField(max_length=300, blank=True)
    station = models.CharField(max_length=120, blank=True)
    description = models.TextField()
    rating = models.FloatField(default=0)

    def __str__(self):
        return f'[{self.name}]'


class Tag(models.Model):
    tag_name = models.CharField(max_length=30)

