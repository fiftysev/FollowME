from rest_framework import serializers
from .models import Place, Tag, FavoriteList


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['value', 'text']


class PlaceSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Place
        fields = ['id', 'name', 'photo',
                  'address', 'description', 'station',
                  'rating', 'tags']


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteList
        fields = ['user', 'place']
