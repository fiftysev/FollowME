from django.conf.urls import url
from django.urls import path, include
from .views import PlaceView, PlaceView, RegistrationUserView, UserListView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', PlaceView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('registration/', RegistrationUserView.as_view(), name='registration'),
    path('userlist/', UserListView.as_view(), name='UserList')
]
