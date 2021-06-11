from rest_framework import viewsets, generics
from .models import Place, FavoriteList
from .serializers import PlaceSerializer, FavoritesSerializer


class PlaceListView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class FavoritesTableView(generics.ListCreateAPIView):
    queryset = FavoriteList.objects.all()
    serializer_class = FavoritesSerializer
