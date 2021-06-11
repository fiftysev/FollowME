from rest_framework import serializers
from .models import Place, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag_name']


class PlaceSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Place
        fields = ['id', 'name', 'photo',
                  'address', 'description', 'station',
                  'rating', 'tags']