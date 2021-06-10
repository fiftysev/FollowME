from rest_framework import viewsets, generics
from .models import Place
from .serializers import PlaceSerializer


class PlaceList(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
