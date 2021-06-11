from django.db import models


class Tag(models.Model):
    text = models.CharField(max_length=30)
    value = models.CharField(max_length=30, default=text)

    def __str__(self):
        return f'[{self.value}]'


class Place(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=120)
    photo = models.URLField(max_length=300)
    address = models.CharField(max_length=300, blank=True)
    station = models.CharField(max_length=120, blank=True)
    description = models.TextField()
    rating = models.FloatField(default=0)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'[{self.name}]'


