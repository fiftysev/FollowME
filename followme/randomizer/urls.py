from django.urls import path
from .views import PlaceList


urlpatterns = [
    path('get_places/', PlaceList.as_view(), name='get_places'),
]

