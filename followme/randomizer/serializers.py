from rest_framework import serializers
from .models import Place, Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['value', 'text']


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True)
    # other_photos = serializers.ListSerializer(many=True)

    class Meta:
        model = Place
        fields = ['id', 'name', 'photo',
                  'address', 'description', 'station',
                  'rating', 'tags']

