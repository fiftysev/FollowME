from django.urls import path
from .views import PlaceListView, FavoritesTableView


urlpatterns = [
    path('get_places/', PlaceListView.as_view(), name='get_places'),
    path('get_favorites', FavoritesTableView.as_view(), name='show_favorites'),
]

