from django.urls import path
from .views import PlaceListView


urlpatterns = [
    path('get_places/', PlaceListView.as_view(), name='get_places'),
]

