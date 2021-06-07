from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['place_name', 'place_photo',
                  'place_address', 'place_station',
                  'place_description', 'place_rating',
                  'place_tags']
