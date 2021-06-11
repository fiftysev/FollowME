from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from .models import Place
from .serializers import PlaceSerializer


class PlaceView(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

